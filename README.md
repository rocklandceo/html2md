```markdown
# html2md: Convert Web Pages to Markdown

`html2md` is a Python-based tool that converts web pages into clean and readable Markdown format.

## Prerequisites

- [Python](https://www.python.org/downloads/)

## Setup

### 1. Clone the Repository

To get started, first clone the `html2md` repository:

```bash
git clone https://github.com/rocklandceo/html2md.git
```

### 2. Install Dependencies

Navigate to the root directory of the `html2md` project and install the Python requirements:

```bash
pip install -r requirements.txt
```

### 3. Usage

After setting up, you can use the `html2md.py` script to convert web pages to Markdown:

```bash
python html2md.py
```

If you're using Python 3 and have both Python 2 and Python 3 installed on your machine, you might need to use:

```bash
python3 html2md.py
```

The script will prompt you to enter the URL of the web page you wish to convert. After processing, the converted content will be saved in the `converted-files` directory with a filename based on the webpage's title.

## License

Please ensure you comply with the licensing terms of the tools and libraries used in this project.
```

You can replace the content of your current `readme.md` file with the updated version provided above. After updating the `readme.md` file, make sure to commit and push the changes to your GitHub repository:

```bash
git add readme.md
git commit -m "Updated readme.md after removing parser submodule"
git push origin main
```
