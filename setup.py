from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    description="A Python boilerplate project",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
