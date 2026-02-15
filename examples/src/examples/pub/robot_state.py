import argparse
import random

from examples.common.expub import ExamplePub
from roboapp.robot_state_pb2 import RobotStateMessage

key_expr = "robotstate"


class RobotStatePub(ExamplePub):
    def create_message(self) -> RobotStateMessage:
        return RobotStateMessage(
            state=random.randint(0, 6),
            color=random.choice(("blue", "red")),
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--hz", type=float, help="Publishing frequency in Hz")
    args = parser.parse_args()
    publisher = RobotStatePub(key_expr, args.hz)
    publisher.run()
