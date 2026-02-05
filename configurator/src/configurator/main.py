from pathlib import Path

from prompt_toolkit.shortcuts import (
    radiolist_dialog,
)

from configurator.autostart import parse_autostart, place_autostart
from configurator.systemd import (
    enable_systemd_service,
    place_zenoh_config,
    run_systemd_services,
)

if __name__ == "__main__":
    tasks = (
        ("install", "起動設定のインストール"),
        ("start", "Roboappの起動・停止"),
        ("setup", "Roboappの自動起動の設定・解除"),
    )

    result = radiolist_dialog(
        title="Roboapp Configurator",
        text="実行内容を選んでください",
        values=tasks,
        default=tasks[0][0],
    ).run()

    match result:
        case "install":
            root_path = Path(__file__).parents[4] / "autostart.toml"

            targets = parse_autostart(root_path)

            for t in targets:
                place_autostart(t)

            place_zenoh_config()
        case "start":
            res_start: bool | None = radiolist_dialog(
                title="Roboappの起動・停止",
                text="Roboappを起動しますか？",
                values=[(True, "起動"), (False, "停止")],
                default=True,
            ).run()
            if res_start is None:
                exit(0)

            run_systemd_services(res_start)
        case "setup":
            res_setup: bool | None = radiolist_dialog(
                title="Roboappの自動起動の設定・解除",
                text="Roboappの自動起動を設定しますか？",
                values=[(True, "設定"), (False, "解除")],
                default=True,
            ).run()
            if res_setup is None:
                exit(0)

            enable_systemd_service(res_setup)
        case _:
            pass
