import json
from typing import Any, Dict

from flask import Flask, jsonify, request
from scrapli.driver.core import IOSXRDriver


def get_received_routes(host: str, username: str, password: str, peer_ip: str) -> Dict[str, Any]:
    """Fetch BGP received routes for a given peer from a Cisco IOS XR device.

    Parameters
    ----------
    host: str
        IP address or hostname of the IOS XR device.
    username: str
        Username for SSH authentication.
    password: str
        Password for SSH authentication.
    peer_ip: str
        IP address of the BGP neighbor whose received routes are requested.

    Returns
    -------
    dict
        Parsed JSON data of the received routes.
    """
    with IOSXRDriver(
        host=host,
        auth_username=username,
        auth_password=password,
        auth_strict_key=False,
    ) as conn:
        cmd = f"show bgp ipv4 unicast neighbors {peer_ip} received-routes | json"
        response = conn.send_command(cmd)
        return json.loads(response.result)


app = Flask(__name__)


@app.route("/received_routes")
def received_routes() -> Any:
    """HTTP endpoint returning received routes for a BGP peer.

    Expects query parameters `host`, `username`, `password`, and `peer`.
    """
    host = request.args.get("host", "")
    username = request.args.get("username", "")
    password = request.args.get("password", "")
    peer = request.args.get("peer", "")

    if not all([host, username, password, peer]):
        return jsonify({"error": "Missing required query parameters"}), 400

    routes = get_received_routes(host, username, password, peer)
    return jsonify(routes)


if __name__ == "__main__":
    app.run(debug=True)
