"""A horizontal CCTV camera faces left with a right wall mount. Lucide cctv informs the connected neck and bracket. Omit the small joint ring and doubled wall plate; open the lower lens hood to eliminate a tiny enclosed wedge."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24db39c9-5e45-47cb-9ee2-fd6fc86b8198'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance cctv_24db39c9-5e45-47cb-9ee2-fd6fc86b8198.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'cctv-camera-facing-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('cctv', 'camera', 'surveillance', 'security', 'wall mount', 'monitoring', 'video', 'bullet camera')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        mirror = False
        def p(x,y): return (48-x,y) if mirror else (x,y)
        self.add_polyline('housing',p(4,8),p(38,8),p(38,24),p(24,24),p(12,24),p(4,16),closed=True)
        self.add_line('lens',p(4,16),p(4,24))
        self.relate('connect','lens','housing')
        self.add_line('neck',p(24,24),p(24,32))
        self.add_arc('bend',p(24,32),p(28,36),radius_x=4,sweep=mirror)
        self.add_line('arm',p(28,36),p(44,36))
        self.add_contour('mount','neck','bend','arm')
        self.relate('connect','mount','housing')
        self.add_polyline('wall',p(44,30),p(44,36),p(44,40))
        self.relate('connect','mount','wall')
