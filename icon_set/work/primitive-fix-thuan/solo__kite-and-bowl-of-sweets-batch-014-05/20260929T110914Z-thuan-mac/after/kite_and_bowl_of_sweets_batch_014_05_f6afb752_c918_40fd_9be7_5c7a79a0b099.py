"""The rejected bowl has only one undifferentiated semicircle and an overlarge diamond. No written feedback. Restored distinct sweet lobes, a shallow bowl and tapered kite; omitted the third sweet and spars for spacing.
Construction: No useful exact Lucide match; reference composition and geometric construction.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f6afb752-c918-40fd-9be7-5c7a79a0b099'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kite-and-bowl-of-sweets-batch-014-05/20260929T110914Z-thuan-mac/reference/makara sankranti_f6afb752-c918-40fd-9be7-5c7a79a0b099.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'kite-and-bowl-of-sweets-batch-014-05'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('kite', 'and', 'bowl', 'of', 'sweets', 'batch', '014', '05')
    
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

        poly('kite',(33,6),(42,14),(34,25),(25,14),closed=True)
        bez('tail',(34,25),((34,33),(42,35),(42,42)));join('kite','tail')
        path('sweets',(6,33),[('C',(11,26),(6,27),(8,25)),('C',(20,26),(11,20),(20,20)),('C',(26,33),(23,25),(26,27))])
        line('rim',(6,33),(26,33))
        path('bowl',(26,33),[('C',(20,42),(25,39),(24,42)),('L',(12,42)),('C',(6,33),(8,42),(7,39))]);join('rim','bowl','sweets')
