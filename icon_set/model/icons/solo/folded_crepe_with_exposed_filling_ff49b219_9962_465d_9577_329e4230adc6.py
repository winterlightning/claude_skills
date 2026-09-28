"""Folded Dessert Crepe.

Plan: Folded crepe pocket with exposed filling and overlapping front flap. Bounds8,4,40,44. No small filling marks.
Construction reference: origami.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff49b219-9962-465d-9577-329e4230adc6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/crepe_ff49b219-9962-465d-9577-329e4230adc6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'folded-crepe-with-exposed-filling'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('folded', 'crepe', 'with', 'exposed', 'filling')

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

        path('crepe',(8,20),[('C',(16,12),(8,14),(12,12)),('C',(24,4),(16,6),(20,4)),('C',(40,20),(30,4),(36,12)),('L',(24,44)),('L',(8,20))],True)
        path('fold',(8,20),[('C',(32,32),(20,20),(28,24))]);join('crepe','fold')
