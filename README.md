# File: README.md
# Version: 1.1.0

# Objective
Building a complete local CLI solution in VS Code that:
* Documents the directory structure, files and codebase
* Takes any codebase (PHP, JS, TS, TSX, HTML, CSS, SCSS, SQL) AND other text files (MD, PO, POT, SH, TXT, YAML, YML)
* Analyzes code functions, classes, comments, and database interactions
* Documents the codebase for further detailed queries
* Analyzes DB schema (if exists): tables, indexes, views, stored procedures, triggers
* Analyzes DB sample data (if exists) from: tables
* Documents the database structure and queries
* Creates dependency relationships
* Builds intermediate files (JSON/Markdown) to prepare for AI Queries
* Offers ChatGPT prompt examples for querying code and db

## Setup
Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
```bash
python analyze.py
```

```bash
python prompt.py 'Write your AI prompt here'
```

## Output
- `/output/parsed_files.json` – intermediary code and db metadata
- `/output/dependency_graph.gv` – Graphviz dependency graph
- `/output/documentation.md` – generated documentation
- `/output/answer.md` – generated answer from query

# Project Structure
```
CodeReview/
│── analyze.py                  # Main entrypoint: walks /src, routes to parsers, aggregates results
│── config.yaml                 # Settings for INCLUDE_SQL, API keys, supported extensions, etc.
│── requirements.txt            # Python deps
│── .env                        # Environment vars
│── GEMINI.md                   # Usage & querying guide for Gemini in VS Code
│
├── modules/
│   ├── config_loader.py
│   ├── agent_logic.py
│   ├── file_utils.py
│   └── providers/
│       ├── base_provider.py
│       ├── ollama_provider.py
│       ├── openai_provider.py
│       ├── gemini_provider.py
│       └── manager.py
│
├── parsers/
│   ├── handlers.py
│   ├── css_handler.py          # CSS parser
│   ├── html_handler.py         # HTML parser
│   ├── js_handler.py           # JavaScript parser
│   ├── json_handler.py         # JSON parser
│   ├── md_handler.py           # Markdown parser
│   ├── php_handler.py          # PHP parser
│   ├── po_handler.py           # .po Translations parser
│   ├── pot_handler.py          # .pot Translations parser
│   ├── py_handler.py           # Python parser
│   ├── scss_handler.py         # SCSS parser
│   ├── sh_handler.py           # Shell parser
│   ├── sql_handler.py          # SQL parser
│   ├── ts_handler.py           # TypeScript parser
│   ├── tsx_handler.py          # TypeScript parser
│   ├── tst_handler.py          # Textfile parser
│   ├── yaml_handler.py         # YAML parser
│   ├── yal_handler.py          # YAML parser
│
├── outputs/
│   ├── intermediate_json/      # One JSON per file after parsing
│   ├── markdown_docs/          # Generated docs per plugin
│
└── src/                        # Source root
│   ├── code/                   # Multiple Code Files
│   ├── db/                     # SQL schema + optional sample data
│   │   ├── schema.sql
│   │   ├── sample_data.sql
```
