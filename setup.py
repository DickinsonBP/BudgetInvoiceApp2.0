from setuptools import setup

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name='BudgetInvoiceApp',
    packages=['BI'],
    install_requires=install_requires
    )