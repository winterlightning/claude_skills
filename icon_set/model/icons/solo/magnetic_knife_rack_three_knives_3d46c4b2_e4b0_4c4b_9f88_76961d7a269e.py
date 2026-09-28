"""Three evenly spaced knife definitions hang from one horizontal rail. Curved blade bellies replace angular wedges. HRECT_L centerlines (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3d46c4b2-e4b0-4c4b-9f88-76961d7a269e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/kitchen knife set_3d46c4b2-e4b0-4c4b-9f88-76961d7a269e.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='No useful exact Lucide rack match'
DESIGN_PLAN='Three evenly spaced knife definitions hang from one horizontal rail. Curved blade bellies replace angular wedges. HRECT_L centerlines (4,8)-(44,40).'
OMISSIONS='Rail thickness and outlined handles reduced to single strokes; three knives retained.'
class Drawing(Solo48):
    icon_id='magnetic-knife-rack-three-knives'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'furnitures'
    categories = ('furnitures', 'primitives')
    aliases=()
    keywords=('magnetic', 'knife', 'rack', 'three', 'knives')
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
        self.add_polyline('rail',*((x,22) for x in (4,12,20,28,36,44)))
        for i,x in enumerate((4,20,36)):
            self.add_line(f'handle-{i}',(x+8,8),(x+8,22));self.relate('connect','rail',f'handle-{i}')
            self.path(f'blade-{i}',(x,22),[('L',(x,40)),('C',(x+8,28),(x+6,36),(x+8,32)),('L',(x+8,22))]);self.relate('connect','rail',f'blade-{i}')
