"""Flower with Stem and Leaf.

Plan: Rounded flower lobes above stem and pointed leaves, bounds8,4,40,44. Omit tiny disk to preserve open blossom.
Construction reference: flower-2.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5ba3e5a-1e84-4926-9afb-e69a52e23191'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/corsage_f5ba3e5a-1e84-4926-9afb-e69a52e23191.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'five-petal-flower-with-side-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('five', 'petal', 'flower', 'with', 'side', 'leaf')

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

        path('bloom',(24,10),[('C',(30,4),(24,5),(26,4)),('C',(36,10),(34,4),(36,5)),('C',(40,15),(40,10),(40,12)),('C',(36,20),(40,18),(40,20)),('C',(36,28),(40,25),(40,28)),('C',(30,25),(32,28),(30,27)),('C',(22,28),(28,27),(26,28)),('C',(20,20),(18,28),(16,25)),('C',(16,15),(16,20),(16,18)),('C',(24,10),(16,12),(18,10))],True)
        line('stem',(30,25),(30,44));join('stem','bloom')
        path('leaf',(30,44),[('C',(8,35),(14,44),(8,40)),('C',(30,44),(22,36),(28,39))],True);join('leaf','stem')
