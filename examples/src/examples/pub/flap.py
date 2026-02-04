import random

from examples.common.expub import ExamplePub
from examples.domain.proto.flap_pb2 import Flap

key_expr = "flap"


class FlapPub(ExamplePub):
    def create_message(self) -> Flap:
        return Flap(
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
