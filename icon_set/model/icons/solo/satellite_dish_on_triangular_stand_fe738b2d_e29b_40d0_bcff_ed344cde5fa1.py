"""Satellite Communication Dish Antenna.

Plan: Retained the tilted dish, circular receiver, receiver arm and lower support. Reduced the narrow triangular support to an open angled stand.
Construction reference: Lucide satellite-dish: open diagonal rim and coherent bowl; original receiver and stand retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe738b2d-e29b-40d0-bcff-ed344cde5fa1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/satellite dish_fe738b2d-e29b-40d0-bcff-ed344cde5fa1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'satellite-dish-on-triangular-stand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('satellite', 'dish', 'on', 'triangular', 'stand')

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
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('dish',(6,6),[('L',(24,18)),('L',(40,28)),('C',(12,28),(30,34),(18,34)),('C',(6,6),(6,24),(6,14))],True)
        line('arm',(24,18),(34,10));circle('receiver',38,10,4);join('arm','dish');join('arm','receiver')
        poly('stand',(12,28),(6,42),(20,42));join('stand','dish')
