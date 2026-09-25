'Three broad grains form a triangular group with one above and two below. Each has a pointed upper tip, curved sides and a flattened rounded base.\nPlan: Three grain outlines in a triangular group. Shared grain definition, two bottom instances and a centered top one.\nConstruction reference: bean: smooth food contours, with source three-grain layout.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9588ce1d-b11c-425d-9000-0a97517cf561'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/buckwheat_9588ce1d-b11c-425d-9000-0a97517cf561.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-teardrop-buckwheat-grains'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'teardrop', 'buckwheat', 'grains')

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

        for name,x,y in [('top',24,6),('left',13,27),('right',35,27)]:
         path(name,(x,y),[('C',(x+7,y+11),(x+4,y+3),(x+7,y+7)),('C',(x,y+15),(x+7,y+15),(x+3,y+15)),('C',(x-7,y+11),(x-3,y+15),(x-7,y+15)),('C',(x,y),(x-7,y+7),(x-4,y+3))],True)
