"""Ringed Planet Saturn.

Plan: Planet circle with sweeping diagonal ring; bounds6,6,42,42. Front orbit occludes lower globe.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6202dcbb-4f20-480e-8b1f-ebc5b4ef0324'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__planet-with-diagonal-ring/20260927T164305Z-thuan-mac-1/reference/planet ringed_6202dcbb-4f20-480e-8b1f-ebc5b4ef0324.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'planet-with-diagonal-ring'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('planet', 'with', 'diagonal', 'ring')

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

        path('globe',(9,24),[('A',(24,9),15,15,True),('A',(36,15),15,15,True),('A',(39,24),15,15,True),('A',(24,39),15,15,True),('A',(12,33),15,15,True),('A',(9,24),15,15,True)],True)
        # The broad diagonal is a continuous orbit, as in the source drawing.
        path('orbit',(9,24),[('C',(4,40),(4,29),(4,36)),('C',(12,33),(6,40),(9,37)),('C',(36,15),(20,29),(29,20)),('C',(44,8),(40,11),(43,8)),('C',(39,24),(44,14),(44,19))]);join('orbit','globe')
