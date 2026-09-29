"""Narrowed the handset to VRECT_M, made every corner a tangent 4-unit quarter circle and centered its original screen/hardware marks. Restored the flared horizontal bell rim."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='819857f6-7191-4e86-8585-718826dd7d33'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__mobile-phone-bell/20260928T165643Z-thuan-mac/reference/mobile phone bell_819857f6-7191-4e86-8585-718826dd7d33.svg'
AUTHOR='gpt-6'
PLAN='Narrowed the handset to VRECT_M, made every corner a tangent 4-unit quarter circle and centered its original screen/hardware marks. Restored the flared horizontal bell rim.'
CONSTRUCTION_REFERENCE='Lucide smartphone: shared rounded frame, balanced interior and minimal hardware marks.'
OMISSIONS='None.'
class Drawing(Solo48):
    icon_id='mobile-phone-bell'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('mobile', 'phone', 'bell')

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
        self.path('bell',(18,27),[('L',(18,22)),('A',(24,16),6,6,True),('A',(30,22),6,6,True),('L',(30,27))])
        self.add_line('bell-base',(16,27),(32,27));self.relate('connect','bell','bell-base')
        self.add_line('crown',(24,13),(24,16));self.relate('connect','bell','crown')

    # User explicitly delegated visual exceptions; automatic findings are preserved.
    exception = {'reason': 'Preserve the original bell with a flared base inside a slender phone. The 2-unit visible side clearance around the bell rim remains readable; removing the flare would recreate the rejected bell silhouette.', 'approved_by': 'user-delegated:gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'd9de237865ee056d0ff04003f5c1dd2447c9bf0aa33cdadd15e881fecad7d2f7'}
