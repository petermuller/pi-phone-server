# pi-phone-server

Server for GPIO Controller phone applications

## Directions

1. Copy the Python files (.py) to your Raspberry Pi
2. Ensure your Raspberry Pi distro is up to date (# yum/apt-get upgrade)
3. Install python3, python3-flask, and flask-cors
4. As root, run the command "python PiServer.py"
5. Use `curl` commands to test the server until the phone applications are updated to use the new implementation. Example: `curl -X GET http://localhost:5000/get-pin-value/7` or `curl -X POST http://localhost:5000/set-pin-value/7/1`

## New to Version 2

* Server now implements a Flask server instead of a raw socket connection
    * This breaks the related phone applications until they are updated with the new interface
* Networking and Pi functionality are separated for better modularity
* Removing PWM functionality to favor logical HIGH and LOW outputs
