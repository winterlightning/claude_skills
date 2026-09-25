"""Rod of Asclepius Medical Symbol.

Plan: One serpentine line winds around upright staff; bounds8,4,40,44. Simplify snake thickness and retain three alternating bends.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3726d96a-f376-4f85-be5e-b05615cdd3f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rod of asclepius_3726d96a-f376-4f85-be5e-b05615cdd3f9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-serpent-around-a-staff'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('single', 'serpent', 'around', 'a', 'staff')

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

        poly('staff',(24,4),(24,12),(24,28),(24,44))
        path('snake',(40,12),[('L',(24,12)),('C',(8,20),(12,12),(8,14)),('C',(24,28),(8,26),(15,28)),('C',(36,34),(34,28),(36,30)),('C',(24,40),(36,40),(28,40))]);join('snake','staff')
