# CSS styling and glob support was vibe coded.

import markdown
import argparse
import os
import glob

# Setup argparse
parser = argparse.ArgumentParser(
    prog="Markdown to HTML Converter",
    description="Converts Markdown files to HTML format."
)
parser.add_argument("filenames", nargs='+', help="Markdown file(s) to convert (supports glob patterns)")
parser.add_argument("-t", "--test", action="store_true", help="Test mode - print HTML to stdout instead of writing to file")

args = parser.parse_args()

# Main functions
def main(input_file, styles=""):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    html_content = markdown.markdown(content)
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>{styles}</style>
</head>
<body>{html_content}</body>
</html>"""

def to_html_file(input_file):
    output_file = os.path.splitext(input_file)[0] + ".html"
    styles = """
    body {
        background-color: #333;
        color: white;
        font-family: Arial, sans-serif;
        margin: 50px;
        padding: 50px;
        max-width: 1200px;
    }
    h1, h2, h3, h4, h5, h6 {
        margin-top: 20px;
        margin-bottom: 10px;
    }
    p {
        margin-bottom: 15px;
        line-height: 1.6;
    }
    img:not([width]) {
        max-width: 500px;
        height: auto;
        display: block;
        margin: 20px 0;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    img[width] {
        display: inline-block;
        margin: 10px 5px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    blockquote {
        border-left: 4px solid #666;
        padding-left: 20px;
        margin: 20px 0;
        font-style: italic;
        color: #ccc;
    }
    a {
        color: #66b3ff;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    code {
        background-color: #444;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
    }
    """
    html_content = main(input_file, styles)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

# Function calls
# Expand glob patterns and collect all files
all_files = []
for pattern in args.filenames:
    # Check if pattern contains glob characters
    if '*' in pattern or '?' in pattern or '[' in pattern:
        expanded = glob.glob(pattern)
        if not expanded:
            print(f"Warning: No files matched pattern '{pattern}'")
        all_files.extend(expanded)
    else:
        all_files.append(pattern)

# Filter for markdown files only
markdown_files = [f for f in all_files if f.endswith('.md')]

if not markdown_files:
    print("Error: No markdown files found to convert")
    exit(1)

# Process each file
if not args.test:
    for input_file in markdown_files:
        if not os.path.exists(input_file):
            print(f"Warning: File '{input_file}' does not exist, skipping...")
            continue
        print(f"Converting {input_file}...")
        to_html_file(input_file)
    print(f"\nSuccessfully converted {len(markdown_files)} file(s)")
else:
    # Test mode - only process first file
    if markdown_files:
        print(main(markdown_files[0]))

