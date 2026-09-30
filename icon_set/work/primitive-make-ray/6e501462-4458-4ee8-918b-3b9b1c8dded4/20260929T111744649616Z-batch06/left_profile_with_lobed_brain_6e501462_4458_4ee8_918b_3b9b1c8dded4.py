"""The rejected brain is a pinched clover and the facial jaw is angular. No written feedback. Opened the brain into broad rounded lobes and smoothed the left-facing head and neck; omitted internal folds.
Construction: Lucide brain: coherent rounded lobes. Shared human user reference: smooth head and shoulder vocabulary.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6e501462-4458-4ee8-918b-3b9b1c8dded4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__left-profile-with-lobed-brain/20260929T110914Z-thuan-mac/reference/neurobiologist_6e501462-4458-4ee8-918b-3b9b1c8dded4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'left-profile-with-lobed-brain'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('left', 'profile', 'with', 'lobed', 'brain')
    
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

        path('head',(35,42),[('C',(42,22),(32,33),(42,33)),('C',(25,6),(42,12),(35,6)),('C',(10,21),(16,6),(10,12)),('L',(6,28)),('L',(10,28)),('L',(10,33)),('C',(14,36),(10,35),(11,36)),('L',(22,36)),('L',(22,42))])
        path('brain',(20,26),[('C',(19,20),(16,26),(17,21)),('C',(26,16),(18,15),(23,13)),('C',(31,21),(30,14),(33,17)),('C',(27,27),(33,25),(30,28)),('L',(27,26)),('L',(20,26))],True)
