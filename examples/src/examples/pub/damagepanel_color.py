import random

from examples.src.buf import validate

from examples.common.expub import ExamplePub
from roboapp.damagepanel_color_pb2 import DamagePanelColorMessage

key_expr = "damagepanel"


class DamagePanelPub(ExamplePub):
    def __init__(self, key: str, hz: float | None) -> None:
        super().__init__(key, hz)

    def create_message(self) -> DamagePanelColorMessage:
        msg = DamagePanelColorMessage(color=random.choice(["red", "blue"]))
        validate(msg)
        return msg


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--hz", type=float, help="Publishing frequency in Hz")
    args = parser.parse_args()
    publisher = DamagePanelPub(key_expr, args.hz)
    publisher.run()
