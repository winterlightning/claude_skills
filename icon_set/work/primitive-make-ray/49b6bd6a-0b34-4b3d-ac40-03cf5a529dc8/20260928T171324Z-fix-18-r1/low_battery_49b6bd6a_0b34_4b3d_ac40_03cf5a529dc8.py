"""Restored a wider battery silhouette, integrated rounded terminal and two compact left-aligned charge marks."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='49b6bd6a-0b34-4b3d-ac40-03cf5a529dc8'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__low-battery/20260928T171406Z-thuan-mac/reference/charging battery low_49b6bd6a-0b34-4b3d-ac40-03cf5a529dc8.svg'
AUTHOR='gpt-6'
PLAN='Restored a wider battery silhouette, integrated rounded terminal and two compact left-aligned charge marks.'
CONSTRUCTION_REFERENCE='Lucide battery-low: rounded body and left charge mark; source: two marks and integrated terminal.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='low-battery'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('low', 'battery')

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
        self.path('case',(8,14),[('L',(34,14)),('A',(38,18),4,4,True),('L',(38,20)),('L',(42,20)),('A',(44,22),2,2,True),('L',(44,26)),('A',(42,28),2,2,True),('L',(38,28)),('L',(38,30)),('A',(34,34),4,4,True),('L',(8,34)),('A',(4,30),4,4,True),('L',(4,18)),('A',(8,14),4,4,True)],True)

        for x in (12,20):self.add_line(f'charge-{x}',(x,20),(x,28))

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'Retain the wider battery proportion and two left-aligned charge marks. The shallow envelope and 2-unit top/bottom interior gaps remain readable at 48 px, preserving the source charge count.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'f642ecebab71b7ade226abd98c9c51fd9971b2bffca5d13e42dde99867dbfde9'}
