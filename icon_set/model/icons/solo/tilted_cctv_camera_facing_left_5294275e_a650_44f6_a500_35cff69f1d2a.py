"""A tilted CCTV camera faces left on a bent mount. Lucide cctv informs tilted housing, detached lens and smooth bracket elbow. Omit minor corner rounding; retain deliberate directional asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5294275e-a650-44f6-a500-35cff69f1d2a'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance cctv 1_5294275e-a650-44f6-a500-35cff69f1d2a.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'tilted-cctv-camera-facing-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    categories = ("protection", "primitives")
    aliases = ()
    keywords = ('cctv', 'camera', 'surveillance', 'security', 'tilted', 'monitoring', 'video', 'mount')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        mirror = False
        def p(x,y): return (48-x,y) if mirror else (x,y)
        self.add_polyline('housing',p(14,16),p(38,8),p(44,26),p(32,30),p(20,34),closed=True)
        self.add_line('lens',p(4,20),p(8,32))
        self.add_line('post',p(32,30),p(32,36))
        self.add_arc('elbow',p(32,36),p(36,40),radius_x=4,sweep=mirror)
        self.add_line('foot',p(36,40),p(44,40))
        self.add_contour('mount','post','elbow','foot')
        self.relate('connect','mount','housing')
