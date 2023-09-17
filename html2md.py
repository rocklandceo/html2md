import html2text
import requests
import os
import re
import subprocess
import json
from bs4 import BeautifulSoup

def parse_with_postlight_parser(url):
    # Define the path to the cli.js script inside the parser submodule
    cli_path = './parser/cli.js'
    
    # Use subprocess to run the script and capture the output
    result = subprocess.check_output(['node', cli_path, url])
    
    # Parse the JSON output to get the parsed content
    parsed_data = json.loads(result)
    return parsed_data.get('content', '')

if __name__ == "__main__":
    url = input("Enter the URL: ")
    
    # Parse the content using Postlight Parser
    html_content = parse_with_postlight_parser(url)
    
    # Convert the HTML content to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown_content = h.handle(html_content)
    
    # Extract title for filename using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    title_element = soup.find('title')
    title = title_element.text if title_element else "default-title"
    formatted_title = re.sub('[^a-zA-Z0-9\s]', '', title).replace(' ', '-').lower()
    
    # Define the path for the markdown file
    output_directory = "converted-files"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    markdown_output_path = os.path.join(output_directory, f"{formatted_title}.md")
    
    # Save the Markdown content
    with open(markdown_output_path, "w", encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Content from the URL has been parsed and saved to '{markdown_output_path}'.")

