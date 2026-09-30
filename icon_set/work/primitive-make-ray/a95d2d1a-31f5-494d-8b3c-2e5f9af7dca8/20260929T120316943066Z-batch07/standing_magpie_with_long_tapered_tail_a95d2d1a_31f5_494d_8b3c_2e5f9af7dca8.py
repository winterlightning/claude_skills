"""The rejected magpie has a short solid tail and no eye. No written feedback. Restored an elongated outlined tapering tail, a round head with a visible eye, and a supporting bent leg; the second foot and wing seam are omitted for spacing.
Construction: Lucide bird: circular head and purposeful eye; source supplies left-facing pose and long tail.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a95d2d1a-31f5-494d-8b3c-2e5f9af7dca8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-magpie-with-long-tapered-tail/20260929T115249Z-thuan-mac/reference/magpie_a95d2d1a-31f5-494d-8b3c-2e5f9af7dca8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'standing-magpie-with-long-tapered-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'magpie', 'with', 'long', 'tapered', 'tail')
    
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

        path('bird',(6,17),[('L',(8,15)),('A',(17,6),9),('A',(26,15),9),('C',(35,30),(26,20),(32,25)),('L',(42,40)),('C',(38,42),(42,42),(40,42)),('L',(26,33)),('C',(10,20),(18,36),(10,30)),('L',(6,17))],True)
        self.add_dot('eye',(17,15))
        poly('leg',(18,33),(16,42),(10,42));join('leg','bird')
