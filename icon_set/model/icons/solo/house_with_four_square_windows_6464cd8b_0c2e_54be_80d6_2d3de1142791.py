"""A house-shaped silhouette has a high peaked roof and rounded lower corners. Four square windows form an evenly spaced two-by-two grid across the otherwise blank facade.
Symbol plan: Symmetric peaked house with four equal square window panes in a 2x2 block. Shared mullions keep all four openings readable; omit the bottom facade line and gaps between independent window frames.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: house; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6464cd8b-0c2e-54be-80d6-2d3de1142791'
SOURCE_PATH = 'pictographic-primitives/building/home_6464cd8b-0c2e-54be-80d6-2d3de1142791.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'house-with-four-square-windows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('house', 'with', 'four', 'square', 'windows')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        self.add_polyline('house',(6,42),(6,18),(24,6),(42,18),(42,42))
        self.add_polyline('window-frame',(15,22),(24,22),(33,22),(33,31),(33,40),(24,40),(15,40),(15,31),closed=True)
        self.add_polyline('vertical-mullion',(24,22),(24,31),(24,40))
        self.add_polyline('horizontal-mullion',(15,31),(24,31),(33,31))
        self.relate('connect','window-frame','vertical-mullion');self.relate('connect','window-frame','horizontal-mullion');self.relate('connect','vertical-mullion','horizontal-mullion')
