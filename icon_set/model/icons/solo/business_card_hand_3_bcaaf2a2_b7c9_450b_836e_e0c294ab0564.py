from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bcaaf2a2-b7c9-450b-836e-e0c294ab0564'
SOURCE_PATH = 'icon_set/work/todo-references/business card hand 3_bcaaf2a2-b7c9-450b-836e-e0c294ab0564.svg'
AUTHOR = 'gpt-6'

PLAN = 'Hand holding a portrait business card; flatten the upper hand clearance and shorten the shoulder bowl while retaining the portrait.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/bcaaf2a2-b7c9-450b-836e-e0c294ab0564/20260922T221840-dd88b8/result.json'

class Drawing(Solo48):
    icon_id = 'business-card-hand-3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('hand', 'holding', 'business', 'card')

    def build(self):
        # Business card rectangle interrupted by a right-hand grip, with a detached portrait inside and a rising back-of-hand outline. Square visible extremes (4,4)-(44,44). Portrait head r3 bottom26, shoulders34: exact 4 ink gap.
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
        self.add_polyline('card',(34,22),(34,14),(6,14),(6,42),(34,42),(34,34))
        self.add_bezier('hand-back',(24,6),((30,6),(36,6),(42,6)))
        self.add_line('thumb-top',(42,22),(30,22))
        self.add_arc('thumb-tip',(30,22),(30,34),radius_x=6,sweep=False)
        self.add_line('thumb-bottom',(30,34),(42,34))
        self.add_contour('thumb','thumb-top','thumb-tip','thumb-bottom')
        self.relate('connect','card','thumb')
        circle('head',16,23,3)
        self.add_arc('shoulders',(12,37),(20,37),radius_x=4,radius_y=3,sweep=True)
