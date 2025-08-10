# File: parsers/php_handler.py
# Version: 1.1.0
import re

def parse(content):
    """
    Parses PHP content to extract namespaces, classes, and functions.
    """
    namespaces = re.findall(r'namespace\s+([^;]+);', content)
    classes = re.findall(r'class\s+([a-zA-Z0-9_]+)', content)
    functions = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', content)
    
    return {
        "namespaces": namespaces,
        "classes": [{"name": c, "extends": None} for c in classes],
        "functions": [{"name": f, "parameters": ""} for f in functions],
    }

