from setuptools import setup


setup(
    name="goyda-pre-commit-hook",
    version="0.1",
    py_modules=["goyda"],
    entry_points={
        "console_scripts": [
            "goyda-hook=goyda:main",
        ],
    },
)
