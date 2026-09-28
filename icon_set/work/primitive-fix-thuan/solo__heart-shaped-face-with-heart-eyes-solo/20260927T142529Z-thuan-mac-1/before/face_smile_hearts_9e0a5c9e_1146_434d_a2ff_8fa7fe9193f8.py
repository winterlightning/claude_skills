"""Heart-shaped face with heart eyes.
Plan: SQUARE uses (6,6)-(42,42); large mirrored hearts sit above a pointed lower face.
Design changes: Heart eyes form the upper face lobes. Shallower eye clefts enlarge their internal openings; the central head cleft and pointed chin retain the heart-face structure. Compact smile retained.
References: Original reference supplies heart eyes, central cleft and pointed chin. Shared mirrored heart construction; human user.svg reviewed for facial vocabulary. No additional Lucide construction used.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8'
SOURCE_PATH='pictographic-primitives/_uncategorized_18/face smile hearts_9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='heart-shaped-face-with-heart-eyes-solo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('heart','eyes','love','smile')
    def build(self):
        for i,(x,s) in enumerate(((13,1),(35,-1))):
            q=lambda dx,y:(x+s*dx,y)
            self.add_bezier(f'eye-{i}',q(0,9),(q(-1,7),q(-2,6),q(-4,6)),(q(-6,6),q(-7,8),q(-7,12)),(q(-7,18),q(-3,23),q(0,26)),(q(3,23),q(7,18),q(7,12)),(q(7,8),q(6,6),q(4,6)),(q(2,6),q(1,7),q(0,9)))
            self.add_contour(f'heart-{i}',f'eye-{i}',closed=True)
        self.add_polyline('cleft',(20,12),(24,16),(28,12))
        self.relate('connect','cleft','heart-0')
        self.relate('connect','cleft','heart-1')
        self.add_bezier('chin',(13,26),((13,35),(18,38),(24,42)),((30,38),(35,35),(35,26)))
        self.relate('connect','chin','heart-0')
        self.relate('connect','chin','heart-1')
        self.add_arc('smile',(22,29),(26,29),radius_x=2,radius_y=1,sweep=False)