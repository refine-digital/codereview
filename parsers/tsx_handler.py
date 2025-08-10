def parse(content):
    # TODO: Implement parsing logic for .ts
    return {"type": "tsx", "length": len(content), "preview": content[:100]}
