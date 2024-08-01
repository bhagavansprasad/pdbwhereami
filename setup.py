from setuptools import setup

setup(
    name="whereami",
    version="0.1.0",
    py_modules=["whereami"],
    install_requires=[
        "datetime",
        "json",
        "sys",
        "inspect",
    ],
    author="Bhagavan",
    author_email="bhagavansprasad@gmail.com",
    description="Helps ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)