from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9c1cbac-5439-4b45-98c2-03e923e14b07'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_10/cell border right_b9c1cbac-5439-4b45-98c2-03e923e14b07.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-section-grid-layout'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'section', 'grid', 'layout')

    def build(self):
        # Rounded square split into two left cells and one full-height right cell. Shared axis24 and radius4. Boundary segments split at each T-junction; visible(4,4)-(44,44).
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
        parts=[
        ('t1',(10,6),(24,6)),('t2',(24,6),(38,6)),
        ('r',(42,10),(42,38)),('b1',(38,42),(24,42)),('b2',(24,42),(10,42)),
        ('l1',(6,38),(6,24)),('l2',(6,24),(6,10))]
        for n,a,b in parts:self.add_line(n,a,b)
        for n,a,b in [('tr',(38,6),(42,10)),('br',(42,38),(38,42)),('bl',(10,42),(6,38)),('tl',(6,10),(10,6))]:
            self.add_arc(n,a,b,radius_x=4)
        self.add_contour('frame','t1','t2','tr','r','br','b1','b2','bl','l1','l2','tl',closed=True)
        self.add_polyline('vertical',(24,6),(24,24),(24,42))
        self.add_line('horizontal',(6,24),(24,24))
        self.relate('connect','frame','vertical')
        self.relate('connect','frame','horizontal')
        self.relate('connect','vertical','horizontal')
