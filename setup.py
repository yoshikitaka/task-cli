"""Setup configuration for task-cli"""
from setuptools import setup, find_packages

setup(
    name="task-cli",
    version="0.1.0",
    description="CLI ToDo management tool",
    author="yoshikitaka",
    author_email="yoshiki@example.com",
    python_requires=">=3.8",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "click>=8.1.0",
    ],
    entry_points={
        "console_scripts": [
            "task-cli=task_cli.cli:main",
        ],
    },
)
