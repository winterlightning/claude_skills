'A broad rectangular entrance surround contains a tall central arched opening. A horizontal band crosses near the top, while equal side piers descend to a straight shared lower edge.\nPlan: Rectangular surround with inset central arch; shared baseline nodes. Remove top band to give the arch legal clearance.\nConstruction reference: panels-top-left: shared structural edges, one coherent perimeter.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cefac8c4-8b54-4ce8-aeea-34b69895ec80'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/loggia_cefac8c4-8b54-4ce8-aeea-34b69895ec80.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rectangular-entrance-with-central-arch'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('rectangular', 'entrance', 'with', 'central', 'arch')

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

        poly('surround',(6,42),(6,6),(42,6),(42,42),(33,42),(15,42),(6,42))
        path('arch',(15,42),[('L',(15,28)),('A',(33,28),9,9,True),('L',(33,42))])
        join('surround','arch')
