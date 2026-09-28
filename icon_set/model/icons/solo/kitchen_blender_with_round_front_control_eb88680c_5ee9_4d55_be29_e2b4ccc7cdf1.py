"""Tapered jug, open curved handle and broad motor housing with an outlined round control. VRECT_L centerlines (8,4)-(40,44). Restore the circular control; one shared divider avoids double painting. Omit tiny feet and lid thickness."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eb88680c-5ee9-4d55-be29-e2b4ccc7cdf1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/drinks/vitamix_eb88680c-5ee9-4d55-be29-e2b4ccc7cdf1.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'blender'
DESIGN_PLAN = 'Tapered jug, open curved handle and broad motor housing with an outlined round control. VRECT_L centerlines (8,4)-(40,44). Restore the circular control; one shared divider avoids double painting. Omit tiny feet and lid thickness.'
class Drawing(Solo48):
    icon_id = 'kitchen-blender-with-round-front-control'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    categories = ('drinks', 'primitives')
    aliases = ()
    keywords = ('kitchen', 'blender', 'with', 'round', 'front', 'control')
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)


    def build(self):
        self.path('silhouette',(8,4),[('L',(32,4)),('L',(30,20)),('L',(40,44)),('L',(8,44)),('L',(14,20)),('L',(8,4))],True)
        self.add_line('divider',(14,20),(30,20));self.relate('connect','silhouette','divider')
        self.path('handle',(32,4),[('A',(40,12),8,8,True),('L',(40,22))]);self.relate('connect','silhouette','handle')
        self.circle('control',23,32,3)
