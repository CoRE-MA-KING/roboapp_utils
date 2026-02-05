import argparse

from examples.common.expub import ExamplePub
from roboapp.robot_state_pb2 import RobotStateMessage

key_expr = "robotstate"


class RobotStatePub(ExamplePub):
    def create_message(self) -> RobotStateMessage:
        # RobotStateIdのenum値は適宜置き換えてください
        return RobotStateMessage(
            state=0,  # 例: IDLE
            color="blue",
        )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--hz", type=float, help="Publishing frequency in Hz")
    args = parser.parse_args()
    publisher = RobotStatePub(key_expr, args.hz)
    publisher.run()
