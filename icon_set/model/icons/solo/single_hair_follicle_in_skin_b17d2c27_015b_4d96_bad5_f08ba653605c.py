"""A broad teardrop-shaped hair root rises to a curved pointed tip above a shallow rounded skin pocket. The skin surface extends horizontally outward from both sides of the follicle.
Symbol plan: One tapered asymmetric hair with a round root above a broad shallow skin pocket. Keep one curved side and one straight side; omit duplicate skin edges.
Keyshape: HRECT_L; centerline extremes (4,8)-(44,40).
Construction reference: droplet; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b17d2c27-015b-4d96-bad5-f08ba653605c'
SOURCE_PATH = 'pictographic-primitives/beauty/hair skin_b17d2c27-015b-4d96-bad5-f08ba653605c.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'single-hair-follicle-in-skin'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    aliases = ()
    keywords = ('single', 'hair', 'follicle', 'in', 'skin')

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

        self.add_arc('hair-left',(28,8),(16,22),radius_x=12,radius_y=14,sweep=False)
        self.add_arc('root',(16,22),(32,22),radius_x=8,sweep=False)
        self.add_line('hair-right',(32,22),(28,8))
        self.add_contour('hair','hair-left','root','hair-right',closed=True)
        self.add_arc('skin',(4,28),(44,28),radius_x=20,radius_y=12,sweep=False)
