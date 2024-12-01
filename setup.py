from setuptools import setup


setup(
    name="goyda-pre-commit-hook",
    version="0.6.2",
    py_modules=["goyda"],
    entry_points={
        "console_scripts": [
            "goyda-hook=goyda:main",
        ],
    },
)
