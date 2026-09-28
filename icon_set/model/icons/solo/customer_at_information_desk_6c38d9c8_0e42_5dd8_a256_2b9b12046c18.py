"""A large standing customer faces a smaller attendant behind a horizontal desk line. Both figures have circular heads and rounded shoulders, while the foreground customer's body tapers downward.
Symbol plan: Standing customer faces a bust attendant behind the desk. Both heads use radius 4; customer neck (12,22) and attendant shoulder crown (34,28) yield exactly 4 ink gap. Shared human references supply stick and bust anatomy; omit clothing outlines and attendant chest line.
Keyshape: SQUARE; centerline extremes (6,6)-(42,42).
Construction reference: human_ref/full_body_ref.png; human_ref/user.svg. Lucide original and atomic-debug renders inspected where named.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c38d9c8-0e42-5dd8-a256-2b9b12046c18'
SOURCE_PATH = 'pictographic-primitives/companies/information desk customer_6c38d9c8-0e42-5dd8-a256-2b9b12046c18.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'customer-at-information-desk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'companies'
    categories = ('primitives', 'companies')
    aliases = ()
    keywords = ('customer', 'at', 'information', 'desk')

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

        circle('customer-head',12,10,4);circle('attendant-head',34,16,4)
        self.add_line('customer-torso',(12,22),(12,34))
        self.add_polyline('customer-arms',(6,26),(12,22),(20,22));self.relate('connect','customer-torso','customer-arms')
        self.add_polyline('customer-legs',(6,42),(12,34),(18,42));self.relate('connect','customer-torso','customer-legs')
        self.add_arc('shoulder-left',(26,36),(34,28),radius_x=8)
        self.add_arc('shoulder-right',(34,28),(42,36),radius_x=8)
        self.add_contour('attendant-body','shoulder-left','shoulder-right')
        self.add_polyline('desk',(24,36),(26,36),(42,36),(42,42));self.relate('connect','desk','attendant-body')
        self.mark_human_figure('customer',head='customer-head',torso='customer-torso',torso_junction='start')
