"""Hand Holding Megaphone.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The upward-tilted horn and gripping hand retain the megaphone interaction. Hidden handle edges are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: megaphone hand-fist.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dade40b3-c760-4793-8539-0b7a29c7d77c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/election campaign 4_dade40b3-c760-4793-8539-0b7a29c7d77c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-gripping-upward-tilted-megaphone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('hand', 'gripping', 'upward', 'tilted', 'megaphone')

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

        poly('horn',(14,16),(36,6),(42,24),(22,24))
        path('rear',(14,16),[('L',(10,18)),('A',(14,28),6,6,False),('L',(22,24))]);join('rear','horn')
        line('handle',(22,24),(26,36));join('handle','horn');join('handle','rear')
        path('hand',(6,42),[('L',(14,38)),('L',(16,36)),('L',(28,36)),('A',(32,40),4,4,True),('L',(32,42))]);join('hand','handle')
