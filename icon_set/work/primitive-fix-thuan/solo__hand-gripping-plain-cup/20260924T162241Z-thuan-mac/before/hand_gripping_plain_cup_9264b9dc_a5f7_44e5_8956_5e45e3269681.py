"""Hand holding a ceramic cup.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
A raised thumb and broad curled finger wrap around a plain cup. The hidden cup wall is removed beneath the grip.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand-grab.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9264b9dc-a5f7-44e5-8956-5e45e3269681'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_10/ceramic making_9264b9dc-a5f7-44e5-8956-5e45e3269681.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-gripping-plain-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hand', 'gripping', 'plain', 'cup')

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

        poly('cup',(26,14),(42,14),(42,42),(26,42),(26,32))
        path('hand',(6,24),[('L',(12,24)),('C',(16,6),(16,18),(14,10)),('C',(26,10),(22,6),(26,6)),('L',(26,14)),('L',(24,24)),('L',(28,24)),('A',(28,32),4,4,True),('L',(20,32))])
        poly('palm',(6,38),(14,42),(26,42));join('palm','cup');join('hand','cup')
