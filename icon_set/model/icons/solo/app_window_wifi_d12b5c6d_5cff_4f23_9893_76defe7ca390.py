"""Application browser window with wireless signal arcs above it."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "d12b5c6d-5cff-4f23-9893-76defe7ca390"
SOURCE_PATH = "icon_set/work/todo-references/app window wifi_d12b5c6d-5cff-4f23-9893-76defe7ca390.svg"
AUTHOR = "gpt-6"


class AppWindowWifi(Solo48):
    icon_id = "app-window-wifi"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/interface"
    aliases = ("wireless-app-window",)
    keywords = ("application", "window", "browser", "wifi", "wireless")

    def build(self) -> None:
        # Nested signal quarters sit above the browser header.
        self.add_arc("wifi-outer", (8, 18), (20, 6), radius_x=12)
        self.add_arc("wifi-inner", (16, 18), (20, 14), radius_x=4)
        self.add_polyline("window", (6, 26), (42, 26), (42, 42), (6, 42), closed=True)
        self.add_line("header-divider", (6, 34), (42, 34))
        self.relate("connect", "window", "header-divider")
