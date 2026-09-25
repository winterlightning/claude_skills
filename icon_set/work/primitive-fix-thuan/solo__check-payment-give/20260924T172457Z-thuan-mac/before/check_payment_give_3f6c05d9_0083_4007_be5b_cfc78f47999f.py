from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f6c05d9-0083-4007-be5b-cfc78f47999f'
SOURCE_PATH = 'icon_set/work/todo-references/check payment give_3f6c05d9-0083-4007-be5b-cfc78f47999f.svg'
AUTHOR = 'gpt-6'

PLAN = 'Check above a pointing hand; lower the fingertip and enlarge the gap in the occluded check edge.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/3f6c05d9-0083-4007-be5b-cfc78f47999f/20260922T222946-af8b23/result.json'

class Drawing(Solo48):
    icon_id = 'check-payment-give'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hand', 'selecting', 'bank', 'check')

    def build(self):
        # Bank check with two writing marks and amount field, selected by a hand rising into its lower edge. Check outline interrupted at finger. Square visible(4,4)-(44,44); rounded fingertip and palm are separate shared symbols.
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
        self.add_polyline('check',(12,26),(6,26),(6,6),(42,6),(42,26),(40,26))
        self.add_line('writing',(14,15),(22,15))
        self.add_line('amount',(30,15),(34,15))
        self.add_line('finger-left',(24,34),(24,28))
        self.add_arc('tip',(24,28),(32,28),radius_x=4)
        self.add_polyline('finger-right',(32,28),(32,34),(36,34),(36,36))
        self.add_arc('palm-bottom-right',(36,36),(30,42),radius_x=6)
        self.add_line('palm-bottom',(30,42),(22,42))
        self.add_arc('palm-bottom-left',(22,42),(16,36),radius_x=6)
        self.add_polyline('palm-left',(16,36),(16,34),(24,28))
        for a,b in [('finger-left','tip'),('tip','finger-right'),('finger-right','palm-bottom-right'),('palm-bottom-right','palm-bottom'),('palm-bottom','palm-bottom-left'),('palm-bottom-left','palm-left'),('palm-left','tip')]:
            self.relate('connect',a,b)
