import argparse

from examples.common.expub import ExamplePub
from examples.domain.proto.robot_state_pb2 import RobotState

key_expr = "robotstate"


class RobotStatePub(ExamplePub):
    def create_message(self) -> RobotState:
        # RobotStateIdのenum値は適宜置き換えてください
        return RobotState(
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
