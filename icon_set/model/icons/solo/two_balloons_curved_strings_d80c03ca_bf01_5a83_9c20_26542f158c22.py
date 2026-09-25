"""Pair of Party Balloons.
Plan: Two equal oval balloons stagger vertically, each owning its curved string. Extrema (6,6)-(42,42).
Reference: Lucide balloon: coherent inflated outline and gently curved string.
Reduction: Small knot triangles omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd80c03ca-bf01-5a83-9c20-26542f158c22'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/party balloons_d80c03ca-bf01-5a83-9c20-26542f158c22.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'two-balloons-curved-strings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('pair', 'of', 'party', 'balloons')

    def build(self):

        for i,(x,y) in enumerate(((12,16),(36,20))):
            self.add_arc(f'balloon-{i}-a',(x,y-10),(x,y+10),radius_x=6,radius_y=10)
            self.add_arc(f'balloon-{i}-b',(x,y+10),(x,y-10),radius_x=6,radius_y=10)
            self.add_contour(f'balloon-{i}',f'balloon-{i}-a',f'balloon-{i}-b',closed=True)
            self.add_bezier(f'string-{i}',(x,y+10),((x,34),(x-4,36),(x,42)))
            self.relate('connect',f'balloon-{i}',f'string-{i}')
