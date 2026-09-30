"""The rejected version is an ordinary wrench and drops the lightning-shaped lower edge in the original. No written feedback. Restored the open lightning stroke below the wrench jaw and the rounded left handle end.
Construction: Lucide wrench: round shoulder and purposeful open jaw; reference supplies lightning.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8b71e7e7-15cf-4d31-8c76-295ef5576f53'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-end-wrench-batch-04-v2/20260929T110914Z-thuan-mac/reference/flash wrench_8b71e7e7-15cf-4d31-8c76-295ef5576f53.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'open-end-wrench-batch-04-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'end', 'wrench', 'batch', '04', 'v2')
    
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

        path('wrench',(13,42),[('A',(6,35),7),('C',(9,30),(6,33),(7,31)),('L',(20,20)),('C',(30,6),(17,12),(22,6)),('L',(24,14)),('L',(32,22)),('L',(42,12)),('C',(35,27),(42,21),(40,26))])
        poly('lightning',(35,27),(20,35),(38,35),(29,42));join('wrench','lightning')
