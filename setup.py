from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="certwiz",
    version="0.1.0",
    author="Manbehindthemadness",
    author_email="manbehindthemadness@gmail.com",
    description="Quickly add SSL functionality into a microservice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/manbehindthemadness/certwiz",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pyOpenSSL",
        "build-settings",
    ],
)
