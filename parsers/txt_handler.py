def parse(content):
    """
    Parses TXT content to extract paragraphs.
    """
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
    
    return {
        "paragraphs": paragraphs,
    }


