from bs4 import BeautifulSoup

def parse(content):
    soup = BeautifulSoup(content, 'html.parser')
    
    significant_tags = ['a', 'script', 'img', 'form', 'input', 'textarea', 'select', 'button', 'h1', 'h2', 'h3']
    tags = [tag.name for tag in soup.find_all(significant_tags)]
    
    links = [link.get('href') for link in soup.find_all('a') if link.get('href')]
    
    scripts = [script.get('src') for script in soup.find_all('script') if script.get('src')]
    
    return {
        "type": "html",
        "tags": tags,
        "links": links,
        "scripts": scripts,
        "length": len(content),
        "preview": content[:250]
    }
