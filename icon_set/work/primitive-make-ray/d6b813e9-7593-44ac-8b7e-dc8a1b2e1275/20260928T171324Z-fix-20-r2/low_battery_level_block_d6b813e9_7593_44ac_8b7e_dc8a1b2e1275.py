"""Restored the outlined low-charge block, a shallower case and a separately outlined rounded terminal."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d6b813e9-7593-44ac-8b7e-dc8a1b2e1275'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__low-battery-level-block/20260928T171406Z-thuan-mac/reference/charging battery low_d6b813e9-7593-44ac-8b7e-dc8a1b2e1275.svg'
AUTHOR='gpt-6'
PLAN='Restored the outlined low-charge block, a shallower case and a separately outlined rounded terminal.'
CONSTRUCTION_REFERENCE='Lucide battery-low: rounded case; supplied source specifically requires an outlined charge block.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='low-battery-level-block'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('low', 'battery', 'level', 'block')

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

        self.path('case',(8,12),[('L',(32,12)),('A',(36,16),4,4,True),('L',(36,20)),('L',(36,28)),('L',(36,32)),('A',(32,36),4,4,True),('L',(8,36)),('A',(4,32),4,4,True),('L',(4,16)),('A',(8,12),4,4,True)],True)
        self.path('terminal',(36,20),[('L',(42,20)),('A',(44,22),2,2,True),('L',(44,26)),('A',(42,28),2,2,True),('L',(36,28))])
        self.relate('connect','case','terminal')
        self.add_polyline('charge',(12,18),(18,18),(18,30),(12,30),closed=True)


    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'Preserve a tall outlined low-charge block rather than collapse it to the rejected single stroke. Its 2-unit inner opening and case clearance remain legible; the body is intentionally shallower than HRECT_M.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'ad5df11db0bfa67a805c28c4cdd502ea60be527687e5a599345ad3d1d50cd01c'}
