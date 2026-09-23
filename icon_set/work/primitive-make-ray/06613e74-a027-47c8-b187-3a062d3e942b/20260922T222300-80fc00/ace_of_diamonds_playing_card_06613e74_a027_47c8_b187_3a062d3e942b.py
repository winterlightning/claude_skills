from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '06613e74-a027-47c8-b187-3a062d3e942b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/card game diamond_06613e74-a027-47c8-b187-3a062d3e942b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ace-of-diamonds-playing-card'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('ace', 'of', 'diamonds', 'playing', 'card')

    def build(self):
        # Upright rounded card with a large centered diamond and matching small corner diamonds. VRECT_L ink (6,2)-(42,46). Diamond instances share shape but use distinct center/radius parameters.
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
        rounded('card',8,4,40,44,4)
        for n,x,y,rx,ry in [('main',24,24,7,9),('upper',16,12,3,4),('lower',32,36,3,4)]:
            self.add_polyline(n,(x,y-ry),(x+rx,y),(x,y+ry),(x-rx,y),closed=True)
