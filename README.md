# Data Generation Tool

A Python-based tool for generating test data for ETL workloads and data engineering training. Supports schema inference from DDL or sample files, data generation with real-world heuristics, and output to formats like CSV, Delta, TXT, etc.

## Features
- Infer schema from SQL DDL or sample datasets (CSV, etc.).
- Generate data with customizable distributions (e.g., normal, uniform).
- Output to multiple formats.
- CLI for quick usage.
- Modular design for future web UI and API.

## Installation
```bash
pip install -r requirements.txt
pip install -e .
```

## Usage
CLI example:
```bash
python src/cli.py --ddl "CREATE TABLE test (id INT, name VARCHAR)" --num-rows 100 --format csv --output output.csv
```

## Future Enhancements
- More file formats (input/output).
- Advanced heuristics for realistic data.
- Web UI with drag-and-drop.
- API endpoints.

## Project Structure
The repository is structured for modularity, separating core logic, CLI, API, web UI, tests, and documentation. This design supports easy extension to a consumer-facing web app and API while compartmentalizing modules.

```
data-gen-tool/
├── .gitignore            # Git ignore file for common exclusions (e.g., __pycache__, venv)
├── README.md             # This file: Project overview, usage, and structure
├── requirements.txt      # Core dependencies (e.g., faker, pandas, numpy)
├── requirements-dev.txt  # Development dependencies (e.g., pytest, black)
├── setup.py              # Setup script for packaging the tool as a pip-installable package
├── src/                  # Source code directory for the core library and CLI
│   ├── cli.py            # Command-line interface entry point using Click
│   └── data_gen/         # Main package with core modules
│       ├── __init__.py   # Package initializer (empty)
│       ├── generators.py # Data generation logic (e.g., using Faker, NumPy for distributions)
│       ├── parsers.py    # Schema inference from DDL or sample files
│       ├── utils.py      # Utility functions (e.g., logging)
│       └── writers.py    # Output writers for formats like CSV, Delta, TXT
├── api/                  # API layer (FastAPI stub for future backend)
│   ├── __init__.py       # Package initializer (empty)
│   └── app.py            # FastAPI app with endpoints for data generation
├── web/                  # Web UI layer (Streamlit stub for user-facing app)
│   └── app.py            # Streamlit app for drag-and-drop schema inference and generation
├── tests/                # Unit and integration tests
│   ├── __init__.py       # Package initializer (empty)
│   ├── test_generators.py# Tests for generators module
│   ├── test_parsers.py   # Tests for parsers module
│   └── test_writers.py   # Tests for writers module
└── docs/                 # Documentation directory (e.g., for Sphinx or MkDocs)
    └── index.rst         # Placeholder for main documentation index
```

## Code Documentation
All code files include comprehensive comments and docstrings for better understanding and maintainability.

## Contributing
Run tests: `pytest tests/`.
Format code: `black .`.