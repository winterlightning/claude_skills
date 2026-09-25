"""Round Lychee Fruit With Stem.

Plan: Scalloped lychee with short stem; bounds8,4,40,44. Six broad lobes replace fine scallops.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cfc159ee-9340-421a-b18c-64e67e4703dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/lychee_cfc159ee-9340-421a-b18c-64e67e4703dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'scalloped-lychee-with-short-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('scalloped', 'lychee', 'with', 'short', 'stem')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('fruit',(24,12),[('C',(36,16),(32,8),(36,10)),('C',(40,28),(40,20),(36,24)),('C',(32,40),(40,34),(38,40)),('C',(24,44),(30,44),(27,44)),('C',(16,40),(21,44),(18,44)),('C',(8,28),(10,40),(8,34)),('C',(12,16),(12,24),(8,20)),('C',(24,12),(12,10),(16,8))],True)
        path('stem',(24,12),[('C',(28,4),(24,8),(24,6))]);join('stem','fruit')
