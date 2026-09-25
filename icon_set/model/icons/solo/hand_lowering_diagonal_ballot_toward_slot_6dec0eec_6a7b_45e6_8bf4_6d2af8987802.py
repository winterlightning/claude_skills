"""Hand Casting Election Ballot.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The hand grips a diagonal blank ballot above the slot. Hidden card edges are removed at the thumb.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-grab.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6dec0eec-6a7b-45e6-8bf4-6d2af8987802'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/election ballot box 1_6dec0eec-6a7b-45e6-8bf4-6d2af8987802.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-lowering-diagonal-ballot-toward-slot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('hand', 'lowering', 'diagonal', 'ballot', 'toward', 'slot')

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

        poly('paper',(18,16),(6,28),(20,42),(36,26),(30,20))
        path('hand',(32,6),[('L',(18,16)),('A',(24,24),5,5,False),('L',(30,20)),('L',(34,20)),('L',(42,14))]);join('paper','hand')
        line('slot',(6,42),(20,42));join('slot','paper')
