"""A horizontal CCTV camera faces right with a left wall mount. Lucide cctv informs connected neck and bracket. Omit the joint ring and doubled wall plate; mirrored directional geometry preserves the lens hood."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9855e343-79e1-5f85-9909-e1d72ecb3d7e'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance cctv_9855e343-79e1-5f85-9909-e1d72ecb3d7e.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'cctv-camera-facing-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('cctv', 'camera', 'surveillance', 'security', 'wall mount', 'monitoring', 'video', 'bullet camera')

    def build(self):
        # HRECT_L centerline extremes (4, 8, 44, 40).

        mirror = True
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
