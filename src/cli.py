# cli.py: Command-line interface (CLI) entry point for the data generation tool.
# This script uses Click to parse arguments and orchestrate data generation.
# It integrates parsers, generators, and writers for end-to-end execution.
# Usage: python src/cli.py [options]

import click
from data_gen.parsers import infer_from_ddl, infer_from_sample
from data_gen.generators import generate_rows
from data_gen.writers import get_writer

@click.command()
@click.option('--ddl', default=None, help='SQL DDL string for schema inference.')  # Option for DDL input.
@click.option('--sample', default=None, help='Path to sample file for schema inference.')  # Option for sample file.
@click.option('--num-rows', default=100, help='Number of rows to generate.')  # Number of rows to generate.
@click.option('--format', default='csv', help='Output format (csv, delta, txt).')  # Output format selection.
@click.option('--output', default='output', help='Output file path (without extension).')  # Output path.
def main(ddl, sample, num_rows, format, output):
    """
    Main CLI function to generate data based on user inputs.

    This function infers the schema, generates rows, and writes to the specified format.

    Parameters:
    - ddl (str): SQL DDL string (optional).
    - sample (str): Path to sample file (optional).
    - num_rows (int): Number of rows to generate.
    - format (str): Output format.
    - output (str): Base path for output file.

    Raises:
    - click.UsageError: If neither DDL nor sample is provided.
    """
    # Infer schema from DDL if provided.
    if ddl:
        schema = infer_from_ddl(ddl)
    # Alternatively, infer from sample file.
    elif sample:
        schema = infer_from_sample(sample)
    else:
        raise click.UsageError("Provide either --ddl or --sample.")

    # Generate data rows as a list (materialize generator for writing).
    data = list(generate_rows(num_rows, schema))
    # Get the appropriate writer based on format.
    writer = get_writer(format)
    # Write data to file with format extension.
    writer.write(data, f"{output}.{format}")

    # Output success message.
    click.echo(f"Generated {num_rows} rows to {output}.{format}")

if __name__ == '__main__':
    main()  # Run the CLI when script is executed directly.