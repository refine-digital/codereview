from . import php_handler, js_handler, css_handler, scss_handler, sql_handler, ts_handler, py_handler, yaml_handler, yml_handler, json_handler, po_handler, pot_handler, txt_handler, md_handler, html_handler, sh_handler

handlers = {
    'php': php_handler.parse,
    'js': js_handler.parse,
    'css': css_handler.parse,
    'scss': scss_handler.parse,
    'sql': sql_handler.parse,
    'ts': ts_handler.parse,
    'py': py_handler.parse,
    'yaml': yaml_handler.parse,
    'yml': yml_handler.parse,
    'json': json_handler.parse,
    'po': po_handler.parse,
    'pot': pot_handler.parse,
    'txt': txt_handler.parse,
    'md': md_handler.parse,
    'html': html_handler.parse,
    'sh': sh_handler.parse,
}
