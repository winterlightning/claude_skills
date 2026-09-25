"""Application window below two wireless arcs.
Plan: Upper signal and lower window bands. Nested radii differ by nine units; upper-left signal placement is intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "d12b5c6d-5cff-4f23-9893-76defe7ca390"
SOURCE_PATH = 'pictographic-primitives/other/app window wifi_d12b5c6d-5cff-4f23-9893-76defe7ca390.svg'
AUTHOR = "gpt-6"


class AppWindowWifi(Solo48):
    icon_id = "app-window-wifi"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("wireless-app-window",)
    keywords = ("application", "window", "browser", "wifi", "wireless")

    def build(self) -> None:
        # Nested signal quarters sit above the browser header.
        self.add_arc("wifi-outer", (8, 17), (19, 6), radius_x=11)
        self.add_arc("wifi-inner", (17, 17), (19, 15), radius_x=2)
        self.add_polyline("window", (6, 26), (42, 26), (42, 34), (42, 42), (6, 42), (6, 34), closed=True)
        self.add_line("header-divider", (6, 34), (42, 34))
        self.relate("connect", "window", "header-divider")

PLAN = 'Application window below two wireless arcs. Upper signal and lower window bands.'
OMISSIONS = 'None.'
CONSTRUCTION_REFERENCES = ['icon_set/references/lucide/original/wifi.svg', 'icon_set/references/lucide/atomic-debug/wifi.svg']
PARENT_SOURCE = 'icon_set/model/icons/solo/app_window_wifi_d12b5c6d_5cff_4f23_9893_76defe7ca390.py'
