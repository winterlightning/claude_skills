from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b34dc81-b846-4bb2-ab08-2edb491e7e4a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/carport_5b34dc81-b846-4bb2-ab08-2edb491e7e4a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'car-parked-in-garage'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('car', 'parked', 'in', 'garage')

    def build(self):
        # Symmetric gabled garage enclosing a front-view car. Roof owns posts at6/42; car owns trapezoid windshield, body and short attached wheels. Square ink(4,4)-(44,44).
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
        self.add_polyline('roof',(6,16),(24,6),(42,16),(6,16))
        self.add_line('post-left',(6,16),(6,42))
        self.add_line('post-right',(42,16),(42,42))
        self.relate('connect','roof','post-left')
        self.relate('connect','roof','post-right')
        self.add_polyline('body',(14,32),(34,32),(34,40),(30,40),(18,40),(14,40),closed=True)
        self.add_polyline('windshield',(14,32),(18,24),(30,24),(34,32))
        self.relate('connect','body','windshield')
        for n,x in [('left',18),('right',30)]:
            self.add_line('wheel-'+n,(x,40),(x,42))
            self.relate('connect','body','wheel-'+n)
