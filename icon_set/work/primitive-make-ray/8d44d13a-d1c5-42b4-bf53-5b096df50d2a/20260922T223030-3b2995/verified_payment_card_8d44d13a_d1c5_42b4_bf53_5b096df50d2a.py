from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8d44d13a-d1c5-42b4-bf53-5b096df50d2a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/checkbook_8d44d13a-d1c5-42b4-bf53-5b096df50d2a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'verified-payment-card'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('verified', 'payment', 'card')

    def build(self):
        # Rounded payment card with a full-width top stripe, a short writing mark and lower-right check. HRECT_L ink(2,6)-(46,42) preserves wide card proportions; stripe endpoints split sidewalls.
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
        self.add_line('top',(8,8),(40,8))
        self.add_arc('tr',(40,8),(44,12),radius_x=4)
        self.add_polyline('right',(44,12),(44,16),(44,36))
        self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_line('bottom',(40,40),(8,40))
        self.add_arc('bl',(8,40),(4,36),radius_x=4)
        self.add_polyline('left',(4,36),(4,16),(4,12))
        self.add_arc('tl',(4,12),(8,8),radius_x=4)
        for a,b in [('top','tr'),('tr','right'),('right','br'),('br','bottom'),('bottom','bl'),('bl','left'),('left','tl'),('tl','top')]: self.relate('connect',a,b)
        self.add_line('stripe',(4,16),(44,16))
        self.relate('connect','stripe','left')
        self.relate('connect','stripe','right')
        self.add_line('writing',(13,26),(16,26))
        self.add_polyline('check',(25,27),(29,31),(35,24))
