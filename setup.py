from setuptools import setup

with open(r"README.md", "r", encoding='utf-8') as arq:
    readme = arq.read()

setup(name='Wave',
    version='1.0.0',
    license='MIT License',
    author='Lucas Lourenço',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='dev.lucaslourenco@gmail.com',
    keywords='wave build docx treatdata xlsx to word',
    description=u'Wave - Workflow Automation and Versatile Engine',
    packages=['PreRequisitesWave','To','DataHandler','Builder','Transmitter'],
    install_requires=['python-docx','openpyxl','pandas'],)