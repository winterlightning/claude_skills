"""The rejected glasses look like filled dots and the hair looks rectangular. No written feedback. Restored visible round lens openings, a bridge, an integrated rounded bun and a circular jaw. The small smile, ears and hair partition are omitted to keep the lenses clear.
Construction: Lucide glasses: actual round lenses and bridge. Shared human circular jaw; source supplies bun and expression.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'dec0f26b-6bfa-439d-afa0-f23e952da678'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smiling-woman-head-with-bun-and-glasses/20260929T115249Z-thuan-mac/reference/great grandmother_dec0f26b-6bfa-439d-afa0-f23e952da678.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'smiling-woman-head-with-bun-and-glasses'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'woman', 'head', 'with', 'bun', 'and', 'glasses')
    
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

        path('face',(6,24),[('L',(6,23)),('C',(16,15),(6,17),(10,15)),('A',(32,15),8,9,True),('C',(42,23),(38,15),(42,17)),('L',(42,24)),('A',(6,24),18)],True)
        for x in (18,30):circle('lens'+str(x),x,26,3)
        line('bridge',(21,26),(27,26));join('bridge','lens18','lens30')
