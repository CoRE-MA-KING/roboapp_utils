import random

from examples.common.expub import ExamplePub
from examples.domain.proto.camera_switch_pb2 import CameraSwitch

key_expr = "cam/switch"


class CameraSwitchPub(ExamplePub):
    def create_message(self) -> CameraSwitch:
        return CameraSwitch(camera_id=random.randint(0, 2))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--hz", type=float, help="Publishing frequency in Hz")
    args = parser.parse_args()
    publisher = CameraSwitchPub(key_expr, args.hz)
    publisher.run()
