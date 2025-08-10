import re

def parse(content):
    functions = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', content)
    arrow_functions = re.findall(r'(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*\(', content)
    classes = re.findall(r'class\s+([a-zA-Z0-9_]+)', content)
    imports = re.findall(r'import\s+.*\s+from\s+[\'"](.*?)[\'"]', content)
    
    # Improved comment extraction
    raw_comments = re.findall(r'//.*|/\*[\s\S]*?\*/', content)
    
    # Filter and trim comments
    comments = []
    for comment in raw_comments:
        stripped_comment = comment.strip()
        if stripped_comment.startswith('//') and len(stripped_comment) < 20:
            continue
        comments.append(stripped_comment[:150])

    return {
        "type": "js",
        "functions": functions + arrow_functions,
        "classes": classes,
        "imports": imports,
        "comments": comments,
        "length": len(content),
        "preview": content[:250]
    }
