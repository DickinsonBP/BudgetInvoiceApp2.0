# BudgetInvoiceApp2.0
Project to automate the generation of budgets and invoices

## Requirements

* Python 3
* Pipenv `pip install pipenv`

### Command to generate .gitignore
```
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
```

### Command to unit test
```
python3 -m unittest discover
```

### Use pipenv to package dependencies
#### Generate file
```
pipenv install --dev pycodestyle
```
##### If when executing it gives an error, use which pipenv to see where is installed and use that path
#### Edit Pipfile generated
```
[scripts]
lint = "pycodestyle folder1 folder2 ..."
```
#### Run pipenv
```
pipenv run lint
```

Usar pyside.
pyside-uic convierte un archivo ui a .py
C:\Python311\Scripts\pyside6-uic.exe .\pyside_test.ui -o "pyside.py" -x