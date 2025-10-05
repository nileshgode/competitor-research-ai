Follow the installation steps

# For Windows PowerShell, this will install uv in your system
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify installation
uv --version


# Initialize uv project with Python 3.11
uv init --python 3.11


# To create folder structure from CMD
1. mkdir src\agents src\graphs src\models src\tools src\llm src\api src\utils

2. mkdir data\inputs data\outputs
