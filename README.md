# pi-phone-server

Server for GPIO Controller phone applications

## Directions

1. Clone this repository into your Raspberry Pi
2. Create a virtualenv environment and install the dependencies
3. Start the server
4. Have fun!

```shell
# Installation on Pi
python -m venv .venv
source .venv/bin/activate  # or on Windows: .venv/Scripts/Activate.ps1
pip install -e '.[raspi]'
run-server  # by default runs on port 8000, use '-p PORTNUM' to change to another port
```

If you want to install dependencies for testing, you can use the following
```shell
pip install -e '.[test]'
# or on the Pi itself:
pip install -e '.[raspi,test]'

# running tests:
coverage run
coverage xml  # JUnit reporting
coverage html  # HTML reporting
```

## Version 3
This is the third rewrite of this server, but this should be the easiest to interact with.
Main features for this version are:
* FastAPI usage instead of Flask
  * This allows for OpenAPI clients to interact with the server
* Cleaner code
