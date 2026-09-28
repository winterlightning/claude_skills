"""Counterclockwise Synchronize Arrows.
Plan: Two equal opposing circular sweeps and heads repeat under a half turn. Ink (4,4)-(44,44).
Reference construction: refresh-ccw.
Reduction: Keep the two opposing arrows; square their open heads for clarity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bafc5d96-6820-5892-a08b-927ab58a96ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/synchronize arrows_bafc5d96-6820-5892-a08b-927ab58a96ff.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'counterclockwise-synchronize-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('counterclockwise', 'synchronize', 'arrows')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_bezier('upper-tail',(38,12),((35,8),(29,6),(24,6)))
        self.add_arc('upper-arc',(24,6),(6,24),radius_x=18,sweep=False)
        self.add_contour('upper','upper-tail','upper-arc')
        self.add_bezier('lower-tail',(10,36),((13,40),(19,42),(24,42)))
        self.add_arc('lower-arc',(24,42),(42,24),radius_x=18,sweep=False)
        self.add_contour('lower','lower-tail','lower-arc')
        self.add_polyline('left-head',(6,16),(6,24),(14,24))
        self.add_polyline('right-head',(34,24),(42,24),(42,32))
        self.relate('connect','upper','left-head');self.relate('connect','lower','right-head')
