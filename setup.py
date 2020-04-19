from io import open
from setuptools import setup

with open('README.md') as read_me:
    long_description = read_me.read()

setup(
    name='create_eel_app',
    version='0.1.0',
    author='gr3atwh173',
    url='https://github.com/gr3atwh173/create_eel_app',
    packages=['app_templates'],
	scripts=['scripts/create_eel_app.py'],
    install_requires=['pyinstaller'],
    python_requires='>=3.5',
    description='To bootstrap a basic Eel app.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['eel', 'create_eel_app'],
)