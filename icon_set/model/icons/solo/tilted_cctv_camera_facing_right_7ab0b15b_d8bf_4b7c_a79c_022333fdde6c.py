"""A tilted CCTV camera faces right on a bent mount. Independently emitted as a mirrored pair on the same SOLO48 grid. Lucide cctv informs housing and tangent bracket elbow; omit minor corner rounding."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ab0b15b-d8bf-4b7c-a79c-022333fdde6c'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance cctv_7ab0b15b-d8bf-4b7c-a79c-022333fdde6c.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'tilted-cctv-camera-facing-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "protection"
    aliases = ()
    keywords = ('cctv', 'camera', 'surveillance', 'security', 'tilted', 'monitoring', 'video', 'mount')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        mirror = True
        def p(x,y): return (48-x,y) if mirror else (x,y)
        self.add_polyline('housing',p(14,16),p(38,8),p(44,26),p(32,30),p(20,34),closed=True)
        self.add_line('lens',p(4,20),p(8,32))
        self.add_line('post',p(32,30),p(32,36))
        self.add_arc('elbow',p(32,36),p(36,40),radius_x=4,sweep=mirror)
        self.add_line('foot',p(36,40),p(44,40))
        self.add_contour('mount','post','elbow','foot')
        self.relate('connect','mount','housing')
