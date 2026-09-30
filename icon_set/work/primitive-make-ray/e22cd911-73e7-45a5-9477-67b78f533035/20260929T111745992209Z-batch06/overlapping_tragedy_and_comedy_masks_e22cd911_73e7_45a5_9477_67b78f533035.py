"""The current masks omit eyes and use tiny mouth marks. No written feedback. Enlarged the tragic foreground mask with eyes and a broad frown, keeping a curved second mask behind it. The rear facial details are occluded/simplified for legal spacing.
Construction: No useful exact Lucide match; reference composition and geometric construction.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e22cd911-73e7-45a5-9477-67b78f533035'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__overlapping-tragedy-and-comedy-masks/20260929T110914Z-thuan-mac/reference/masks theater_e22cd911-73e7-45a5-9477-67b78f533035.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'overlapping-tragedy-and-comedy-masks'
    keyshape = Keyshape.SQUARE
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

        path('front',(6,6),[('L',(32,6)),('L',(32,23)),('C',(19,37),(32,32),(25,37)),('C',(6,23),(13,37),(6,32)),('L',(6,6))],True)
        self.add_dot('eye-left',(15,15));self.add_dot('eye-right',(23,15))
        bez('frown',(16,27),((17,24),(21,24),(22,27)))
        path('back',(32,15),[('L',(42,15)),('L',(42,30)),('C',(30,42),(42,39),(38,42)),('C',(21,37),(25,42),(22,40))]);join('back','front')
