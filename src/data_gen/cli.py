import argparse
from typing import Dict

from .core.generator import generate_data
from .inputs.ddl_parser import parse_ddl
from .inputs.schema_inference import infer_schema_from_sample
from .outputs.writers.csv_writer import CSVWriter
from .outputs.writers.delta_writer import DeltaWriter
from .outputs.writers.txt_writer import TXTWriter
from .utils.logging import setup_logging

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description='Data Generation CLI')
    parser.add_argument('--ddl-path', type=str, help='Path to DDL file')
    parser.add_argument('--sample-path', type=str, help='Path to sample CSV')
    parser.add_argument('--output-format', choices=['csv', 'delta', 'txt'], required=True)
    parser.add_argument('--row-count', type=int, default=100)
    parser.add_argument('--output-path', type=str, required=True)

    args = parser.parse_args()

    if args.ddl_path:
        with open(args.ddl_path, 'r') as f:
            ddl = f.read()
        schema = parse_ddl(ddl)
    elif args.sample_path:
        schema = infer_schema_from_sample(args.sample_path)
    else:
        raise ValueError("Provide either DDL or sample path")

    data = generate_data(schema, args.row_count)

    if args.output_format == 'csv':
        writer = CSVWriter()
    elif args.output_format == 'delta':
        writer = DeltaWriter()
    elif args.output_format == 'txt':
        writer = TXTWriter()

    writer.write(data, args.output_path)
    logger.info(f"Generated {args.row_count} rows to {args.output_path}")

if __name__ == '__main__':
    main()