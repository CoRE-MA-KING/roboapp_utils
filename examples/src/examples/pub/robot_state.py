import argparse
import random
from typing import Literal

from examples.common.expub import ExamplePub
from examples.domain.messages import RobotStateId, RobotStateMessage

key_expr = "robotstate"


class RobotStatePub(ExamplePub):
    def create_message(self) -> RobotStateMessage:
        state_ids = list(RobotStateId)
        colors: list[Literal["blue", "red"]] = ["blue", "red"]
        return RobotStateMessage(
            state=random.choice(state_ids).value,
            color=random.choice(colors),
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--hz", type=float, help="Publishing frequency in Hz")
    args = parser.parse_args()
    publisher = RobotStatePub(key_expr, args.hz)
    publisher.run()
