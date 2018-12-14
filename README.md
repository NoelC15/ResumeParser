# ResumeParser

Resume Parser converts PDFs into text files and then processes it to extract key fields like: Name, Email, Phone number, and GPA. This information will be displayed in a GUI with editable fields which will then export it into an excel file.

## Installation
```bash
pip install nltk
pip install pandas
```

If punkt error occurs add nltk.download('punkt') to Resume.py, this should resolve error.
 
Before you run code changne directory paths to correct paths where text and excel files are located.
There are two places where directory path must be changed, line 17 and line 73 in Resume.py.
