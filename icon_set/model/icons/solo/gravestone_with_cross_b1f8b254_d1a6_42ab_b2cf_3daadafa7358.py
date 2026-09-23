from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1f8b254-d1a6-42ab-b2cf-3daadafa7358'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/cemetery_b1f8b254-d1a6-42ab-b2cf-3daadafa7358.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'gravestone-with-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('gravestone', 'with', 'cross')

    def build(self):
        # Arched gravestone on rectangular plinth, crowned by a cross and bearing a smaller cross. Shared axis24; crown radius14. VRECT_L visible(6,2)-(42,46).
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
        self.add_polyline('base',(8,36),(10,36),(38,36),(40,36),(40,44),(8,44),closed=True)
        self.add_line('left',(10,36),(10,26))
        self.add_arc('arch-left',(10,26),(24,12),radius_x=14)
        self.add_arc('arch-right',(24,12),(38,26),radius_x=14)
        self.add_line('right',(38,26),(38,36))
        self.add_contour('stone','left','arch-left','arch-right','right')
        self.relate('connect','base','stone')
        self.add_polyline('top-stem',(24,4),(24,6),(24,12))
        self.add_polyline('top-arms',(18,6),(24,6),(30,6))
        self.relate('connect','top-stem','top-arms')
        self.relate('connect','top-stem','stone')
        self.add_polyline('inner-stem',(24,22),(24,25),(24,27))
        self.add_polyline('inner-arms',(20,25),(24,25),(28,25))
        self.relate('connect','inner-stem','inner-arms')
