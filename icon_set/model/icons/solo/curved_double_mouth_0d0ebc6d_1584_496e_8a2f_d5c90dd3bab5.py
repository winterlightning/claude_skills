from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0d0ebc6d-1584-496e-8a2f-d5c90dd3bab5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/cleavage_0d0ebc6d-1584-496e-8a2f-d5c90dd3bab5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-double-mouth'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('curved', 'double', 'mouth')

    def build(self):
        # Two mirrored downward bowl curves meet at central upward cusp, with upright outer ends. Shared half-ellipse radii10/14 and axis24. HRECT_M visible(2,8)-(46,40) preserves broad paired curve shape.
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
        self.add_line('left-upright',(4,10),(4,24))
        self.add_arc('left-bowl',(4,24),(24,24),radius_x=10,radius_y=14,sweep=False)
        self.add_arc('right-bowl',(24,24),(44,24),radius_x=10,radius_y=14,sweep=False)
        self.add_line('right-upright',(44,24),(44,10))
        self.add_contour('paired-curves','left-upright','left-bowl','right-bowl','right-upright')
