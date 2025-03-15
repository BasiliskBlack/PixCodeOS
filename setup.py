# PixCodeOS - Developed by [Your Name] with AI as Co-Developer
# AI tools (e.g., Grok) generated code based on my Sator Square equations and vision.

from setuptools import setup, find_packages

setup(
    name="PixCodeOS",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,  # Include all data files (e.g., src/, tests/)
    install_requires=[
        "numpy",
        "PyQt5",
        "matplotlib",
        "docker",
        "scikit-learn",
        "psutil"
    ],
    data_files=[
        ('/usr/local/bin', ['src/gui/ryoiki_tenkai_gui.py']),  # Example entry point
        ('/etc/pixcodeos', ['README.md', 'requirements.txt']),  # Configuration files
        ('/usr/local/share/pixcodeos', ['src/*', 'tests/*', 'docs/*'])  # All source and test files
    ],
    description="An AI-driven OS with Sator Square geometry and Jujutsu Kaisen-inspired features",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/PixCodeOS",
    author="[Your Name]",
    author_email="[Your Email]",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "pixcodeos=src.gui.ryoiki_tenkai_gui.py:main",  # Entry point for launching GUI
        ],
    },
)
