"""Restored the lower band, narrowed the handset and rebuilt diagonal open wrench jaws."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='05e2ce47-0cc9-49ed-8c9a-44eadff51505'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__mobile-phone-wrench/20260928T171324Z-thuan-mac/reference/mobile phone wrench_05e2ce47-0cc9-49ed-8c9a-44eadff51505.svg'
AUTHOR='gpt-6'
PLAN='Restored the lower band, narrowed the handset and rebuilt diagonal open wrench jaws.'
CONSTRUCTION_REFERENCE='Lucide smartphone: matched rounded frame; wrench: diagonal shaft and coherent open jaws.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='mobile-phone-wrench'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('mobile', 'phone', 'wrench')

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
        self.phone(True)
        self.path('jaw-bottom',(16,25),[('C',(22,25),(17,23),(20,23)),('C',(22,30),(24,27),(24,29))])
        self.path('jaw-top',(28,12),[('C',(26,18),(25,12),(23,16)),('C',(32,15),(29,20),(32,18))])
        self.add_line('shaft',(22,25),(26,18))
        self.relate('connect','shaft','jaw-bottom');self.relate('connect','shaft','jaw-top')

    # User delegated visual exceptions; original automatic findings remain recorded.
    exception = {'reason': 'Retain both diagonal open wrench jaws and the phone lower band. The lower jaw has 2-unit visible side clearance within the slender handset, and remains separated at native size in both themes.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'e44890870881dec1fd40bbb2dd5d85c1bee526e5fd47e0e2ab7b51f76213a0f1'}
