"""Right Facing Chess Knight.

Plan: Right-facing knight with a swept mane and angular muzzle above pedestal. Mirrored construction of shared knight geometry; distinct source preserved. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '953e8247-c199-5111-b2f0-9e8b778321d7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess knight_953e8247-c199-5111-b2f0-9e8b778321d7.svg'
AUTHOR = 'gpt-6'

class RightFacingChessKnight(Solo48):
    icon_id = 'right-facing-chess-knight'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hobbies"
    aliases = ()
    keywords = ('right', 'facing', 'chess', 'knight')

    def build(self):
        mirror=True
        def p(x,y):return (48-x,y) if mirror else (x,y)
        self.add_polyline('front',p(8,44),p(8,36),p(16,36),p(24,22),p(12,24))
        self.add_arc('muzzle',p(12,24),p(8,20),radius_x=4,sweep=not mirror)
        self.add_polyline('brow',p(8,20),p(20,8),p(20,4))
        self.add_arc('mane',p(20,4),p(40,24),radius_x=20,sweep=not mirror)
        self.add_polyline('back',p(40,24),p(36,36),p(40,36),p(40,44),p(8,44))
        self.add_contour('piece',*[f'front-{i}' for i in range(1,5)],'muzzle','brow-1','brow-2','mane',*[f'back-{i}' for i in range(1,5)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['front','brow','back']]
        self.add_line('base',p(16,36),p(36,36));self.relate('connect','piece','base')
