"""Desktop monitor twin post stand."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '322cecd5-e52d-4678-bbf7-3f7ad8910697'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/desktop computer_322cecd5-e52d-4678-bbf7-3f7ad8910697.svg'
SOURCE_REFERENCES = (('322cecd5-e52d-4678-bbf7-3f7ad8910697', 'pictographic-primitives/computers/batch-02/desktop computer_322cecd5-e52d-4678-bbf7-3f7ad8910697.svg'), ('6d96615a-ee89-53a8-b1c1-1dd166ab226d', 'pictographic-primitives/computers/batch-02/desktop computer_6d96615a-ee89-53a8-b1c1-1dd166ab226d.svg'), ('94bf7c3e-3c0a-4019-a95a-f28f2638320e', 'pictographic-primitives/computers/batch-02/desktop computer_94bf7c3e-3c0a-4019-a95a-f28f2638320e.svg'), ('57e73e3c-1182-4352-b22f-1138e2fce8d0', 'pictographic-primitives/computers/batch-02/display_57e73e3c-1182-4352-b22f-1138e2fce8d0.svg'))


class DesktopMonitorTwinPostStand(Solo48):
    icon_id = 'desktop-monitor-twin-post-stand'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ('desktop-display',)
    keywords = ("computer", "screen", "device", "lucide-monitor")

    def build(self) -> None:
        # HRECT_XL: centerline extremes (2,5)-(46,43); symmetry x=24.
        self.add_line("top", (6,5), (42,5))
        self.add_arc("top-right", (42,5), (46,9), radius_x=4)
        self.add_line("right-1", (46,9), (46,25))
        self.add_line("right-2", (46,25), (46,29))
        self.add_arc("bottom-right", (46,29), (42,33), radius_x=4)
        self.add_line("bottom-1", (42,33), (30,33))
        self.add_line("bottom-2", (30,33), (18,33))
        self.add_line("bottom-3", (18,33), (6,33))
        self.add_arc("bottom-left", (6,33), (2,29), radius_x=4)
        self.add_line("left-1", (2,29), (2,25))
        self.add_line("left-2", (2,25), (2,9))
        self.add_arc("top-left", (2,9), (6,5), radius_x=4)
        self.add_contour("screen", "top", "top-right", "right-1", "right-2", "bottom-right", "bottom-1", "bottom-2", "bottom-3", "bottom-left", "left-1", "left-2", "top-left", closed=True)
        self.add_line("chin", (2,25), (46,25))
        self.relate("connect", "screen", "chin")
        self.add_line("post-left", (18,33), (18,43))
        self.add_line("post-right", (30,33), (30,43))
        self.add_polyline("foot", (10,43), (18,43), (30,43), (38,43))
        for post in ("post-left", "post-right"):
            self.relate("connect", "screen", post)
            self.relate("connect", "foot", post)
