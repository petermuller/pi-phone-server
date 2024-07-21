import click
import uvicorn

from pi_phone_server.server import app


@click.command()
@click.option("-p", "--port", type=click.INT, default=8000, required=False)
def run(port: int):
    print(f"Running with port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    run()
