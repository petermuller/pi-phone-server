# pi-phone-server

Server for GPIO Controller phone applications

## Directions

1. Clone this repository into your Raspberry Pi
2. Create a virtualenv environment and install the dependencies
3. As root (because of Pin permissions), start the server
4. Have fun!

## Version 3
This is the third rewrite of this server, but this should be the easiest to interact with.
Main features for this version are:
* FastAPI usage instead of Flask
  * This allows for OpenAPI clients to interact with the server
* Cleaner code
