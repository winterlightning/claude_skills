from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '51de7530-e4b9-4207-92df-6b4ec157c6a4'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/card game cards spade diamond_51de7530-e4b9-4207-92df-6b4ec157c6a4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spade-and-diamond-playing-cards'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('spade', 'and', 'diamond', 'playing', 'cards')

    def build(self):
        # Overlapping playing cards carry separate spade and diamond suits. Front card and rear card are distinct composite symbols; rear outline is interrupted behind the front. Square ink (4,4)-(44,44); overlap is deliberately asymmetric.
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
        rounded('front',6,6,28,36,3)
        self.add_polyline('rear',(28,14),(42,18),(34,42),(18,38),(18,36))
        self.relate('connect','front','rear')
        self.add_line('spade-left',(17,14),(11,22))
        self.add_arc('lobe-left',(11,22),(17,24),radius_x=4,sweep=False)
        self.add_arc('lobe-right',(17,24),(23,22),radius_x=4,sweep=False)
        self.add_line('spade-right',(23,22),(17,14))
        self.add_contour('spade','spade-left','lobe-left','lobe-right','spade-right',closed=True)
        self.add_line('stem',(17,24),(17,29))
        self.relate('connect','spade','stem')
        self.add_polyline('diamond',(28,22),(35,27),(31,34),(28,32))
