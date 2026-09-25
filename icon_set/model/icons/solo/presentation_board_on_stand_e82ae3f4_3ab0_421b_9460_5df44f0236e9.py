from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e82ae3f4-3ab0-421b-9460-5df44f0236e9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_09/canvas_e82ae3f4-3ab0-421b-9460-5df44f0236e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'presentation-board-on-stand-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('presentation', 'board', 'on', 'stand')

    def build(self):
        # Board enclosure on a three-legged easel. Shared attachment points split the ledge and top rail. Square extremes (4,4)-(44,44) from ledge and mast/feet.
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
        self.add_polyline('board',(10,32),(10,14),(24,14),(38,14),(38,32))
        self.add_polyline('ledge',(6,32),(10,32),(18,32),(24,32),(30,32),(38,32),(42,32))
        self.add_line('mast',(24,6),(24,14))
        self.add_line('leg-left',(18,32),(14,42))
        self.add_line('leg-center',(24,32),(24,42))
        self.add_line('leg-right',(30,32),(34,42))
        self.relate('connect','board','ledge')
        self.relate('connect','board','mast')
        for n in ['leg-left','leg-center','leg-right']:
            self.relate('connect','ledge',n)
