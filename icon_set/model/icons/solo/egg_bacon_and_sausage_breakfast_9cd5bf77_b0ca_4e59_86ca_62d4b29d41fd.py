"""Fried Egg Bacon and Sausage.

Plan: Breakfast group of sausage, fried egg and bacon. Bounds6,6,42,42. Omit sausage scoring and bacon inner stripe.
Construction reference: No useful local Lucide match.
Final review: Yolk reduced to one mark to preserve egg clearance.

"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9cd5bf77-b0ca-4e59-86ca-62d4b29d41fd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/breakfast english_9cd5bf77-b0ca-4e59-86ca-62d4b29d41fd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'egg-bacon-and-sausage-breakfast'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('egg', 'bacon', 'and', 'sausage', 'breakfast')

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

        rect('sausage',6,6,36,8,4)
        circle('egg',16,32,10);line('yolk',(16,32),(16,32))
        path('bacon',(34,24),[('C',(42,24),(36,28),(40,28)),('L',(42,42)),('C',(34,42),(40,38),(36,38)),('L',(34,24))],True)
