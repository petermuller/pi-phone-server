import pytest
import requests

from xprocess import ProcessStarter

from pi_phone_server.model.controller.pin import VALID_PINS, PinMode, Voltage

TEST_PORT = 9999
LOCAL_URL = f"http://localhost:{TEST_PORT}"
HEADERS = {
    "Content-Type": "application/json"
}


@pytest.fixture(scope="module", autouse=True)
def server_session(xprocess):
    class PiTestServerStarter(ProcessStarter):
        args = [
            "run-server",
            "-p",
            str(TEST_PORT)
        ]

        def startup_check(self):
            try:
                req = requests.get(LOCAL_URL + "/health", headers=HEADERS)
                if req.status_code == 200 and req.json().get("status", False) == "ok":
                    return True
            except Exception as e:
                print("Trying health check - exception: " + str(e))
                pass
            return False

    xprocess.ensure("pi-test-server", PiTestServerStarter)

    session = requests.session()
    yield session

    session.close()
    xprocess.getinfo("pi-test-server").terminate()


class TestWalkthrough:

    @staticmethod
    def set_pin_mode(pin_id, mode, sess):
        resp = sess.post(f"{LOCAL_URL}/v1/{pin_id}/mode",
                         headers=HEADERS,
                         json={
                             "mode": mode
                         })
        body = resp.json()
        assert resp.status_code == 200
        assert body["mode"] == mode

    @staticmethod
    def get_pin_mode(pin_id, sess):
        resp = sess.get(f"{LOCAL_URL}/v1/{pin_id}/mode",
                        headers=HEADERS)
        assert resp.status_code == 200
        body = resp.json()
        return body

    @staticmethod
    def set_pin_voltage(pin_id, voltage, sess, expected_status=200):
        resp = sess.post(f"{LOCAL_URL}/v1/{pin_id}/voltage",
                         headers=HEADERS,
                         json={
                             "voltage": voltage
                         })
        assert resp.status_code == expected_status
        if expected_status == 200:
            body = resp.json()
            assert body["voltage"] == voltage
        else:
            assert "Cannot set voltage" in resp.content.decode()

    @staticmethod
    def get_pin_voltage(pin_id, sess):
        resp = sess.get(f"{LOCAL_URL}/v1/{pin_id}/voltage",
                        headers=HEADERS)
        assert resp.status_code == 200
        body = resp.json()
        return body

    def test_get_all_pins(self, server_session):
        for pin_id in VALID_PINS:
            # Get summary
            resp = server_session.get(f"{LOCAL_URL}/v1/{pin_id}", headers=HEADERS)
            resp_body = resp.json()
            assert resp_body["pin_id"] == pin_id
            assert resp_body["mode"] == PinMode.INPUT
            # Get input values. Cannot guarantee values so not checking them.
            self.get_pin_voltage(pin_id, server_session)

    def test_get_invalid_pin(self, server_session):
        pin_id = 1  # an invalid pin ID
        for uri in [
            f"{LOCAL_URL}/v1/{pin_id}",
            f"{LOCAL_URL}/v1/{pin_id}/mode",
            f"{LOCAL_URL}/v1/{pin_id}/voltage",
        ]:
            resp = server_session.get(uri, headers=HEADERS)
            assert resp.status_code == 400
            assert "is not valid" in resp.content.decode()

    def test_set_output_pins(self, server_session):
        for pin_id in VALID_PINS:
            # Set pin to output mode
            self.set_pin_mode(pin_id, PinMode.OUTPUT, server_session)

            # Validate that the mode persists on the board
            resp_body = self.get_pin_mode(pin_id, server_session)
            assert resp_body["mode"] == PinMode.OUTPUT

            # Explicitly set pin to low output voltage
            self.set_pin_voltage(pin_id, Voltage.LOW, server_session)

            # Validate that the board keeps the low value
            resp_body = self.get_pin_voltage(pin_id, server_session)
            assert resp_body["voltage"] == Voltage.LOW

            # Set pin to high voltage
            self.set_pin_voltage(pin_id, Voltage.HIGH, server_session)

            # Validate that the board keeps the low value
            resp_body = self.get_pin_voltage(pin_id, server_session)
            assert resp_body["voltage"] == Voltage.HIGH

    def test_set_voltage_on_input_pin(self, server_session):
        pin_id = 7  # valid pin ID
        self.set_pin_mode(pin_id, PinMode.INPUT, server_session)
        # expect a 400 when setting voltage on an input pin
        self.set_pin_voltage(pin_id, Voltage.HIGH, server_session, 400)
