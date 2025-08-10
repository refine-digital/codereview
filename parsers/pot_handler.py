import re

def parse(content):
    """
    Parses POT file content to extract msgid entries.
    """
    msgids = re.findall(r'msgid "(.*?)"', content)
    
    return {
        "msgids": msgids,
    }

