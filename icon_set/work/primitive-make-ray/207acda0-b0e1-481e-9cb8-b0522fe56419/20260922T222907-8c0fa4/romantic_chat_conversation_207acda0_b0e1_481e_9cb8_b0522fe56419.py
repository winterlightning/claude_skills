from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '207acda0-b0e1-481e-9cb8-b0522fe56419'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/chat conversation love romance talk_207acda0-b0e1-481e-9cb8-b0522fe56419.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'romantic-chat-conversation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('romantic', 'chat', 'conversation')

    def build(self):
        # Two overlapping speech bubbles, foreground carrying a heart. Front/right and rear/left tails keep conversation arrangement. Square ink(4,4)-(44,44). Heart lobes share radius3 around axis29.
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
        self.add_polyline('rear',(30,16),(30,6),(6,6),(6,24),(12,24),(12,32),(18,26))
        self.add_polyline('front',(18,16),(42,16),(42,34),(36,34),(36,42),(28,34),(18,34),closed=True)
        self.relate('connect','front','rear')
        self.add_arc('heart-left',(23,23),(29,23),radius_x=3)
        self.add_arc('heart-right',(29,23),(35,23),radius_x=3)
        self.add_line('heart-a',(35,23),(29,30))
        self.add_line('heart-b',(29,30),(23,23))
        self.add_contour('heart','heart-left','heart-right','heart-a','heart-b',closed=True)
