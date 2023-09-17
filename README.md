# html2md: Convert Web Pages to Markdown

`html2md` is a Python-based tool that leverages the power of the Postlight Parser to convert web pages into clean and readable Markdown format.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/) and npm (usually bundled with Node.js)

## Setup

### 1. Clone the Repository

To get started, first clone the `html2md` repository, ensuring you also fetch the included submodules:

```bash
git clone --recursive https://github.com/rocklandceo/html2md.git

```

If you've already cloned the repository without the `--recursive` flag, you can fetch the submodules using:

```bash
git submodule update --init

```

### 2. Install Dependencies

Navigate to the root directory of the `html2md` project and run the provided setup script:

```bash
./setup.sh

```

This script will install both the Python requirements and the npm dependencies for the Postlight Parser.

If you're on a system that doesn't support bash scripts, you can manually install the dependencies:

**Python dependencies**:

```bash
pip install -r requirements.txt

```

**Parser dependencies**:

```bash
cd parser
npm install

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
