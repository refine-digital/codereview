import re

def parse(content):
    """
    Parses SQL content to extract tables and columns.
    """
    tables = re.findall(r'CREATE TABLE\s+([a-zA-Z0-9_]+)', content)
    columns = re.findall(r'(\w+)\s+(?:INT|VARCHAR)', content)
    
    return {
        "tables": tables,
        "columns": columns,
    }
