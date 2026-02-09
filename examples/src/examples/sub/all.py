import time

import zenoh
from examples.common.zenoh_transmitter import create_zenoh_session
from google.protobuf.message import Message
from roboapp.camera_port_pb2 import CameraPortMessage
from roboapp.camera_switch_pb2 import CameraSwitchMessage
from roboapp.damage_panel_pb2 import DamagePanelMessage
from roboapp.disks_pb2 import DisksMessage
from roboapp.flap_pb2 import FlapMessage
from roboapp.lidar_range_pb2 import LiDARRange
from roboapp.lidar_vector_pb2 import LiDARVector
from roboapp.robot_state_pb2 import RobotStateMessage

key_expr = (
    "lidar/force_vector",
    "lidar/range",
    "cam/port",
    "cam/switch",
    "damagepanel",
    "flap",
    "disks",
    "robotstate",
)

key_to_proto: dict[str, type[Message]] = {
    "lidar/force_vector": LiDARVector,
    "lidar/range": LiDARRange,
    "cam/switch": CameraSwitchMessage,
    "cam/port": CameraPortMessage,
    "damagepanel": DamagePanelMessage,
    "flap": FlapMessage,
    "disks": DisksMessage,
    "robotstate": RobotStateMessage,
}


def callback(sample: zenoh.Sample) -> None:
    key = str(sample.key_expr)

    proto_class: type[Message] | None = key_to_proto.get(key, None)

    if proto_class is None:
        print(f"Received {key}: {sample.payload.to_string()}")
        return

    msg = proto_class.FromString(sample.payload.to_bytes())
    print(f"Received {key}: {msg}")


if __name__ == "__main__":
    with create_zenoh_session() as session:
        for k in key_expr:
            session.declare_subscriber(k, callback)

        while True:
            time.sleep(1)
