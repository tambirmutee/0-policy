from setuptools import setup, find_packages

setup(
    name="0-policy",
    version="1.0.0",
    description="A CLI tool for scanning and analyzing Content-Security-Policy (CSP) headers",
    long_description="0-Policy is a terminal-based security analysis tool that fetches and analyzes CSP headers for misconfigurations, risky patterns, and bypassable policies.",
    long_description_content_type="text/markdown",
    author="tambirmutee",
    author_email="mustafayos06@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={
        "console_scripts": [
            "0-policy=zeropolicy.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Environment :: Console"
    ],
    python_requires='>=3.7',
)
