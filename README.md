# Create Eel App

create_eel_app provides basic template and managing utilities for an Eel app.  
  
> Eel is a little Python library for making simple Electron-like HTML/JS GUI apps.

Check out Eel here: https://github.com/samuelhwilliams/Eel

## Usage

### Create an Eel app

```
$ create_eel_app.py create my_awesome_eel_app
```
This creates a directory with the name 	```my_awesome_eel_app``` in the current working directory and initializes a git repository as well.

### Launch the app
In the directory of the newly created app
```
$ create_eel_app.py launch
```

### Package the app

To package the app, simply run

```
$ create_eel_app.py publish
```

This will package your file into a single file using ```pyinstaller``` and put the resulting file in ```dist/``` 
>To change publishing settings, see ```app_config.json```

## Installation
Install it from pypi using 	```pip```
```
$ pip install create-eel-app
```
or from source
```
$ git clone https://github.com/gr3atwh173/create-eel-app
$ cd create-eel-app
$ python setup.py install
```

## Todo
* [x] Implement basic template
* [x] Implement launch
* [x] Implement publish
* [ ] More templates
* [ ] hot reloading 🔥