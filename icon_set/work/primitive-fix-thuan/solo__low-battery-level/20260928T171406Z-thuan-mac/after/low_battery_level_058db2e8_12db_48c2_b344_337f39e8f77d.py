"""Made the body shallower, rounded its terminal transitions and retained one clear left-side charge mark."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='058db2e8-12db-48c2-b344-337f39e8f77d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__low-battery-level/20260928T171406Z-thuan-mac/reference/charging battery low_058db2e8-12db-48c2-b344-337f39e8f77d.svg'
AUTHOR='gpt-6'
PLAN='Made the body shallower, rounded its terminal transitions and retained one clear left-side charge mark.'
CONSTRUCTION_REFERENCE='Lucide battery-low: rounded outline and minimal left charge indicator.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='low-battery-level'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('low', 'battery', 'level')

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

        self.add_line('charge',(12,20),(12,28))

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'Keep the wide low-battery silhouette and one left charge mark. The shallow envelope and 2-unit interior vertical clearance preserve the reference proportions and stay visibly open.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '316c65978be39345c362cd0d63335a395df884f06da76adf980f6d947e80cc0b'}
