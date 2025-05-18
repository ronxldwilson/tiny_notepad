from setuptools import setup, find_packages

setup(
    name="tiny_notepad",
    version="0.1.2",
    author="Ronald Wilson",
    description="A minimal notepad with Ollama integration",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ronxldwilson/tiny_notepad",  # optional
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'tiny_notepad = tiny_notepad.main:main',  
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
