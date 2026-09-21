'A broad outlined arrow points upward with a triangular head and two open shaft edges. Two separate horizontal bars sit beneath its tail, extending farther sideways than the shaft.\nPlan: Upward outlined arrow over two distinct horizontal bars.\nConstruction reference: Lucide arrow-up original and atomic-debug: central axis and equal arrowhead arms.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b34769bf-3391-42e5-ae9c-b1beff3c0b11'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/diagram arrow dash up_b34769bf-3391-42e5-ae9c-b1beff3c0b11.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-up-above-two-horizontal-bars'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('arrow', 'up', 'above', 'two', 'horizontal', 'bars')

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

        poly('arrow',(18,28),(18,16),(10,16),(24,4),(38,16),(30,16),(30,28))
        line('bar-upper',(8,36),(40,36));line('bar-lower',(8,44),(40,44))
