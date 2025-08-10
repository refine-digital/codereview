import re

def parse(content):
    # Simple selector extraction
    selectors = re.findall(r'([a-zA-Z0-9_#\.\- ]+)\s*{', content)
    
    # Simple rule extraction (within curly braces)
    rules = re.findall(r'{([^}]+)}', content)
    
    return {
        "type": "css",
        "selectors": [s.strip() for s in selectors],
        "rules": [r.strip() for r in rules],
        "length": len(content),
        "preview": content[:250]
    }
