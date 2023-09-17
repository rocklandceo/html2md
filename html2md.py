import html2text
import requests
import os
import re
from bs4 import BeautifulSoup

def html_to_markdown(url):
    # Fetch HTML content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Use BeautifulSoup to extract the title from the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    title_element = soup.find('title')  # Assuming the title is within <title> tags
    title = title_element.text if title_element else "default-title"
    
    # Format the title to be used as a filename
    formatted_title = re.sub('[^a-zA-Z0-9\s]', '', title).replace(' ', '-').lower()

    # Convert HTML to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown_content = h.handle(response.text)

    return formatted_title, markdown_content

if __name__ == "__main__":
    url = input("Enter the URL: ")
    formatted_title, markdown_content = html_to_markdown(url)

    # Ensure 'converted-files' directory exists or create it
    output_directory = "converted-files"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Define the path for the markdown file
    markdown_output_path = os.path.join(output_directory, f"{formatted_title}.md")

    # Save the Markdown content
    with open(markdown_output_path, "w", encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"HTML content from the URL has been converted and saved to '{markdown_output_path}'.")
