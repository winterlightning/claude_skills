"""money bill: complete SOLO48 repair.
Kept all four banknote corner ornaments and the central medallion; enlarged corner radii from eight to ten.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '57a71ef9-0c30-4a25-a290-84a6666d4f6e'
SOURCE_PATH = 'pictographic-primitives/other/money bill_57a71ef9-0c30-4a25-a290-84a6666d4f6e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'money-bill'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('money bill',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)



    def banknote(self):
        self.add_polyline('note',(4,8),(14,8),(34,8),(44,8),(44,18),(44,30),(44,40),(34,40),(14,40),(4,40),(4,30),(4,18),closed=True)
        # Four enlarged corner quadrants share explicit nodes with the note edges.
        arcs=[((14,8),(4,18)),((44,18),(34,8)),((4,30),(14,40)),((34,40),(44,30))]
        for i,(a,b) in enumerate(arcs):
            self.add_arc('corner-'+str(i),a,b,radius_x=10)
            self.relate('connect','note','corner-'+str(i))

    def build(self):
        # Corner ornaments and central circular denomination medallion.
        self.banknote()
        self.circle('medallion',24,24,6)
