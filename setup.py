from setuptools import setup, find_packages

setup(
    name='data-gen-tool',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'faker',
        'pandas',
        'sqlparse',
        'pyspark',
        'delta-spark',
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'data-gen-cli = data_gen.cli:main',
        ],
    },
    description='A tool for generating synthetic test data for ETL and training.',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
)