from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1ccecf6e-60d8-417b-accc-4a89121dd0ab'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/business contract approve_1ccecf6e-60d8-417b-accc-4a89121dd0ab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-signing-approved-contract'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hand', 'signing', 'approved', 'contract')

    def build(self):
        # Approved contract sheet with circular check seal and a wrapping hand on each side. VRECT_L visible (6,2)-(42,46) accommodates upright sheet; right thumb deliberately overlaps paper edge.
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
        self.add_polyline('paper',(26,44),(16,44),(16,36),(16,4),(36,4),(36,30))
        self.add_polyline('left-hand',(8,6),(8,28),(16,36))
        self.relate('connect','left-hand','paper')
        circle('seal',26,15,6)
        self.add_polyline('check',(23,15),(25,17),(29,13))
        self.add_line('text',(23,27),(28,27))
        self.add_polyline('right-hand',(40,44),(38,34),(30,26))
        self.add_arc('thumb',(30,26),(26,30),radius_x=3,sweep=False)
        self.add_polyline('palm',(26,30),(32,36),(32,44))
        self.relate('connect','right-hand','thumb')
        self.relate('connect','thumb','palm')
        
