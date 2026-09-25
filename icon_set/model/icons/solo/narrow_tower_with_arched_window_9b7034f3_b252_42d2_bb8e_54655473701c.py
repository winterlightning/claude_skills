'A tall narrow tower has a pointed triangular roof above a plain rectangular shaft. A small arched window sits near the top, with short horizontal roof and base projections.\nPlan: Pointed bell tower with one arched window. Roof and baseline projections omitted. Shared roof/body seam.\nConstruction reference: tower-control: legible roof/shaft hierarchy; source has a pointed roof.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b7034f3-b252-42d2-bb8e-54655473701c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/campanile_9b7034f3-b252-42d2-bb8e-54655473701c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'narrow-tower-with-arched-window'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('narrow', 'tower', 'with', 'arched', 'window')

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

        poly('tower',(10,44),(10,16),(24,4),(38,16),(38,44),(10,44))
        line('eave',(10,16),(38,16));join('tower','eave')
        path('window',(20,34),[('L',(20,28)),('A',(28,28),4,4,True),('L',(28,34)),('L',(20,34))],True)
