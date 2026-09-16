"""A front-facing hooded sweatshirt has a folded hood opening, broad shoulders and long sleeves. Small cuffs extend below the sleeve ends, with a short central line beneath the neckline.
Symbol plan: Mirrored long sleeves and a broad hood on axis x24. The hood uses one elliptical crown and one shallow opening. Cuff seams repeat at y30; omit the short drawstring and pocket.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: shirt. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5ea4efe7-6268-556c-b803-08c8ca011cf1'
SOURCE_PATH = 'pictographic-primitives/clothes/hoodie_5ea4efe7-6268-556c-b803-08c8ca011cf1.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'hoodie-with-cuffed-sleeves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    aliases = ()
    keywords = ('hoodie', 'with', 'cuffed', 'sleeves')

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

        self.add_arc('hood-crown',(14,14),(34,14),radius_x=10,radius_y=8)
        self.add_arc('shoulder-right',(34,14),(42,24),radius_x=8,radius_y=10)
        segments('right',(42,24),(42,30),(42,38),(34,38),(34,42),(14,42),(14,38),(6,38),(6,30),(6,24))
        self.add_arc('shoulder-left',(6,24),(14,14),radius_x=8,radius_y=10)
        self.add_contour('sweatshirt','hood-crown','shoulder-right',*[f'right-{j}' for j in range(1,10)],'shoulder-left',closed=True)
        self.add_arc('hood-opening',(14,14),(34,14),radius_x=10,radius_y=4,sweep=False)
        self.relate('connect','hood-opening','sweatshirt')
        for n,x,outer in [('left',14,6),('right',34,42)]:
         self.add_polyline(n+'-sleeve',(x,26),(x,30),(x,38))
         self.add_line(n+'-cuff',(outer,30),(x,30))
         self.relate('connect',n+'-sleeve','sweatshirt');self.relate('connect',n+'-cuff','sweatshirt');self.relate('connect',n+'-cuff',n+'-sleeve')
