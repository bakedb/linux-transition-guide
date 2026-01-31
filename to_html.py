import markdown
import argparse
import os

# Setup argparse
parser = argparse.ArgumentParser(
    prog="Markdown to HTML Converter",
    description="Converts Markdown files to HTML format."
)
parser.add_argument("filename")
parser.add_argument("-t", "--test", action="store_true")

args = parser.parse_args()

# Main functions
def main(input_file):
    with open(input_file, "r") as f:
        content = f.read()
    return markdown.markdown(content)

def to_html_file(input_file):
    output_file = os.path.splitext(input_file)[0] + ".html"  # Use input_file to derive output filename
    html_content = main(input_file)
    with open(output_file, "w") as f:
        f.write(html_content)

# Function calls
if not args.test:
    to_html_file(args.filename)
else:
    print(main(args.filename))
