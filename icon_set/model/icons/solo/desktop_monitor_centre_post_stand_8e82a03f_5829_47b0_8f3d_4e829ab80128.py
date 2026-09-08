"""desktop-monitor-centre-post-stand: reconstructed from the batch-01 references on SOLO48.

Duplicate source drawings share one concept; SOURCE_REFERENCES retains every ID.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e82a03f-5829-47b0-8f3d-4e829ab80128'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/desktop monitor back_8e82a03f-5829-47b0-8f3d-4e829ab80128.svg'
AUTHOR = 'astra-chatgpt'
SOURCE_REFERENCES = (('8e82a03f-5829-47b0-8f3d-4e829ab80128', 'pictographic-primitives/computers/batch-01/desktop monitor back_8e82a03f-5829-47b0-8f3d-4e829ab80128.svg'), ('b5cf2b0b-f25b-5c64-97a8-08abb35fb265', 'pictographic-primitives/computers/batch-01/desktop monitor back_b5cf2b0b-f25b-5c64-97a8-08abb35fb265.svg'), ('181755f1-a8ab-4d25-8475-ebcf6885f0c8', 'pictographic-primitives/computers/batch-01/monitor_181755f1-a8ab-4d25-8475-ebcf6885f0c8.svg'), ('78e9aab1-7764-40a5-b4c1-bf8d31d6b2cb', 'pictographic-primitives/computers/batch-01/monitor_78e9aab1-7764-40a5-b4c1-bf8d31d6b2cb.svg'), ('8d7f3cd4-f98b-4ae1-b9de-7232643f178a', 'pictographic-primitives/computers/batch-02/monitor_8d7f3cd4-f98b-4ae1-b9de-7232643f178a.svg'))

class DesktopMonitorCentrePostStand(Solo48):
    icon_id = "desktop-monitor-centre-post-stand"
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("desktop-monitor", "monitor-on-stand")
    keywords = ("monitor", "display", "screen", "computer", "stand")

    def build(self) -> None:
        # Centreline extremes (2,5)-(46,43). Lucide monitor: equal quarter
        # circles, a centred post, and a balanced horizontal foot.
        self.add_line("top", (6, 5), (42, 5))
        self.add_arc("upper-right", (42, 5), (46, 9), radius_x=4)
        self.add_line("right", (46, 9), (46, 29))
        self.add_arc("lower-right", (46, 29), (42, 33), radius_x=4)
        self.add_line("bottom-right", (42, 33), (24, 33))
        self.add_line("bottom-left", (24, 33), (6, 33))
        self.add_arc("lower-left", (6, 33), (2, 29), radius_x=4)
        self.add_line("left", (2, 29), (2, 9))
        self.add_arc("upper-left", (2, 9), (6, 5), radius_x=4)
        self.add_contour("screen", "top", "upper-right", "right", "lower-right",
                         "bottom-right", "bottom-left", "lower-left", "left",
                         "upper-left", closed=True)
        self.add_line("post", (24, 33), (24, 43))
        self.add_polyline("foot", (15, 43), (24, 43), (33, 43))
        self.relate("connect", "screen", "post")
        self.relate("connect", "post", "foot")
