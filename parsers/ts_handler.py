import re

def parse(content):
    """
    Parses TypeScript content to extract functions, classes, and imports.
    """
    functions = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', content)
    classes = re.findall(r'class\s+([a-zA-Z0-9_]+)', content)
    imports = re.findall(r'import\s+.*\s+from\s+[\'"](.*?)[\'"]', content)
    
    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
    }


