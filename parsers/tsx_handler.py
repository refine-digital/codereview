import re

def parse(content):
    """
    Parses TSX content to extract functions, interfaces, and imports.
    """
    functions = re.findall(r'const\s+([a-zA-Z0-9_]+)', content)
    interfaces = re.findall(r'interface\s+([a-zA-Z0-9_]+)', content)
    imports = re.findall(r'import\s+.*\s+from\s+[\'"](.*?)[\'"]', content)
    
    return {
        "functions": functions,
        "interfaces": interfaces,
        "imports": imports,
    }


