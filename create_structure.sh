#!/bin/bash

# Create directories
mkdir -p src/data_gen/core
mkdir -p src/data_gen/inputs
mkdir -p src/data_gen/outputs/writers
mkdir -p src/data_gen/utils
mkdir -p api/routes
mkdir -p web/components/static
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p docs
mkdir -p examples
mkdir -p config

# Touch files (create empty placeholders)
touch src/data_gen/__init__.py
touch src/data_gen/core/__init__.py
touch src/data_gen/core/generator.py
touch src/data_gen/core/types.py
touch src/data_gen/inputs/__init__.py
touch src/data_gen/inputs/schema_inference.py
touch src/data_gen/inputs/ddl_parser.py
touch src/data_gen/outputs/__init__.py
touch src/data_gen/outputs/writers/__init__.py
touch src/data_gen/outputs/writers/csv_writer.py
touch src/data_gen/outputs/writers/delta_writer.py
touch src/data_gen/outputs/writers/txt_writer.py
touch src/data_gen/outputs/writers/base_writer.py
touch src/data_gen/outputs/format_utils.py
touch src/data_gen/utils/__init__.py
touch src/data_gen/utils/logging.py
touch src/data_gen/utils/validators.py
touch src/data_gen/cli.py
touch api/__init__.py
touch api/app.py
touch api/routes/__init__.py
touch api/routes/generate.py
touch api/routes/schema.py
touch api/models.py
touch web/app.py
touch web/components/upload.py
touch web/components/ddl_input.py
touch tests/__init__.py
touch tests/unit/test_generator.py
touch tests/unit/test_schema_inference.py
touch tests/unit/test_writers.py
touch tests/integration/test_end_to_end.py
touch docs/index.md
touch docs/api.md
touch examples/sample_ddl.sql
touch examples/sample_data.csv
touch requirements.txt
touch setup.py
touch README.md
touch config/default_config.yaml

echo "Folder structure created!"