import shutil
import subprocess
from pathlib import Path

from configurator.config import get_default_config_path


def get_service_folder() -> Path:
    systemd_path = Path.home() / ".config" / "systemd" / "user"
    systemd_path.mkdir(parents=True, exist_ok=True)
    return systemd_path


def get_service() -> list[str]:
    ret = [
        f.stem.replace(".service", "")
        for f in get_service_folder().glob("roboapp-*.service")
    ]

    return ret


def place_zenoh_config() -> None:
    shutil.copy2(
        Path(__file__).parents[2] / "template" / "zenoh.json5",
        get_default_config_path("zenoh.json5"),
    )
    shutil.copy2(
        Path(__file__).parents[2] / "template" / "roboapp-zenohd.service",
        get_service_folder() / "roboapp-zenohd.service",
    )


def run_systemd_services(start: bool = True) -> None:
    action = "start" if start else "stop"
    for service in get_service():
        cmd = ["systemctl", "--user", action, service]
        print(f"{'Starting' if start else 'Stopping'} service: {service}, {cmd}")
        subprocess.run(cmd, check=True)


def enable_systemd_service(enable: bool) -> None:
    action = "enable" if enable else "disable"
    for service in get_service():
        cmd = ["systemctl", "--user", action, service]
        print(f"{'Enabling' if enable else 'Disabling'} service: {service}, {cmd}")
        subprocess.run(cmd, check=True)
