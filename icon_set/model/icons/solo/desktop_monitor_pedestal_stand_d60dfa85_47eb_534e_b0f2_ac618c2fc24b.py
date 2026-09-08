"""Desktop monitor pedestal stand."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd60dfa85-47eb-534e-b0f2-ac618c2fc24b'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/desktop computer pc_d60dfa85-47eb-534e-b0f2-ac618c2fc24b.svg'
AUTHOR = 'astra-chatgpt'
SOURCE_REFERENCES = (('d60dfa85-47eb-534e-b0f2-ac618c2fc24b', 'pictographic-primitives/computers/batch-02/desktop computer pc_d60dfa85-47eb-534e-b0f2-ac618c2fc24b.svg'), ('09fbfc2b-65a0-4684-b8ee-0ad753b3dbf9', 'pictographic-primitives/computers/batch-02/monitor_09fbfc2b-65a0-4684-b8ee-0ad753b3dbf9.svg'), ('52093ce8-9f15-5ca2-8b57-8fb10859386a', 'pictographic-primitives/computers/batch-02/monitor_52093ce8-9f15-5ca2-8b57-8fb10859386a.svg'), ('bb4efcce-3bcd-4db5-afc0-759ebd202171', 'pictographic-primitives/computers/batch-02/monitor_bb4efcce-3bcd-4db5-afc0-759ebd202171.svg'))


class DesktopMonitorPedestalStand(Solo48):
    icon_id = 'desktop-monitor-pedestal-stand'
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
        self.add_line("bottom-1", (42,33), (29,33))
        self.add_line("bottom-2", (29,33), (19,33))
        self.add_line("bottom-3", (19,33), (6,33))
        self.add_arc("bottom-left", (6,33), (2,29), radius_x=4)
        self.add_line("left-1", (2,29), (2,25))
        self.add_line("left-2", (2,25), (2,9))
        self.add_arc("top-left", (2,9), (6,5), radius_x=4)
        self.add_contour("screen", "top", "top-right", "right-1", "right-2", "bottom-right", "bottom-1", "bottom-2", "bottom-3", "bottom-left", "left-1", "left-2", "top-left", closed=True)
        self.add_line("chin", (2,25), (46,25))
        self.relate("connect", "screen", "chin")
        self.add_polyline("pedestal", (19,33), (15,43), (33,43), (29,33))
        self.relate("connect", "screen", "pedestal")
