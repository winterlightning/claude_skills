"""Funnel with Slanted Outlet.
Plan: Broad straight rim tapers to an eight-unit-wide outlet on the vertical axis. Ink (4,4)-(44,44).
Reference construction: funnel.
Reduction: Retain the diagonal cut at the outlet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2029fee1-3510-5860-8592-f696bb58965d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/filter_2029fee1-3510-5860-8592-f696bb58965d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'funnel-with-slanted-outlet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('funnel', 'with', 'slanted', 'outlet')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('upper',(6,6),(42,6),(28,26),(28,36))
        self.add_polyline('lower',(28,36),(20,42),(20,26),(6,6))
        self.relate('connect','upper','lower')
