# HTMLAccentMapper
HTMLAccentMapper is a Python script designed to improve the usability of QWERTY keyboards by seamlessly integrating HTML accent encoding patterns. This tool simplifies the input of accented characters by recognizing and mapping HTML accent entities. Whether you're a multilingual writer, developer, or someone looking to enhance their keyboard experience, HTMLAccentMapper streamlines the process of accent input.
the script use the [pynut python library](https://pynput.readthedocs.io/en/latest/)

## Install
To test the script on other plateform, launch the provided gui.py. Follow these steps:

Clone this repository.

Create a virtual environment: `python3 -m venv .`
  
Install requirements: `pip install -r requirements.txt`
  
Launch gui.py: `python3 gui.py` (Use python instead of python3 on Windows)

You an build the app for your platform using pyInstaller : `pyinstaller gui.py`
  
## Usage

This script utilizes HTML entities to enable QWERTY (or other keyboard types) to input accents. Instead of using the **`&`** character to initialize the entity, it uses the **`;`** character.

<b>Example</b>

**`;eacute;`** will produce the following output: **`é`** .

Inserting a **`;`** character initializes a table (named key_tab in the script), and all subsequent characters will be added to the table. Inserting another **`;`** stops the gathering process and checks whether the content of key_tab is a valid HTML entity, replacing it with its corresponding accent.

If Space or Enter key is pressed, then key_tab is reinitialized.

# Contributing
Open an Issue then feel free to submit pull request

