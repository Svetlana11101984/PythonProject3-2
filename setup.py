from setuptools import find_packages, setup

setup(
    name="financial-tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.5",
        "pytest>=6.2.5",
        "pytest-cov>=2.12.1"
    ],
    include_package_data=True,
    zip_safe=False
)
