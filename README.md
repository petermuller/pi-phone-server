# pi-phone-server

Server for GPIO Controller phone applications

## Directions

1. Copy the Python files (.py) to your Raspberry Pi
2. Ensure your Raspberry Pi distro is up to date (# yum/apt-get upgrade)
3. As root, run the command "python PiServer.py"
4. Use `curl` commands to test the server until the phone applications are updated to use the new implementation

## New to Version 2

* Server now implements a Flask server instead of a raw socket connection
    * This breaks the related phone applications until they are updated with the new interface
* Networking and Pi functionality are separated for better modularity
* Removing PWM functionality to favor logical HIGH and LOW outputs
