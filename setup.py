from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='TestowanieAutomatyczne_Projekt_II',
    version='2.0.0',
    description='Projekt II z przedmiotu Testowanie automatyczne. Projekt uproszczonej aplikacji w sklepie internetowym'
                'z obsługą kilentów, zamówień i przedmiotów na sprzedaż',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mstapaj/TestowanieAutomatyczne_Projekt_II',
    author='Mateusz Stapaj',
    author_email='mtxstapaj@gmail.com',
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4',
    install_requires=['coverage',
                      'assertpy',
                      'nose2',
                      'parametrized',
                      'setuptools',
                      'pytest'],
)
