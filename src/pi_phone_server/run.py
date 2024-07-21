import uvicorn

from pi_phone_server.server import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
