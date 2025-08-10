import yaml

def get_keys(obj):
    keys = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            keys.append(key)
            keys.extend(get_keys(value))
    elif isinstance(obj, list):
        for item in obj:
            keys.extend(get_keys(item))
    return keys

def parse(content):
    """
    Parses YML content to extract all keys.
    """
    try:
        data = yaml.safe_load(content)
        keys = get_keys(data)
        return {
            "keys": keys,
        }
    except yaml.YAMLError:
        return {
            "keys": [],
        }

