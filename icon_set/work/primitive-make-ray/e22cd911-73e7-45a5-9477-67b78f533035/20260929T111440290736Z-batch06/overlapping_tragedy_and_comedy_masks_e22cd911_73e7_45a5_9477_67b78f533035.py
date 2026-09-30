"""The rejected masks have no eyes and tiny mouth marks, so they read as bowls. No written feedback. Restored eyes and broad opposing mouth curves on overlapping theatrical faces.
Construction: No useful exact Lucide match; reference composition and geometric construction.
Plan: HRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e22cd911-73e7-45a5-9477-67b78f533035'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__overlapping-tragedy-and-comedy-masks/20260929T110914Z-thuan-mac/reference/masks theater_e22cd911-73e7-45a5-9477-67b78f533035.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'overlapping-tragedy-and-comedy-masks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('overlapping', 'tragedy', 'and', 'comedy', 'masks')
    
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

        path('front',(4,8),[('L',(28,8)),('L',(28,22)),('C',(16,34),(28,30),(22,34)),('C',(4,22),(10,34),(4,30)),('L',(4,8))],True)
        self.add_dot('eye-left',(12,17));self.add_dot('eye-right',(20,17))
        bez('frown',(12,27),((14,23),(18,23),(20,27)))
        path('back',(28,14),[('L',(44,14)),('L',(44,28)),('C',(32,40),(44,36),(39,40)),('C',(22,33),(26,40),(23,36))]);join('back','front')
        self.add_dot('rear-eye',(36,23))
        bez('smile',(31,31),((33,34),(35,34),(37,31)))
