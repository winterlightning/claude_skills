"""A tall pair of closed scissors stands beside an upright comb. Two round finger loops sit below the narrow blades, while the comb has a rounded spine and evenly spaced teeth.
Symbol plan: Natural hairdressing tool pair. Two radius-3 finger loops, one joined closed blade, and an independent comb with three regularly spaced teeth. Omit blade seam and finger-rest curl.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: scissors; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '61493023-ec96-4908-8cca-eac5be45de0a'
SOURCE_PATH = 'pictographic-primitives/beauty/hair dress cut_61493023-ec96-4908-8cca-eac5be45de0a.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'hairdressing-scissors-and-comb'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('hairdressing', 'scissors', 'and', 'comb')

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

        for name,x in [('left',9),('right',23)]:
         circle(name+'-loop',x,39,3)
         self.add_line(name+'-shank',(x,36),(17,18))
         self.relate('connect',name+'-loop',name+'-shank')
        self.relate('connect','left-shank','right-shank')
        self.add_line('blade',(17,18),(17,6))
        for n in ('left-shank','right-shank'):self.relate('connect','blade',n)
        self.add_line('comb-top',(34,6),(42,6))
        self.add_line('comb-right',(42,6),(42,38))
        self.add_arc('comb-end',(42,38),(34,38),radius_x=4)
        segments('comb-left',(34,38),(34,22),(34,14),(34,6))
        self.add_contour('comb','comb-top','comb-right','comb-end','comb-left-1','comb-left-2','comb-left-3',closed=True)
        for j in range(3):
         y=6+8*j
         self.add_line(f'tooth-{j}',(28,y),(34,y))
         self.relate('connect',f'tooth-{j}','comb')
