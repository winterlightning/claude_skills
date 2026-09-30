"""The rejected hawk loses the folded wing and reads as a thin generic bird. No written feedback. Broadened the chest and tail, restored a short folded-wing contour, and kept the hooked beak and perch foot.
Construction: Lucide bird: folded wing, hooked head and simple attached feet.
Plan: VRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '70d3ecde-a67d-4049-8f4c-451837cbd344'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__perched-hawk-profile/20260929T110914Z-thuan-mac/reference/hawk_70d3ecde-a67d-4049-8f4c-451837cbd344.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'perched-hawk-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('perched', 'hawk', 'profile')
    
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

        path('outline',(8,37),[('C',(21,14),(12,28),(21,23)),('C',(31,4),(21,7),(25,4)),('C',(40,14),(37,4),(40,8)),('L',(34,12)),('C',(29,34),(34,23),(36,30)),('C',(8,37),(23,39),(13,39))],True)
        bez('wing',(23,18),((28,21),(25,28),(18,31)))
        poly('leg',(27,36),(29,44),(37,44));join('leg','outline')
