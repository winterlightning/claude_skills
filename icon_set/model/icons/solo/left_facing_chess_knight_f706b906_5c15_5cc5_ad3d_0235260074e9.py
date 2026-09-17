"""Left Facing Chess Knight.

Plan: Left-facing knight with broad mane and angular muzzle above pedestal. Lucide chess-knight informs the ear and neck. Omit eye. Bounds (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f706b906-5c15-5cc5-ad3d-0235260074e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/chess knight_f706b906-5c15-5cc5-ad3d-0235260074e9.svg'
AUTHOR = 'gpt-6'

class LeftFacingChessKnight(Solo48):
    icon_id = 'left-facing-chess-knight'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/hobbies"
    aliases = ()
    keywords = ('left', 'facing', 'chess', 'knight')

    def build(self):
        mirror=False
        def p(x,y):return (48-x,y) if mirror else (x,y)
        self.add_polyline('front',p(8,44),p(8,36),p(16,36),p(24,22),p(12,24))
        self.add_arc('muzzle',p(12,24),p(8,20),radius_x=4,sweep=not mirror)
        self.add_polyline('brow',p(8,20),p(20,8),p(20,4))
        self.add_arc('mane',p(20,4),p(40,24),radius_x=20,sweep=not mirror)
        self.add_polyline('back',p(40,24),p(36,36),p(40,36),p(40,44),p(8,44))
        self.add_contour('piece',*[f'front-{i}' for i in range(1,5)],'muzzle','brow-1','brow-2','mane',*[f'back-{i}' for i in range(1,5)],closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ['front','brow','back']]
        self.add_line('base',p(16,36),p(36,36));self.relate('connect','piece','base')
