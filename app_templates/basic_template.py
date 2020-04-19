Files = {}

Files["app_config.json"] = \
"""
{
	"web_folder": "frontend",
	"index_page": "index.html",
	"mode": "chrome",
	"window_size": [600, 300],
	"entry": "app.py",
	"excluded_modules": [],
	"build_dir": "/dist"
}
"""

Files[".gitignore"] = \
"""
.pyc
dist
"""

Files["app.py"] = \
"""
from json import loads

import eel

# load the config file
config = {}
with open("app_config.json", "r") as f:
	config = loads(f.read())

# Set web files folder
eel.init(config["web_folder"])

# Expose this function to Javascript
@eel.expose                         
def py_works():
    return "From Py: It works!"

# Call a Javascript function
eel.js_works()(print)

# start the app
eel.start(config["index_page"], size=config["window_size"], mode=config["mode"])
"""

Files["frontend/"] = None
Files["frontend/img/"] = None

Files["frontend/index.html"] = \
"""
<!DOCTYPE html>
<html>
	<head>
		<title>Eel App</title>
		
        <script type="text/javascript" src="/eel.js"></script>
        <script type="text/javascript" src="js/index.js"></script>
		<link rel="stylesheet" href="css/styles.css">
	</head>

	<body onload="bodyLoaded()">
		<h1>Welcome to Eel!</h1>
		<span id="success_msg">It doesn't work :(</span>
	</body>
</html>
"""

Files["frontend/js/index.js"] = \
"""
eel.expose(js_works);               // Expose this function to Python
function js_works() {
	return "From JS: It works!";
}

function bodyLoaded() {
	var sm = document.getElementById("success_msg");
  	eel.py_works()((msg) => {
		sm.innerHTML = msg 
	});  // Call a Python function
}
"""

Files["frontend/css/styles.css"] = \
"""
body {
	height: 100vh;
	width: 100vw;
	font-family: sans-serif;
	text-align: center;
}

span {
	font-size: x-large;
	font-weight: bold;
}
"""
