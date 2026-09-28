"""Reclining Sun Lounger.

Plan: Lounger continuous bent padded profile with two legs; bounds4,8,44,40.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1cad115-c07d-451b-a6d8-9d8725450bef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/daybed_b1cad115-c07d-451b-a6d8-9d8725450bef.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-lounger-with-angled-backrest'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('low', 'lounger', 'with', 'angled', 'backrest')

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

        path('seat',(4,12),[('A',(8,8),4,4,True),('L',(22,22)),('L',(38,22)),('A',(44,28),6,6,True),('L',(44,32)),('L',(16,32)),('L',(4,18)),('L',(4,12))],True)
        line('leg-left',(12,32),(10,40));line('leg-right',(38,32),(40,40));join('leg-left','seat');join('leg-right','seat')
