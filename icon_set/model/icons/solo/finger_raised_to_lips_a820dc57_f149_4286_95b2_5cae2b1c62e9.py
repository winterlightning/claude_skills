"""Finger on Lips Silence Gesture.

Plan: Left-facing human profile with finger held at lips; bounds8,4,40,44. One coherent hand silhouette replaces tiny folded fingertips.
Construction reference: human_ref/user.svg.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a820dc57-f149-4286-95b2-5cae2b1c62e9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/allowances silence_a820dc57-f149-4286-95b2-5cae2b1c62e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'finger-raised-to-lips'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('finger', 'raised', 'to', 'lips')

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

        path('profile',(40,4),[('C',(32,12),(36,4),(34,6)),('L',(30,24)),('L',(38,24)),('L',(38,34)),('L',(40,34)),('L',(40,44))])
        path('hand',(8,44),[('L',(8,36)),('L',(14,36)),('L',(14,20)),('A',(22,20),4,4,True),('L',(22,44))])
