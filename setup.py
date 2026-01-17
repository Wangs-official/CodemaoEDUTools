from setuptools import setup, find_packages
import re
import os

with open("CodemaoEDUTools/__init__.py", "r", encoding="utf-8") as f:
    version = re.search(r'__version__ = ["\']([^"\']+)["\']', f.read()).group(1)

setup(
    name="CodemaoEDUTools",
    version=version,
    author="WangZixu",
    author_email="wangsofficial@outlook.com",
    description="为编程猫社区的“老师”们提供更便捷的API调用方案，且用且珍惜",
    long_description=open("README.md", encoding="utf-8").read()
    if os.path.exists("README.md")
    else "",
    long_description_content_type="text/markdown",
    url="https://github.com/Wangs-official/CodemaoEDUTools",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.25.1",
        "fake-useragent>=0.1.11",
        "pandas>=1.3.0",
        "openpyxl>=3.0.9",
        "coloredlogs>=15.0",
    ],
    entry_points={
        "console_scripts": [
            "cet=CodemaoEDUTools.__main__:main",
        ],
    },
)
