import re

def parse(content):
    """
    Parses SCSS content to extract variables and mixins.
    """
    variables = re.findall(r'(\$.*?):', content)
    mixins = re.findall(r'@mixin\s+(.*?)\(', content)
    
    return {
        "variables": variables,
        "mixins": mixins,
    }

