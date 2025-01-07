from setuptools import setup, find_packages

setup(
    name="draqai",
    version="0.1.5",
    description="A powerful SDK for building AI assistants with RAG capabilities.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Draq",
    author_email="info@draq.ai",
    url="https://github.com/draqai/AI",
    packages=find_packages(),
    install_requires=[
        "openai",
        "anthropic",
        "groq",
        "langchain",
        "faiss-cpu",  # For vector storage
        "pydantic",   # For data validation
        "requests",   # For web tools
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "opai=opai.cli.main:main",
        ],
    },
)