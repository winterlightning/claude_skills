'A tall rounded cabinet is divided into three equal stacked drawers by horizontal seams. Each drawer carries a shallow cup-shaped pull with a flat top and curved lower corners.\nPlan: Three filing drawers retain count and centered pulls. Remove nested cabinet frame to open space; drawer seams share the outer walls. 40-unit vertical budget is tight for three 16-unit handle bands.\nConstruction reference: panels-top-left: connected panel seams, repeated handle definition.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65e153d2-cde9-406a-87e3-e702b60b0b83'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/archive locker_65e153d2-cde9-406a-87e3-e702b60b0b83.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-drawer-cabinet-with-cup-pulls'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'drawer', 'cabinet', 'with', 'cup', 'pulls')

    # Repair: Rounded cabinet and three drawer faces retained. Cup pulls omitted because each requires an unavailable 16-unit band.
    # Repair: Replace detached pulls with three integrated finger notches; preserve three functional drawer faces in the available height, omitting nested trim.
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)

        path('body',(8,4),[('L',(20,4)),('A',(28,4),4,4,False),('L',(40,4)),('L',(40,17)),('L',(40,31)),('L',(40,44)),('L',(8,44)),('L',(8,31)),('L',(8,17)),('L',(8,4))],True)
        for y in (17,31):
         path(f'drawer-{y}',(8,y),[('L',(20,y)),('A',(28,y),4,4,False),('L',(40,y))]);join('body',f'drawer-{y}')
