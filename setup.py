import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PySide2-Material-Widgets",
    version="0.0.10",
    keywords="pyside2 material widgets",
    author="zhiyiYo",
    author_email="shokokawaii@outlook.com",
    description="A material design widgets library based on PySide2",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GPLv3",
    url="https://github.com/zhiyiYo/QMaterialWidgets/tree/master",
    packages=setuptools.find_packages(),
    install_requires=[
        "PySide2>=5.15.0",
        "PySide2-Frameless-Window",
        "darkdetect",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Documentation': 'https://qmaterialwidgets.readthedocs.io/',
        'Source Code': 'https://github.com/zhiyiYo/QMaterialWidgets/tree/master',
        'Bug Tracker': 'https://github.com/zhiyiYo/QMaterialWidgets/issues',
    }
)
