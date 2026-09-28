'Three long horizontal arrows point right in evenly spaced parallel rows. Each straight shaft ends in an open angled arrowhead, with their tips aligned vertically and no enclosing frame.\nPlan: Three identical right arrows in parallel rows. Shared head dimensions and vertical pitch.\nConstruction reference: arrow-right: open head and straight shaft, same direction as original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6b5b550-00d1-4b59-b66b-e0afb5d02bdd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/spread_c6b5b550-00d1-4b59-b66b-e0afb5d02bdd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-parallel-rightward-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'parallel', 'rightward', 'arrows')

    # Repair: Three compact open heads on 12-unit row pitch; all arrows remain rightward.
    # Repair: Expanded vertical pitch preserves open arrowheads and exact eight-unit gaps.
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

        for j,y in enumerate((8,24,40)):
         poly(f'head-{j}',(34,y-4),(40,y),(34,y+4))
         line(f'shaft-{j}',(8,y),(40,y));join(f'head-{j}',f'shaft-{j}')
