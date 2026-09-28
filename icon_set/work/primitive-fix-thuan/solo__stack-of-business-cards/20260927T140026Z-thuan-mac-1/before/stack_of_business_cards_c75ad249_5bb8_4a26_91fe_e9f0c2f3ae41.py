from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c75ad249-5bb8-4a26-91fe-e9f0c2f3ae41'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/business card stack 1_c75ad249-5bb8-4a26-91fe-e9f0c2f3ae41.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stack-of-business-cards'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('stack', 'of', 'business', 'cards')

    def build(self):
        # Stack reduced to two cards so the front diamond has legal clearance. Rear upper edge and front rounded rectangle. VRECT_L ink (6,2)-(42,46) gives diamond vertical room; centered diamond uses shared radius6.
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
        self.add_line('rear-card',(16,4),(40,4))
        rounded('front-card',8,14,40,44,4)
        x,y,r=24,29,6
        self.add_polyline('diamond',(x,y-r),(x+r,y),(x,y+r),(x-r,y),closed=True)
