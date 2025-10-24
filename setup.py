from setuptools import setup, find_packages

setup(
    name="todo-cli",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "todo=todo.main:main",
        ],
    },
)
