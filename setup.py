from setuptools import setup, find_packages

setup(
    name="Supply Chain Data tower",                # Project name
    version="0.1.0",                  # Version number
    description="Supply Chain Data tower project",
    author="Bikesh Kumar Maharana",
    author_email="maharanabikesh47@gmail.com",
    packages=find_packages(),         # Automatically find all packages
    install_requires=[                # Dependencies
        "requests",
        "numpy"
    ],
    entry_points={                    # Optional: command-line scripts
        "console_scripts": [
            "mytool=my_project.cli:main",
        ],
    },
)
