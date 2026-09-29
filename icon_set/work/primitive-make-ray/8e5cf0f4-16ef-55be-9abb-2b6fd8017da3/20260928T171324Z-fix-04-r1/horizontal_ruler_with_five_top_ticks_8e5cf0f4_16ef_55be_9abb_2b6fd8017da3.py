"""Restored a shallow rounded ruler and all five equally spaced top graduations."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='8e5cf0f4-16ef-55be-9abb-2b6fd8017da3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__horizontal-ruler-with-five-top-ticks/20260928T171324Z-thuan-mac/reference/ruler_8e5cf0f4-16ef-55be-9abb-2b6fd8017da3.svg'
AUTHOR='gpt-6'
PLAN='Restored a shallow rounded ruler and all five equally spaced top graduations.'
CONSTRUCTION_REFERENCE='Lucide ruler: repeated edge graduations and rounded case; source controls horizontal proportions.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='horizontal-ruler-with-five-top-ticks'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('horizontal', 'ruler', 'with', 'five', 'top', 'ticks')

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
        top,bottom=17,31
        self.path('case',(7,top),[('L',(10,top)),('L',(17,top)),('L',(24,top)),('L',(31,top)),('L',(38,top)),('L',(41,top)),('A',(44,20),3,3,True),('L',(44,28)),('A',(41,bottom),3,3,True),('L',(7,bottom)),('A',(4,28),3,3,True),('L',(4,20)),('A',(7,top),3,3,True)],True)
        for j in range(5):
            x=10+7*j;self.add_line(f'tick-{j}',(x,top),(x,23));self.relate('connect','case',f'tick-{j}')

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'Preserve the original shallow ruler proportions and all five ticks. The 18-unit visible height and 2–3-unit visible tick gaps remain clear; a standard tall envelope would recreate the rejected slab shape.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '3ac2d41cd5f5ae10a81bb9ff6e9c223b15070cd3d950901a751dabe3ea5229f3'}
