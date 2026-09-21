'A tall rounded cabinet surrounds three separate rounded rectangular drawer fronts. Each drawer has a short centered horizontal handle, with clear gaps between the fronts and the outer frame.\nPlan: Three filing drawers retain count and centered pulls. Remove nested cabinet frame to open space; drawer seams share the outer walls. 40-unit vertical budget is tight for three 16-unit handle bands.\nConstruction reference: panels-top-left: connected panel seams, repeated handle definition.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39bc7143-aab6-4bbb-9e54-1e955c556e69'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/archive locker 1_39bc7143-aab6-4bbb-9e54-1e955c556e69.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cabinet-with-three-inset-drawers'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('cabinet', 'with', 'three', 'inset', 'drawers')

    # Repair: Three separate drawer fronts retained. Outer shell and handles omitted: nesting them requires more than 40 centerline units.
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
