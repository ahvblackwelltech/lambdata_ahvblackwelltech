import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_ahvblackwelltech",
    version="0.0.1",
    author="Ahvi Blackwell",
    author_email="ahvi-blackwell@lambdastudents.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ahvblackwelltech/lambdata_ahvblackwelltech/blob/master/my_lambda/helper_utility.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
