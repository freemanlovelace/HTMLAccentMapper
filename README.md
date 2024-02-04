# HTMLAccentMapper
HTMLAccentMapper is a Python script designed to improve the usability of QWERTY keyboards by seamlessly integrating HTML accent encoding patterns. This tool simplifies the input of accented characters by recognizing and mapping HTML accent entities. Whether you're a multilingual writer, developer, or someone looking to enhance their keyboard experience, HTMLAccentMapper streamlines the process of accent input.
the script use the [pynut python library](https://pynput.readthedocs.io/en/latest/)

![test screenshot](/screenshot/mapperTest.gif)

## Install
To test the script on other plateform, launch the provided gui.py. Follow these steps:

1. Clone this repository
2. create a virtual environment
3. activate the virtual environment
4. Install requirements then Launch gui.py :  

```
python3 -m venv ./HTMLAccentMapperEnv
source ./HTMLAccentMapperEnv/bin/activate (on windows : HTMLAccentMapperEnv\Scripts\activate)
pip install -r requirements.txt
python3 gui.py (Use python instead of python3 on Windows)
```

You an build the app for your platform using pyInstaller : `pyinstaller gui.py`
  
## Usage

This script utilizes HTML entities to enable QWERTY (or other keyboard types) to input accents. Instead of using the **`&`** character to initialize the entity, it uses the **`;`** character.

<h4>Example</h4>

**`;eacute;`** will produce the following output: **`é`** .

Inserting a **`;`** character initializes a table (named key_tab in the script), and all subsequent characters will be added to the table. Inserting another **`;`** stops the gathering process and checks whether the content of key_tab is a valid HTML entity, replacing it with its corresponding accent.

If Space or Enter key is pressed, then key_tab is reinitialized.

<h4>Here are all supported entities :</h4>

<table>
    <tr>
        <th>Entity</th>
        <th>Corresponding Accent</th>
    </tr>
    <tr>
        <td>aacute</td>
        <td>á</td>
    </tr>
    <tr>
        <td>eacute</td>
        <td>é</td>
    </tr>
    <tr>
        <td>iacute</td>
        <td>í</td>
    </tr>
    <tr>
        <td>oacute</td>
        <td>ó</td>
    </tr>
    <tr>
        <td>uacute</td>
        <td>ú</td>
    </tr>
    <tr>
        <td>agrave</td>
        <td>à</td>
    </tr>
    <tr>
        <td>egrave</td>
        <td>è</td>
    </tr>
    <tr>
        <td>igrave</td>
        <td>ì</td>
    </tr>
    <tr>
        <td>ograve</td>
        <td>ò</td>
    </tr>
    <tr>
        <td>ugrave</td>
        <td>ù</td>
    </tr>
    <tr>
        <td>acirc</td>
        <td>â</td>
    </tr>
    <tr>
        <td>ecirc</td>
        <td>ê</td>
    </tr>
    <tr>
        <td>icirc</td>
        <td>î</td>
    </tr>
    <tr>
        <td>ocirc</td>
        <td>ô</td>
    </tr>
    <tr>
        <td>ucirc</td>
        <td>û</td>
    </tr>
    <tr>
        <td>atilde</td>
        <td>ã</td>
    </tr>
    <tr>
        <td>etilde</td>
        <td>ẽ</td>
    </tr>
    <tr>
        <td>itilde</td>
        <td>ĩ</td>
    </tr>
    <tr>
        <td>otilde</td>
        <td>õ</td>
    </tr>
    <tr>
        <td>utilde</td>
        <td>ũ</td>
    </tr>
    <tr>
        <td>auml</td>
        <td>ä</td>
    </tr>
    <tr>
        <td>euml</td>
        <td>ë</td>
    </tr>
    <tr>
        <td>iuml</td>
        <td>ï</td>
    </tr>
    <tr>
        <td>ouml</td>
        <td>ö</td>
    </tr>
    <tr>
        <td>uuml</td>
        <td>ü</td>
    </tr>
    <tr>
        <td>ccedil</td>
        <td>ç</td>
    </tr>
    <tr>
        <td>nbsp</td>
        <td>tabulation</td>
    </tr>
</table>

# Contributing
If you want to contribute open an issue then feel free to submit pull request

