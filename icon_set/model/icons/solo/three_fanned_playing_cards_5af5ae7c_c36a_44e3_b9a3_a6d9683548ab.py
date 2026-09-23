from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5af5ae7c-c36a-44e3-b9a3-a6d9683548ab'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/card game cards_5af5ae7c-c36a-44e3-b9a3-a6d9683548ab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-fanned-playing-cards'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('three', 'fanned', 'playing', 'cards')

    def build(self):
        # Three layered cards with front diamond. Front rectangle owns a centered radius6 diamond; rear cards expose top and left edges. Square ink extremes (4,4)-(44,44). Spacing requires reducing the fan angles.
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
        self.add_polyline('front',(14,14),(18,14),(38,14),(42,14),(42,42),(14,42),(14,38),(14,18),closed=True)
        self.add_polyline('upper-card',(18,14),(18,6),(38,6),(38,14))
        self.add_polyline('left-card',(14,18),(6,18),(6,38),(14,38))
        self.relate('connect','front','upper-card')
        self.relate('connect','front','left-card')
        x,y,r=28,28,6
        self.add_polyline('diamond',(x,y-r),(x+r,y),(x,y+r),(x-r,y),closed=True)
