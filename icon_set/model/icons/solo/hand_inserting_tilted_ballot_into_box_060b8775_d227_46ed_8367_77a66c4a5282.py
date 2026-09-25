"""Hand Inserting Vote into Ballot Box.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The ballot keeps its diagonal orientation as it enters the box. Occluded upper card edges are removed beneath the gripping hand; the thumb opening is widened.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-grab.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '060b8775-d227-46ed-8367-77a66c4a5282'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/election ballot box 2_060b8775-d227-46ed-8367-77a66c4a5282.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-inserting-tilted-ballot-into-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('hand', 'inserting', 'tilted', 'ballot', 'into', 'box')

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

        poly('box',(6,30),(22,30),(42,30),(42,42),(6,42),closed=True)
        poly('paper-left',(22,30),(6,14),(14,6));line('paper-right',(36,22),(22,30));join('paper-left','box');join('paper-right','box')
        line('hand-upper',(14,6),(42,6));join('hand-upper','paper-left')
        path('hand-lower',(42,22),[('L',(36,22)),('L',(28,22)),('A',(28,14),4,4,True),('L',(36,14))]);join('hand-lower','paper-right')
