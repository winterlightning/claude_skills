"""The current lasagna has a sharp top and an almost flat bottom dash. No written feedback. Rounded the top pasta corners, centered an even wavy filling, and restored a curved lower pasta edge; omitted the lower closed seam to keep layer gaps clear.
Construction: No useful exact Lucide match; reference composition and geometric construction.
Plan: HRECT_L SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2aff3c8f-3e4c-45f3-ba4c-fd7a453c14fe'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__layered-lasagna/20260929T110914Z-thuan-mac/reference/lasagna_2aff3c8f-3e4c-45f3-ba4c-fd7a453c14fe.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'layered-lasagna'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('layered', 'lasagna')
    
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

        path('top',(4,17),[('L',(8,10)),('C',(12,8),(9,8),(10,8)),('L',(36,8)),('C',(40,10),(38,8),(39,8)),('L',(44,17)),('L',(4,17))],True)
        bez('filling',(4,27),((11,22),(17,32),(24,27)),((31,22),(37,32),(44,27)))
        path('bottom',(4,38),[('C',(12,40),(4,40),(8,40)),('L',(36,40)),('C',(44,38),(40,40),(44,40))])
