import ast

def parse(content):
    try:
        tree = ast.parse(content)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
        from_imports = [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
        return {
            "functions": functions,
            "classes": classes,
            "imports": imports,
            "from_imports": from_imports,
            "type": "py",
            "length": len(content),
            "preview": content[:250]
        }
    except SyntaxError as e:
        return {"error": f"Syntax error: {e}"}
