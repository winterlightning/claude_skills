"""Two long narrow tweezer arms spread apart toward the upper-right from a joined lower-left end. One arm curves gently, and the small joined tip has a slightly flattened outer edge.
Symbol plan: Open diagonal tweezer arms joined by a radius-5 heel. The inner arm is straight; one broad cubic gently flares the outer arm. Both heel joins use the exact 3:4 tangent; omit the tiny flattened tip.
Keyshape: CIRCLE; centerline extremes radius 20 about (24,24).
Construction reference: ruler. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a0a454d8-3104-53f0-a450-a93ac39df363'
SOURCE_PATH = 'pictographic-primitives/beauty/instrument tweezers_a0a454d8-3104-53f0-a450-a93ac39df363.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'open-tweezers-on-diagonal'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('open', 'tweezers', 'on', 'diagonal')

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

        self.add_line('inner-arm',(33,11),(9,29))
        self.add_arc('heel',(9,29),(15,37),radius_x=5,sweep=False)
        self.add_bezier('outer-arm',(15,37),((23,31),(35,24),(43,21)))
        self.add_contour('tweezers','inner-arm','heel','outer-arm')
