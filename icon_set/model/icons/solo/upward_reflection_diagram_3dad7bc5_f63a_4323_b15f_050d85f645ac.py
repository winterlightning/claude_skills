"""Upward Reflection Diagram — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3dad7bc5-f63a-4323-b15f-050d85f645ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/reflect up_3dad7bc5-f63a-4323-b15f-050d85f645ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upward-reflection-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('upward', 'reflection', 'diagram')

    def build(self):
        # Plan: mirrored triangles across a horizontal axis, left curved transfer arrow.
        # SQUARE extremes6,6,42,42. Source triangles preserved; Lucide open arrow construction.
        self.add_polyline('upper',(22,6),(42,6),(32,16),closed=True)
        self.add_polyline('lower',(22,42),(42,42),(32,32),closed=True)
        self.add_line('axis',(26,24),(42,24))
        self.add_bezier('turn',(14,35),((10,35),(6,31),(6,27)),((6,21),(12,16),(18,16)))
        self.add_polyline('head',(10,12),(18,16),(18,24));self.relate('connect','turn','head')


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

