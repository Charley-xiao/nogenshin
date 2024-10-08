from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nogenshin",
    version="0.1.1",
    author="Charley Xiao",
    author_email="charleyxiao057@gmail.com",
    description="Genshin, but no Genshin.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Charley-xiao/nogenshin",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # No dependencies
    ],
)
