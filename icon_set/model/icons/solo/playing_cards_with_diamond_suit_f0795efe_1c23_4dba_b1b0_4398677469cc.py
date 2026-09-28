from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0795efe-1c23-4dba-b1b0-4398677469cc'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/cards_f0795efe-1c23-4dba-b1b0-4398677469cc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'playing-cards-with-diamond-suit'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('playing', 'cards', 'with', 'diamond', 'suit')

    def build(self):
        # Two overlapping cards, front with centered diamond. Exposed back edge wraps top and left; card corners use round stroke joins. SQUARE ink (4,4)-(44,44). Eight-unit offset and diamond half-diagonal6 derive clean spacing.
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def rect(n,l,t,r,b):
            self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        def rounded(n,l,t,r,b,k):
            self.add_line(n+'-t',(l+k,t),(r-k,t))
            self.add_arc(n+'-tr',(r-k,t),(r,t+k),radius_x=k)
            self.add_line(n+'-r',(r,t+k),(r,b-k))
            self.add_arc(n+'-br',(r,b-k),(r-k,b),radius_x=k)
            self.add_line(n+'-b',(r-k,b),(l+k,b))
            self.add_arc(n+'-bl',(l+k,b),(l,b-k),radius_x=k)
            self.add_line(n+'-l',(l,b-k),(l,t+k))
            self.add_arc(n+'-tl',(l,t+k),(l+k,t),radius_x=k)
            self.add_contour(n,*[n+'-'+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)
        self.add_polyline('front',(14,14),(34,14),(42,14),(42,42),(14,42),(14,34),closed=True)
        self.add_polyline('rear',(14,34),(6,34),(6,6),(34,6),(34,14))
        self.relate('connect','rear','front')
        x,y,r=28,28,6
        self.add_polyline('diamond',(x,y-r),(x+r,y),(x,y+r),(x-r,y),closed=True)
