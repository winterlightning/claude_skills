from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51de7530-e4b9-4207-92df-6b4ec157c6a4'
SOURCE_PATH = 'icon_set/work/todo-references/card game cards spade diamond_51de7530-e4b9-4207-92df-6b4ec157c6a4.svg'
AUTHOR = 'gpt-6'

PLAN = 'Overlapping spade and diamond cards; widen the front card and rebalance its spade inside the available opening.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/51de7530-e4b9-4207-92df-6b4ec157c6a4/20260922T222142-4b1b0a/result.json'

class Drawing(Solo48):
    icon_id = 'card-game-cards-spade-diamond'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
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
        rounded('front',6,6,32,36,3)
        self.add_polyline('rear',(32,14),(42,18),(34,42),(18,38),(18,36))
        self.relate('connect','front','rear')
        self.add_line('spade-left',(19,15),(15,22))
        self.add_arc('lobe-left',(15,22),(19,23),radius_x=3,sweep=False)
        self.add_arc('lobe-right',(19,23),(23,22),radius_x=3,sweep=False)
        self.add_line('spade-right',(23,22),(19,15))
        self.add_contour('spade','spade-left','lobe-left','lobe-right','spade-right',closed=True)
        self.add_line('stem',(19,23),(19,27))
        self.relate('connect','spade','stem')
        self.add_polyline('diamond',(32,22),(37,27),(33,34),(32,32))
        self.relate('connect','diamond','front')
