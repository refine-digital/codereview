import re

def parse(content):
    """
    Parses Markdown content to extract headings and links.
    """
    headings = re.findall(r'#+\s+(.*)', content)
    links = re.findall(r'\[.*?\]\((.*?)\)', content)
    
    return {
        "headings": headings,
        "links": links,
    }

