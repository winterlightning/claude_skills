from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1ccecf6e-60d8-417b-accc-4a89121dd0ab'
SOURCE_PATH = 'icon_set/work/todo-references/business contract approve_1ccecf6e-60d8-417b-accc-4a89121dd0ab.svg'
AUTHOR = 'gpt-6'

PLAN = 'Approved contract held in two hands; enlarge the sheet and separate text rows; circular approval seal retained.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/1ccecf6e-60d8-417b-accc-4a89121dd0ab/20260922T222001-63ce6a/result.json'

class Drawing(Solo48):
    icon_id = 'business-contract-approve'
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
        self.add_polyline('paper',(26,44),(14,44),(14,36),(14,4),(38,4),(38,28))
        self.add_polyline('left-hand',(8,6),(8,28),(14,36))
        self.relate('connect','left-hand','paper')
        circle('seal',26,15,7)
        self.add_polyline('check',(23,15),(25,17),(29,13))
        self.add_line('text',(22,27),(28,27))
        self.add_line('text-lower',(22,35),(24,35))
        self.add_polyline('right-hand',(40,44),(38,34),(30,26))
        self.add_arc('thumb',(30,26),(26,30),radius_x=3,sweep=False)
        self.add_polyline('palm',(26,30),(32,36),(32,44))
        self.relate('connect','right-hand','thumb')
        self.relate('connect','thumb','palm')
        
