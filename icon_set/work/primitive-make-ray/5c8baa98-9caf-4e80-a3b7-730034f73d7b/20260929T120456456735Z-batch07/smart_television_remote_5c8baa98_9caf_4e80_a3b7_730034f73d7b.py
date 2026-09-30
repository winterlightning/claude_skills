"""The current remote omits a lower button and compresses the rocker. No written feedback. Restored all four button positions and a longer volume rocker inside a rounded shell; the divider and tiny label are omitted to preserve control spacing.
Construction: No useful local remote match; rounded enclosure and equal button spacing from the supplied reference.
Plan: VRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5c8baa98-9caf-4e80-a3b7-730034f73d7b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smart-television-remote/20260929T115249Z-thuan-mac/reference/modern tv remote smart_5c8baa98-9caf-4e80-a3b7-730034f73d7b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smart-television-remote'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smart', 'television', 'remote')
    
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

        rect('shell',8,4,32,40,6)
        for j,(x,y) in enumerate(((18,15),(30,15),(18,27),(18,35))):self.add_dot('button'+str(j),(x,y))
        line('rocker',(30,27),(30,35))
