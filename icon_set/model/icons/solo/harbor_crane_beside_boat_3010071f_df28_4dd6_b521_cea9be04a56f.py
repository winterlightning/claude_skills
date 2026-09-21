"""Shipyard Boat Lift Crane.

Plan: Retained the harbor crane, hanging hook, boat hull and cabin. Reduced the gantry beam thickness to a stroke and moved the hook clear of the cabin.
Construction reference: No useful exact Lucide match; source-specific construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3010071f-df28-4dd6-b521-cea9be04a56f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boatyard_3010071f-df28-4dd6-b521-cea9be04a56f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'harbor-crane-beside-boat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('harbor', 'crane', 'beside', 'boat')

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

        poly('crane',(42,42),(42,6),(10,6))
        path('hook',(33,6),[('L',(33,18)),('A',(25,18),4,4,True)]);join('hook','crane')
        poly('boat',(6,32),(30,32),(26,42),(10,42),(6,32),closed=True)
        poly('cabin',(8,32),(10,24),(18,24),(20,32));join('cabin','boat')
