import random

from examples.common.expub import ExamplePub
from roboapp.flap_pb2 import FlapMessage

key_expr = "flap"


class FlapPub(ExamplePub):
    def create_message(self) -> FlapMessage:
        return FlapMessage(
            pitch=random.uniform(0.0, 15.0),
            yaw=random.uniform(0.0, 40.0),
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--hz", type=float, help="Publishing frequency in Hz")
    args = parser.parse_args()
    publisher = FlapPub(key_expr, args.hz)
    publisher.run()
