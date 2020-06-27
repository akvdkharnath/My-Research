import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Orchestrator_A5", 
    version="0.0.1",
    author="Harnath Atmakuri",
    author_email="akvdkharnath@gmail.com",
    description="This package is mainly user to intigrate(automate) orchestrator with python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.6.5',
    keywords = ""
)