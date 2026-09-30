"""The current smoke is two horizontal curls above an undersized bust. No written feedback. Rebuilt tall, open rising smoke contours flanking a larger centered head and curved shoulders.
Construction: Human user.svg: circular head and curved shoulder. Bust ink touches at center; smoke intentionally flares outward.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '071c4c52-a190-4210-8d8d-e3f3838977f4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-beneath-rising-smoke-plumes-071c4c52/20260929T110914Z-thuan-mac/reference/ashura day of atonement tenth day of muharram_071c4c52-a190-4210-8d8d-e3f3838977f4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-beneath-rising-smoke-plumes-071c4c52'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'beneath', 'rising', 'smoke', 'plumes', '071c4c52')
    human_construction = "bust"
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

        circle('head',24,29,4)
        arc('shoulder-left',(14,42),(24,37),10,5)
        arc('shoulder-right',(24,37),(34,42),10,5)
        join('head','shoulder-left');join('head','shoulder-right')
        path('smoke-left',(12,29),[('C',(7,20),(6,27),(6,24)),('C',(6,10),(11,17),(11,13)),('C',(12,6),(6,6),(9,6))])
        path('smoke-right',(36,29),[('C',(41,20),(42,27),(42,24)),('C',(42,10),(37,17),(37,13)),('C',(36,6),(42,6),(39,6))])
