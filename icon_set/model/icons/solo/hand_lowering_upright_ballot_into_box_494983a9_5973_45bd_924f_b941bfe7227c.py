"""Hand Casting Ballot Into Box.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
An upright blank ballot enters a broad box beneath the gripping hand. The lid rim is omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-grab.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '494983a9-5973-45bd-924f-b941bfe7227c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/election ballot box 3_494983a9-5973-45bd-924f-b941bfe7227c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-lowering-upright-ballot-into-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hand', 'lowering', 'upright', 'ballot', 'into', 'box')

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

        poly('box',(6,30),(12,30),(28,30),(42,30),(42,42),(6,42),closed=True)
        poly('ballot-left',(12,30),(12,10),(24,10));line('ballot-right',(28,18),(28,30));join('box','ballot-left');join('box','ballot-right')
        path('hand',(42,6),[('L',(34,6)),('L',(24,10)),('A',(24,18),4,4,False),('L',(28,18)),('L',(34,18)),('L',(42,14))]);join('ballot-left','hand');join('ballot-right','hand')
