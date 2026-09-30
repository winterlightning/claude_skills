"""The current microphone capsule is broad and squat with a large foot. No written feedback. Restored a taller capsule, two spaced grille rows, a centered thin stem and a shorter base.
Construction: Lucide mic: long capsule and centered supporting stem; supplied reference owns the grille and foot.
Plan: VRECT_M SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '40a82f8e-607c-4a5c-9bd8-2c7172dbb654'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-studio-microphone/20260929T115249Z-thuan-mac/reference/microphone podcast on air_40a82f8e-607c-4a5c-9bd8-2c7172dbb654.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'standing-studio-microphone'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'studio', 'microphone')
    
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*ps,closed=False): self.add_polyline(n,*ps,closed=closed)
        def bez(n,a,*ss): self.add_bezier(n,a,*ss)
        def arc(n,a,b,rx,ry=None,s=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=s)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'a',n+'b',closed=True)
        def path(n,a,commands,closed=False):
            members=[]
            for j,c in enumerate(commands):
                k,b,*args=c; name=n+str(j)
                if k=='L': line(name,a,b)
                elif k=='A': arc(name,a,b,*args)
                elif k=='C': bez(name,a,(args[0],args[1],b))
                members.append(name);a=b
            self.add_contour(n,*members,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r),('L',(x+r,y+h)),('A',(x,y+h-r),r),('L',(x,y+r)),('A',(x+r,y),r)],True)
        def join(*ns): self.relate('connect',*ns)

        path('capsule',(14,14),[('A',(24,4),10),('A',(34,14),10),('L',(34,24)),('A',(24,34),10),('A',(14,24),10),('L',(14,14))],True)
        for y in (14,24):
         line('left'+str(y),(14,y),(20,y));line('right'+str(y),(28,y),(34,y));join('left'+str(y),'capsule');join('right'+str(y),'capsule')
        line('stem',(24,34),(24,44));poly('foot',(10,44),(24,44),(38,44));join('stem','capsule','foot')
