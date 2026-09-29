"""
setup.py — Package installation file for Plant Care AI System.
"""

from setuptools import setup, find_packages

setup(
    name="plant_care_ai",
    version="1.0.0",
    description="Plant Care AI Detection System using Transfer Learning and Flask",
    author="Antigravity Team",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "tensorflow>=2.13.0",
        "flask>=2.3.3",
        "pillow>=10.0.1",
        "numpy>=1.24.3",
        "pandas>=2.0.3",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.2",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "plant-care=main:main",
        ],
    },
)
