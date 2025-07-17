# setup.py: Configuration for packaging the data-gen-tool as a Python package.
# This allows easy installation and distribution, e.g., via pip install -e .
# It defines metadata, dependencies, and entry points for CLI.

from setuptools import setup, find_packages

setup(
    name='data-gen-tool',  # Package name for pip installation.
    version='0.1.0',  # Initial version; increment as features are added.
    packages=find_packages(where='src'),  # Automatically find packages in src/.
    package_dir={'': 'src'},  # Map package root to src/ directory.
    install_requires=[  # Core dependencies required for the tool to run.
        'faker',
        'pandas',
        'numpy',
        'scipy',
        'sqlparse',
        'pyarrow',
        'click',
    ],
    entry_points={  # Define console scripts for easy CLI access.
        'console_scripts': [
            'data-gen = data_gen.cli:main',  # Maps 'data-gen' command to cli.main().
        ],
    },
    author='Your Name',  # Author metadata.
    description='Data generation tool for ETL and training',  # Short description.
)