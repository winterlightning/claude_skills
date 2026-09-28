"""Rising Trend Bar Chart.

Plan: Ascending bars and rising trend arrow form a single chart; bounds4,8,44,40. Reduce bars to thick strokes where outlining would crowd.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cefde376-e6c6-4228-9fa9-9c6b0e5d5a0e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/chart area_cefde376-e6c6-4228-9fa9-9c6b0e5d5a0e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-bars-with-rising-trend-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'bars', 'with', 'rising', 'trend', 'arrow')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        poly('baseline',(4,40),(12,40),(20,40),(28,40),(36,40),(44,40))
        for x,y in ((4,32),(20,30),(36,25)):
         poly('bar-'+str(x),(x,40),(x,y),(x+8,y),(x+8,40));join('bar-'+str(x),'baseline')
        path('trend',(4,22),[('C',(44,8),(20,22),(36,17))]);poly('head',(36,8),(44,8),(44,16));join('head','trend')
