"""The rejected alpaca is angular and reads like a blocky dog. No written feedback. Rebuilt a taller neck, rounded muzzle, upright ear and softer back and haunch while preserving two visible legs; tiny eye and far legs are omitted.
Construction: Source defines long neck and standing profile; no useful local alpaca body match.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '09625729-d47a-4fde-a9a2-61e0c7cfe86e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-alpaca-in-profile/20260929T115249Z-thuan-mac/reference/alpaca_09625729-d47a-4fde-a9a2-61e0c7cfe86e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'standing-alpaca-in-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'alpaca', 'in', 'profile')
    
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

        path('alpaca',(6,28),[('C',(12,22),(6,24),(8,22)),('L',(25,22)),('L',(25,13)),('C',(29,10),(25,11),(27,10)),('L',(29,6)),('L',(32,12)),('C',(36,14),(34,12),(36,12)),('L',(39,14)),('C',(42,18),(42,14),(42,16)),('C',(38,22),(42,21),(40,22)),('L',(35,22)),('L',(37,42)),('L',(28,42)),('L',(27,32)),('L',(18,32)),('L',(15,42)),('L',(6,42)),('L',(8,33)),('C',(6,28),(6,32),(6,30))],True)
