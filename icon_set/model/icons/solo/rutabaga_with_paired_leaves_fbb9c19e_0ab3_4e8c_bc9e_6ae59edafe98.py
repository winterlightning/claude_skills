"""Root vegetable with leaves.

Plan: Rutabaga bulb, pointed root and paired leaves; bounds8,4,40,44.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbb9c19e-0ab3-4e8c-bc9e-6ae59edafe98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/rutabaga_fbb9c19e-0ab3-4e8c-bc9e-6ae59edafe98.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rutabaga-with-paired-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('rutabaga', 'with', 'paired', 'leaves')

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

        path('bulb',(24,24),[('C',(40,30),(34,24),(40,27)),('C',(24,44),(40,38),(28,38)),('C',(8,30),(20,38),(8,38)),('C',(24,24),(8,27),(14,24))],True)
        line('stem',(24,24),(24,14));join('stem','bulb')
        path('leaves',(24,14),[('C',(8,4),(12,14),(8,10)),('C',(24,14),(17,4),(22,7)),('C',(40,4),(26,7),(31,4)),('C',(24,14),(40,10),(36,14))],True);join('leaves','stem')
