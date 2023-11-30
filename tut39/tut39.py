'''
    TODO: Virtual Environment in Python | Python Tutorial - Day #43 
    * sudo apt update
    * sudo apt install python3-venv
    ? Create a virtual environment
        python3 -m venv myenv_custom_name
    ? Activate the virtual environment (Linux/macOS)
        source myenv/bin/activate
    ? Activate the virtual environment (Windows)
        myenv\Scripts\activate.bat
    ? Install particular version
        pip install pandas==1.4.4
    ? Output the list of installed packages and their versions to a file
        pip freeze > requirements.txt
    ? Install the packages listed in the requirements.txt file
        pip install -r requirements.txt
    * pipx install xyz
'''


import pandas as pd

print(pd.__version__)
