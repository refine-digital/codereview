import re

def parse(content):
    """
    Parses PO file content to extract msgid and msgstr entries.
    """
    entries = {}
    matches = re.findall(r'msgid "([^"]*)"\s+msgstr "([^"]*)"', content)
    for msgid, msgstr in matches:
        entries[msgid] = msgstr
    
    return {
        "entries": entries,
    }

