"""A cylindrical brush angles upward-right from a long narrow handle with a rounded end. Straight bristles project from both sides of the broad rounded brush head.
Symbol plan: Diagonal cylindrical brush capsule with radius-5 ends, exact 3:4 tangents, two bristles on either side and a long single-stroke handle. Shared normal and pitch define both bristle rows.
Keyshape: CIRCLE; centerline extremes radius 20 about (24,24).
Construction reference: brush; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b7486990-cc91-477d-b188-5344514de41f'
SOURCE_PATH = 'pictographic-primitives/beauty/hair dress round brush 1_b7486990-cc91-477d-b188-5344514de41f.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'round-hairbrush-with-long-handle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('round', 'hairbrush', 'with', 'long', 'handle')

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

        segments('head-inner',(21,20),(25,17),(33,11))
        self.add_arc('tip',(33,11),(39,19),radius_x=5)
        segments('head-outer',(39,19),(31,25),(27,28))
        self.add_arc('heel-a',(27,28),(20,27),radius_x=5)
        self.add_arc('heel-b',(20,27),(21,20),radius_x=5)
        self.add_contour('brush','head-inner-1','head-inner-2','tip','head-outer-1','head-outer-2','heel-a','heel-b',closed=True)
        self.add_line('handle',(20,27),(8,36))
        self.relate('connect','handle','brush')
        for j,(x,y,dx,dy) in enumerate([(25,17,-3,-4),(33,11,-3,-4),(31,25,3,4),(39,19,3,4)]):
         self.add_line(f'bristle-{j}',(x,y),(x+dx,y+dy))
         self.relate('connect',f'bristle-{j}','brush')
