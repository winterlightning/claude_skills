"""Extended the three tines and smoothed the bowl; retained the diagonal oval spoon."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='53cd4f82-ae5a-4f7a-8ddd-de64747944f4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__crossed-fork-with-spoon/20260928T165643Z-thuan-mac/reference/symbol spoon cross fork_53cd4f82-ae5a-4f7a-8ddd-de64747944f4.svg'
AUTHOR='gpt-6'
PLAN='Extended the three tines and smoothed the bowl; retained the diagonal oval spoon.'
CONSTRUCTION_REFERENCE='Lucide utensils-crossed: parallel tines and coherent bowl; supplied reference: spoon oval.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='crossed-fork-with-spoon'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('crossed', 'fork', 'with', 'spoon')

    def path(self,n,start,commands,closed=False):
        here=start; ids=[]
        for i,(kind,end,*a) in enumerate(commands):
            ident=f'{n}-{i}';ids.append(ident)
            if kind=='L': self.add_line(ident,here,end)
            elif kind=='A': self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C': self.add_bezier(ident,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self,band=True):
        # Shared outline owns width, corner radius and band attachment nodes.
        l,r,t,b,k,y=10,38,4,44,4,36
        self.path('phone',(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,y)),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,y)),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        if band:
            self.add_line('band',(l,y),(r,y));self.relate('connect','phone','band')

    def build(self):
        # Three long, parallel teeth share a smooth U bowl and a diagonal handle.
        self.path('fork-head',(6,16),[('L',(12,22)),('C',(20,20),(15,25),(18,22)),('C',(22,12),(22,18),(25,15)),('L',(16,6))])
        self.add_line('fork-middle',(11,11),(20,20))
        self.add_polyline('fork-handle',(20,20),(25,25),(42,42))
        self.relate('connect','fork-head','fork-middle')
        self.relate('connect','fork-head','fork-handle')
        self.relate('connect','fork-middle','fork-handle')

        self.path('spoon-bowl',(32,18),[('C',(37,6),(28,14),(32,6)),('C',(42,11),(40,6),(42,8)),('C',(32,18),(42,17),(36,22))],True)
        self.add_polyline('spoon-handle',(6,42),(25,25),(32,18))
        self.relate('connect','spoon-handle','spoon-bowl')
        self.relate('connect','spoon-handle','fork-handle')


    # User explicitly delegated visual exceptions; automatic findings are preserved.
    exception = {'reason': 'The fork needs three long tines and a clear U bowl. Approximately 3-unit gaps preserve the fork and the diagonal oval spoon; the spoon was moved away from the fork to remove the earlier narrow wedge.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'b2605fd31af7ed7f728b7e6d69caf3cb8db0649b0ef3742ac37890b60d9a40ad'}
