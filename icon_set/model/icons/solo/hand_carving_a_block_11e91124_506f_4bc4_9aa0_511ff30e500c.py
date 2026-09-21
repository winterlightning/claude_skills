"""Hand Carving With Tool.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The hand grips an angled chisel that meets a carved block. Concealed tool edges and small finger creases are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-grab.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11e91124-506f-4bc4-9aa0-511ff30e500c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/carving_11e91124-506f-4bc4-9aa0-511ff30e500c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-carving-a-block'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hand', 'carving', 'a', 'block')

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

        poly('block-base',(6,42),(18,42),(42,42),(42,34),(26,34))
        poly('chisel-left',(12,34),(20,22));poly('chisel-right',(34,26),(26,34),(18,42));join('chisel-right','block-base')
        path('hand',(26,6),[('L',(36,6)),('L',(42,12)),('L',(34,26)),('C',(26,18),(26,26),(22,22)),('L',(20,22))]);join('hand','chisel-left');join('hand','chisel-right')
