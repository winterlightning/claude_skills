'Two pointed tea leaves spread from a curved branching stem at upper left. Five rounded pearls overlap in a compact cluster below and to the right of the leaves.\nPlan: Two tea leaves above five pearls. Preserve all five pearls; separate the pearl outlines instead of overlapping their ink.\nConstruction reference: leaf: coherent pointed leaves; circles preserve the ingredient cluster.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47b073e7-6d6d-4914-a060-1296929bd372'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bubble tea leaf_47b073e7-6d6d-4914-a060-1296929bd372.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tea-leaves-beside-pearl-cluster'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tea', 'leaves', 'beside', 'pearl', 'cluster')

    # Repair: Five pearl circles have 4-unit centerline diameters, not zero-area holes; spread to a two-over-three group.
    # Repair: Remove the nonessential extended stem and shorten the leaf pair to provide clearance above all five outlined pearls.
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

        path('leaves',(6,6),[('C',(16,18),(13,6),(16,11)),('C',(28,6),(17,10),(22,6)),('C',(16,18),(28,15),(23,18)),('C',(6,6),(8,18),(6,12))],True)
        for j,(x,y) in enumerate([(20,28),(33,28),(12,40),(26,40),(40,40)]):circle(f'pearl-{j}',x,y,2)
