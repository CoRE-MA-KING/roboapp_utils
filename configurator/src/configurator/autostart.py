import tomllib
from collections.abc import Sequence
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel

from configurator.systemd import get_service_folder, place_zenoh_config


class AutoStart(BaseModel):
    app_folder: Path
    name: str
    working_dir: str
    executable: str
    args: str | Sequence[str] | None = ""


def place_autostart(target: AutoStart) -> None:
    env = Environment(
        loader=FileSystemLoader((Path(__file__).parents[2] / "template" / "systemd")),
        autoescape=False,
    )
    template = env.get_template("example.service.tmpl")
    rendered = template.render(target.model_dump())

    with open(
        get_service_folder() / f"roboapp-{target.name}.service", "w"
    ) as service_file:
        service_file.write(rendered)


def parse_autostart(target: Path) -> Sequence[AutoStart]:
    ret = []
    with open(target, "rb") as f:
        x = tomllib.load(f)
        for k, v in x.items():
            args = v.get("args", None)
            if isinstance(args, list):
                args = " ".join(args)
            elif args is None:
                args = ""

            ret.append(
                AutoStart(
                    app_folder=target.parent,
                    name=k,
                    working_dir=v["working_dir"],
                    executable=v["executable"],
                    args=args,
                )
            )
    return ret


def auto_start(root_path: Path) -> None:
    print(root_path)
    targets = parse_autostart(root_path)
    print(targets)

    for t in targets:
        place_autostart(t)

    place_zenoh_config()
