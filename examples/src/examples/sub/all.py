import time

import zenoh

from examples.common.zenoh_transmitter import create_zenoh_session
from examples.domain.proto.roboapp.camera_switch_pb2 import CameraSwitchMessage
from examples.domain.proto.roboapp.damage_panel_pb2 import DamagePanelMessage
from examples.domain.proto.roboapp.disks_pb2 import DisksMessage
from examples.domain.proto.roboapp.flap_pb2 import FlapMessage
from examples.domain.proto.roboapp.lidar_range_pb2 import LiDARRange
from examples.domain.proto.roboapp.lidar_vector_pb2 import LiDARVector
from examples.domain.proto.roboapp.robot_state_pb2 import RobotStateMessage

key_expr = (
    "lidar/force_vector",
    "lidar/range",
    "cam/switch",
    "damagepanel",
    "flap",
    "disks",
    "robotstate",
)

key_to_proto = {
    "lidar/force_vector": LiDARVector,
    "lidar/range": LiDARRange,
    "cam/switch": CameraSwitchMessage,
    "damagepanel": DamagePanelMessage,
    "flap": FlapMessage,
    "disks": DisksMessage,
    "robotstate": RobotStateMessage,
}


def callback(sample: zenoh.Sample) -> None:
    key = str(sample.key_expr)
    proto_class = key_to_proto.get(key)
    if proto_class:
        msg = proto_class.FromString(sample.payload.to_bytes())
        print(f"Received {key}: {msg}")
    else:
        print(f"Received {key}: {sample.payload.to_string()}")


if __name__ == "__main__":
    with create_zenoh_session() as session:
        for k in key_expr:
            session.declare_subscriber(k, callback)

        while True:
            time.sleep(1)
