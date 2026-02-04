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
def main(input_file, styles=""):
    with open(input_file, "r") as f:
        content = f.read()
    html_content = markdown.markdown(content)
    return f"<html><head><style>{styles}</style></head><body>{html_content}</body></html>"

def to_html_file(input_file):
    output_file = os.path.splitext(input_file)[0] + ".html"
    styles = """
    body {
        background-color: #333;
        color: white;
        font-family: Arial, sans-serif;
        margin: 50px;
        padding: 50px;
    }
    h1, h2, h3, h4, h5, h6 {
        margin-top: 20px;
        margin-bottom: 10px;
    }
    p {
        margin-bottom: 15px;
    }
    """
    html_content = main(input_file, styles)
    with open(output_file, "w") as f:
        f.write(html_content)

# Function calls
if not args.test:
    to_html_file(args.filename)
else:
    print(main(args.filename))
