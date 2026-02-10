import random

from examples.common.expub import ExamplePub
from roboapp.damagepanel_target_pb2 import DamagePanelTargetMessage, Target

key_expr = "damagepanel"


class DamagePanelPub(ExamplePub):
    def __init__(self, key: str, hz: float | None, no: bool = False) -> None:
        super().__init__(key, hz)
        self.no = no

    def create_message(self) -> DamagePanelTargetMessage:
        if self.no:
            msg = DamagePanelTargetMessage(target=None)
        else:
            msg = DamagePanelTargetMessage(
                target=Target(
                    x=random.randint(0, 1280),
                    y=random.randint(0, 720),
                    distance=random.randint(0, 100),
                    width=random.randint(10, 50),
                    height=random.randint(20, 100),
                )
            )
        return msg


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--hz", type=float, help="Publishing frequency in Hz")
    parser.add_argument(
        "-n", action="store_true", help="Send empty target (None) if specified"
    )
    args = parser.parse_args()
    publisher = DamagePanelPub(key_expr, args.hz, args.n)
    publisher.run()
