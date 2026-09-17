"""Vertical Compression between Boundaries — batch 52."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c2baf313-e4e0-4c97-b27e-19773900c366'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/shrink vertical 1_c2baf313-e4e0-4c97-b27e-19773900c366.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vertical-compression-between-boundaries'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('vertical', 'compression', 'between', 'boundaries')

    def build(self):
        # Plan: equal upper/lower boundaries and two inward arrows sharing attachment points.
        # SQUARE extremes6,6,42,42. Lucide fold-vertical informs opposed open heads.
        for n,y,s in [('upper',6,1),('lower',42,-1)]:
            tip=y+s*14
            self.add_polyline(n+'-boundary',(6,y),(24,y),(42,y))
            self.add_line(n+'-shaft',(24,y),(24,tip))
            self.add_polyline(n+'-head',(16,tip-s*8),(24,tip),(32,tip-s*8))
            self.relate('connect',n+'-shaft',n+'-boundary');self.relate('connect',n+'-shaft',n+'-head')


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4):self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

