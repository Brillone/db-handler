from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='db-handler',
    version='0.0.1',
    packages=['db_handler'],
    url='https://realmatch.visualstudio.com/Algo%20-%20Pandologic/_git/db-handler',
    license='MIT License',
    author='Pandologic',
    author_email='ebrill@pandologic.com',
    description='Python integration with multiple databases types',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: MIT License",
            "Operating System :: OS Independent",
        ],
    python_requires='>=3.6'
)
