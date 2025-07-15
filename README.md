# Data Gen Tool

[![GitHub license](https://img.shields.io/github/license/yourusername/data-gen-tool)](https://github.com/yourusername/data-gen-tool/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/data-gen-tool)](https://github.com/yourusername/data-gen-tool/issues)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/data-gen-tool)](https://github.com/yourusername/data-gen-tool/stargazers)

A versatile, consumer-facing data generation tool designed for data engineers and trainers. Generate synthetic test data quickly for ETL workloads, training programs, or prototyping—based on inferred schemas from sample datasets or provided SQL DDL. Supports multiple output formats like CSV, Delta tables (via PySpark), TXT, and more.

This project is built iteratively with a modular structure to support future expansions: a core Python library for data generation, an API (using FastAPI), and a web app (using Streamlit) for user-friendly interactions like drag-and-drop schema inference.

## Features

- **Schema Inference**: Drag-and-drop sample datasets (e.g., CSV, Parquet) to automatically infer data schemas, types, and distributions.
- **DDL Parsing**: Provide SQL DDL strings to extract table schemas and generate compliant data.
- **Data Generation**: Create realistic synthetic data using libraries like Faker, with customizable distributions, constraints, and row counts.
- **Output Formats**:
  - CSV
  - Delta tables (scalable via PySpark for large datasets)
  - TXT (plain text)
  - Extensible to other formats (e.g., JSON, Parquet)
- **Scalability**: Handles small in-memory generation (Pandas) or large-scale distributed outputs (PySpark).
- **CLI for Testing**: Initial command-line interface for quick prototyping.
- **Future Plans**:
  - Web App: Streamlit-based UI for drag-and-drop and DDL inputs.
  - API: FastAPI endpoints for programmatic access (e.g., generate data via POST requests).
- **Use Cases**:
  - Test ETL pipelines without real data.
  - Generate datasets for data engineering training modules.
  - Prototype schemas for Spark/SQL workloads.

## Installation

### Prerequisites
- Python 3.8+
- Optional: Apache Spark (for Delta table outputs; install via `pyspark` and `delta-spark`)

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/data-gen-tool.git
   cd data-gen-tool
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   Key libraries include: `pandas`, `faker`, `pyspark`, `delta-spark`, `fastapi`, `streamlit`, `sqlparse` (for DDL parsing).

3. (Optional) For Spark/Delta support:
   - Ensure Spark is installed and configured (e.g., `SPARK_HOME` env var).
   - Test with: `spark-submit --packages io.delta:delta-spark_2.12:3.2.0 ...`

## Usage

### Via CLI (Early Stage)
Generate data from a sample DDL:
```
python src/data_gen/cli.py --ddl-path examples/sample_ddl.sql --output-format csv --row-count 100 --output-path output/generated.csv
```

Infer schema from a sample CSV and generate Delta table:
```
python src/data_gen/cli.py --sample-path examples/sample_data.csv --output-format delta --row-count 1000 --output-path output/generated_delta
```

### Future Web App
Run the Streamlit app:
```
streamlit run web/app.py
```
- Upload a sample file or paste DDL.
- Configure generation params (e.g., distributions via UI).
- Download generated data in chosen format.

### Future API
Start the FastAPI server:
```
uvicorn api.app:app --reload
```
- POST to `/generate` with schema/DDL payload.
- Example curl:
  ```
  curl -X POST "http://localhost:8000/generate" -H "Content-Type: application/json" -d '{"ddl": "CREATE TABLE users (id INT, name VARCHAR(255))", "row_count": 50, "format": "csv"}'
  ```

## Examples

### Sample DDL Input
From `examples/sample_ddl.sql`:
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    salary DECIMAL(10, 2),
    hire_date DATE
);
```
Generated data might include rows like:
- id: 1, name: "John Doe", age: 28, salary: 55000.00, hire_date: 2023-01-15

### Schema Inference from CSV
Upload `examples/sample_data.csv` with columns like `product_id, name, price`. The tool infers types (int, str, float) and generates similar data.

## Project Structure
```
data-gen-tool/
├── src/                # Core library (reusable Python package)
│   └── data_gen/
│       ├── core/       # Generation logic (generator.py, types.py)
│       ├── inputs/     # Schema inference and DDL parsing
│       ├── outputs/    # Writers for CSV, Delta, etc.
│       ├── utils/      # Logging, validators
│       └── cli.py      # Command-line entrypoint
├── api/                # FastAPI app and routes
├── web/                # Streamlit web app
├── tests/              # Unit and integration tests
├── docs/               # Documentation
├── examples/           # Sample DDL and datasets
├── config/             # Default configs (e.g., YAML for params)
├── requirements.txt
├── setup.py            # For packaging
└── README.md
```

## Contributing
We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
- Report issues or suggest features via GitHub Issues.
- Submit PRs for bug fixes, new writers, or enhanced distributions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with ❤️ by data engineers for data engineers. Feedback? Open an issue!
