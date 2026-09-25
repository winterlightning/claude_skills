"""Two long curved hairs extend upward from teardrop roots inside a rectangular skin section. A wavy internal boundary crosses the block, while gaps in the upper surface accommodate the hairs.
Symbol plan: Two circular roots with long curved hair shafts inside an open-topped skin section. Repeat centres at x17 and x31. Omit the crowded internal layer wave and top-surface fragments.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: droplet; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f4508f56-aef2-4bd3-9429-b9e29c295ea1'
SOURCE_PATH = 'pictographic-primitives/beauty/hair under skin_f4508f56-aef2-4bd3-9429-b9e29c295ea1.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'two-hair-roots-beneath-skin'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('two', 'hair', 'roots', 'beneath', 'skin')

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

        self.add_polyline('skin',(6,22),(6,42),(42,42),(42,22))
        for j,x in enumerate((17,31)):
         self.add_arc(f'root-{j}-right',(x,27),(x,33),radius_x=3)
         self.add_arc(f'root-{j}-left',(x,33),(x,27),radius_x=3)
         self.add_contour(f'root-{j}',f'root-{j}-right',f'root-{j}-left',closed=True)
         self.add_line(f'shaft-{j}',(x,27),(x,18))
         self.add_arc(f'curve-{j}',(x,18),(x+6,6),radius_x=6,radius_y=12)
         self.add_contour(f'hair-{j}',f'shaft-{j}',f'curve-{j}')
         self.relate('connect',f'hair-{j}',f'root-{j}')
