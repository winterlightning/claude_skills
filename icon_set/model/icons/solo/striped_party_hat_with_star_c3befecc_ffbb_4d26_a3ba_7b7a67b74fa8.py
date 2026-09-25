"""Festive Party Hat with Star.

Plan: Cone party hat with integral star topper, bounds8,4,40,44. Keep one diagonal stripe and five-point topper.
Construction reference: star.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3befecc-ffbb-4d26-a3ba-7b7a67b74fa8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/christmas tree top_c3befecc-ffbb-4d26-a3ba-7b7a67b74fa8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'striped-party-hat-with-star'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('striped', 'party', 'hat', 'with', 'star')

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

        poly('star',(24,4),(27,10),(34,11),(29,16),(30,22),(24,19),(18,22),(19,16),(14,11),(21,10),closed=True)
        poly('hat',(18,22),(8,44),(40,44),(30,22));join('hat','star')
        line('stripe',(13,33),(35,33));join('stripe','hat')
