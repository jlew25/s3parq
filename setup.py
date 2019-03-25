from setuptools import setup, find_packages
from os import path

package_name = "s3parq"
package_version = "0.0.2"
description = "Write and read/query s3 parquet data using Athena/Spectrum/Hive style partitioning."
cur_directory = path.abspath(path.dirname(__file__))
with open(path.join(cur_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Integrichain Innovation Team",
    author_email="engineering@integrichain.com",
    url="https://github.com/IntegriChain1/s3parq",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
        ],
    packages= find_packages(exclude=("tests",)),
    include_package_data=True,
    tests_require = ["dfmock==0.0.14","moto"],
    install_requires=["pandas","pyarrow","boto3","s3fs"]
    )
