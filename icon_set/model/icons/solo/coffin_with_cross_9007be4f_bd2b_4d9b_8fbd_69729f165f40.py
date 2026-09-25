from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9007be4f-bd2b-4d9b-8fbd-69729f165f40'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/casket_9007be4f-bd2b-4d9b-8fbd-69729f165f40.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'coffin-with-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('coffin', 'with', 'cross')

    def build(self):
        # Symmetric six-sided coffin with centered cross. Mirror axis24; VRECT_L extremes x8/40 and y4/44 preserve tall tapered proportions. Cross halves share exact junction(24,20).
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
        axis=24
        self.add_polyline('coffin',(16,4),(32,4),(40,16),(32,44),(16,44),(8,16),closed=True)
        self.add_polyline('vertical',(axis,14),(axis,20),(axis,30))
        self.add_polyline('horizontal',(18,20),(axis,20),(30,20))
        self.relate('connect','vertical','horizontal')
