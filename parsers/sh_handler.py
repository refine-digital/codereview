import re

def parse(content):
    """
    Parses Shell script content to extract functions and variables.
    """
    functions = re.findall(r'([a-zA-Z0-9_]+)\s*\(\)', content)
    variables = re.findall(r'([A-Z_]+)=', content)
    
    return {
        "functions": functions,
        "variables": variables,
    }

