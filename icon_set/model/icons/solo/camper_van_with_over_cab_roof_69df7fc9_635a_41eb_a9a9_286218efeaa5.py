"""Recreational Vehicle Camper Van.

Plan: Camper body and overcab ledge, two wheels and one side window; bounds4,8,44,40.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69df7fc9-635a-41eb-a9a9-286218efeaa5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rv_69df7fc9-635a-41eb-a9a9-286218efeaa5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'camper-van-with-over-cab-roof'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('camper', 'van', 'with', 'over', 'cab', 'roof')

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

        path('body',(8,8),[('L',(34,8)),('C',(40,16),(38,8),(40,12)),('L',(30,16)),('L',(34,24)),('L',(40,24)),('L',(44,24)),('L',(44,36)),('L',(36,36)),('A',(28,36),4,4,False),('L',(20,36)),('A',(12,36),4,4,False),('L',(4,36)),('L',(4,12)),('A',(8,8),4,4,True)],True)
        for x in (12,28):path('wheel-'+str(x),(x,36),[('A',(x+8,36),4,4,False)]);join('wheel-'+str(x),'body')
        line('window',(13,20),(21,20))
