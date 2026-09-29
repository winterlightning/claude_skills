"""Narrowed the handset to VRECT_M, made every corner a tangent 4-unit quarter circle and centered its original screen/hardware marks."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b4668e9a-a445-4547-ab4c-3cab57aef111'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__mobile-phone-control-pause/20260928T165643Z-thuan-mac/reference/mobile phone control pause_b4668e9a-a445-4547-ab4c-3cab57aef111.svg'
AUTHOR='gpt-6'
PLAN='Narrowed the handset to VRECT_M, made every corner a tangent 4-unit quarter circle and centered its original screen/hardware marks.'
CONSTRUCTION_REFERENCE='Lucide smartphone: shared rounded frame, balanced interior and minimal hardware marks.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='mobile-phone-control-pause'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('mobile', 'phone', 'control', 'pause')

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
        for x in (20,28):self.add_line(f'pause-{x}',(x,16),(x,26))
