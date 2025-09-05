# 1. Create a Virtual Environment

Run the following command to create a virtual environment:
`python -m venv <env_name>`

# 2. Activate the Virtual Environment

On Windows:
`venv\Scripts\activate`

# 3. Install Packages in the Virtual Environment

Once the virtual environment is activated, use pip to install packages:
`pip install flask beautifulsoup4 requests`

# 4. Recreate the Environment:

Use pip freeze to generate a requirements.txt file:
`pip freeze > requirements.txt`
Others can recreate the environment using:
`pip install -r requirements.txt`
