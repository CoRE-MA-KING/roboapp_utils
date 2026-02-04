import random

from examples.common.expub import ExamplePub
from examples.domain.proto.disks_pb2 import Disks

key_expr = "disks"


class DisksPub(ExamplePub):
    def create_message(self) -> Disks:
        return Disks(
            left=random.randint(0, 35),
            right=random.randint(0, 35),
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--hz", type=float, help="Publishing frequency in Hz")
    args = parser.parse_args()
    publisher = DisksPub(key_expr, args.hz)
    publisher.run()
