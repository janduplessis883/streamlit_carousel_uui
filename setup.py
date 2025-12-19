import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit-carousel-uui",
    version="0.1.4",
    author="Jan du Plessis",
    author_email="",
    description="A Streamlit component for displaying an Untitled UI styled carousel",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/janduplessis883/streamlit_carousel_uui",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "streamlit>=1.0.0",
    ],
)
