"""Flattened both lobes into a horizontal open infinity stroke with balanced paired curves."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2c06654c-8d06-5a7b-95e0-7f57b63f8bac'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__loop-manual/20260928T171406Z-thuan-mac/reference/loop manual_2c06654c-8d06-5a7b-95e0-7f57b63f8bac.svg'
AUTHOR='gpt-6'
PLAN='Flattened both lobes into a horizontal open infinity stroke with balanced paired curves.'
CONSTRUCTION_REFERENCE='Lucide infinity: tangent loop curves joined by a diagonal transition; source keeps two open ends.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='loop-manual'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('loop', 'manual')

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
        self.path('loop',(20,18),[('C',(12,12),(17,14),(15,12)),('C',(4,24),(7,12),(4,17)),('C',(12,36),(4,31),(7,36)),('C',(24,24),(17,36),(21,28)),('C',(36,12),(27,20),(31,12)),('C',(44,24),(41,12),(44,17)),('C',(36,36),(44,31),(41,36)),('C',(28,30),(33,36),(31,34))])

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'The source is a horizontal open infinity loop. Its 28-unit visible height intentionally underfills HRECT_M by 2 units at top and bottom; all spacing checks pass, and the open ends remain clear.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '850e2c158a840bb9416de61f27bfdd5aa99df46bf533c1280546625d6718f48e'}
