"""Funnel with Rounded Outlet.
Plan: Broad straight rim tapers to an eight-unit-wide outlet on the vertical axis. Ink (4,4)-(44,44).
Reference construction: funnel.
Reduction: Retain the rounded flat outlet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ddd3a18-50e8-5af4-89b5-45dddb136f94'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/filter_8ddd3a18-50e8-5af4-89b5-45dddb136f94.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'funnel-with-rounded-outlet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('funnel', 'with', 'rounded', 'outlet')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('upper',(6,6),(42,6),(28,26),(28,40))
        self.add_arc('br',(28,40),(26,42),radius_x=2)
        self.add_line('bottom',(26,42),(22,42))
        self.add_arc('bl',(22,42),(20,40),radius_x=2)
        self.add_polyline('left',(20,40),(20,26),(6,6))
        self.relate('connect','upper','br');self.relate('connect','br','bottom');self.relate('connect','bottom','bl');self.relate('connect','bl','left');self.relate('connect','left','upper')
