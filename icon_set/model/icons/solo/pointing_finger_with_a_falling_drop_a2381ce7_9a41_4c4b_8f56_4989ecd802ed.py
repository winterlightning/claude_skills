"""Hand with Bleeding Finger.

Plan: SQUARE, centerline extremes (6, 6, 42, 42); 48 x 48, stroke 4.
The horizontal pointing finger sits above a pointed droplet. Fine finger divisions are omitted.
Repeated circles, arcs and equal series use shared helper definitions and parameters.
Construction reference: hand.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2381ce7-9a41-4c4b-8f56-4989ecd802ed'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/bandage finger bleed_a2381ce7-9a41-4c4b-8f56-4989ecd802ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointing-finger-with-a-falling-drop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('pointing', 'finger', 'with', 'a', 'falling', 'drop')

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

        path('hand',(6,18),[('L',(18,6)),('C',(28,10),(22,6),(28,6)),('L',(24,14)),('L',(38,14)),('A',(38,22),4,4,True),('L',(24,22)),('L',(24,38)),('L',(16,38)),('L',(6,34))])
        path('drop',(38,31),[('L',(34,38)),('A',(42,38),4,4,False),('L',(38,31))],True)
