# Project: Code Review & Documentation Generator

## Project Overview

This project is a command-line tool that analyzes a given codebase and generates documentation, dependency graphs, and structured data for AI-powered querying. It's designed to work with a variety of programming and markup languages, including PHP, JavaScript, Python, and SQL. The tool parses the source code, extracts key information like classes, functions, and database schema, and then outputs this information in various formats, including JSON and Markdown. This structured output can then be used with a generative AI model (like Gemini) to answer questions about the codebase.

The project is written in Python and uses a modular, handler-based approach to support different file types. The main script, `analyze.py`, walks through the source directory, identifies files based on their extension, and then uses the appropriate handler from the `parsers/` directory to extract data. The configuration is managed through a `config.yaml` file, allowing users to specify the source directory, output directory, and which file types to include.

## Building and Running

To use this tool, you first need to install the required Python packages:

```bash
pip install -r requirements.txt
```

Once the dependencies are installed, you can run the analysis with the following command:

```bash
python analyze.py
```

This will parse the files in the `src/` directory and generate output files in the `output/` directory.

To query the generated data with an AI model, you can use the `prompt.py` script:

```bash
python prompt.py "Your question about the codebase"
```

This will send the parsed data along with your question to the Gemini API and save the answer in `output/answer.md`.

**NOTE:** You will need to set up a `.env` file with your `API_KEY` for the `prompt.py` script to work.

## Development Conventions

The project follows a modular structure, with each file type having its own handler in the `parsers/` directory. This makes it easy to extend the tool to support new languages. The handlers are responsible for parsing the content of a file and returning a dictionary of extracted data.

The project uses `sqlglot` for SQL parsing, which is a powerful library that can handle various SQL dialects. The `graphviz` library is used to generate dependency graphs.

---

## Project Architecture Overview

The project has been refactored into a modular, provider-centric architecture to support advanced features and improve maintainability.

### Core Components:

*   **/modules/:** Contains the core logic of the application, broken down into the following modules:
    *   **config_loader.py:** Loads and validates the main `config.yaml`.
    *   **agent_logic.py:** Contains the logic for mapping file types to agents.
    *   **file_utils.py:** Provides utility functions for file hashing and caching.
    *   **/providers/:** The heart of the new architecture. It contains a `ProviderManager` and dedicated classes for each AI provider (Ollama, OpenAI, Gemini). Each provider class is responsible for:
        *   Managing its own API connection.
        *   Constructing provider-specific, optimized prompts.
        *   Executing prompts and handling responses.
        *   Implementing provider-specific caching strategies.
*   **analyze.py:** The main entry point for the application. It orchestrates the workflow by importing and calling functions from the various modules.

### Two-Step Enrichment Process:

The analysis process now follows a two-step enrichment strategy:
1.  **Initial Analysis:** A high-level analysis of the code is performed to get a general understanding of its purpose and structure.
2.  **Detailed RAG Tasks:** The output from the initial analysis is used as context for a series of more focused, detailed analysis tasks, as defined in the `config.yaml`. This allows for a more comprehensive and accurate analysis of the code.
