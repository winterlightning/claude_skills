'Two flowing banks trace a winding creek that bends from upper right toward lower left. A low rounded stone sits beside the left bank, with a flat base and arched top.\nPlan: Winding creek has two banks plus a rounded stone to the left. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b92e887-098d-47a7-8d9e-8a8c56cf19a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/creek_7b92e887-098d-47a7-8d9e-8a8c56cf19a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winding-creek-beside-rounded-stone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('winding', 'creek', 'beside', 'rounded', 'stone')

    # Repair: Space parallel bank constructions farther apart and retain the separate left-bank stone.
    # Repair: Use parallel coherent banks with a wider14-unit offset and a small round stone in the open left foreground.
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

        path('left-bank',(28,6),[('C',(22,16),(22,6),(22,10)),('C',(28,26),(22,20),(28,22)),('C',(16,42),(28,34),(16,34))])
        path('right-bank',(42,6),[('C',(36,16),(36,6),(36,10)),('C',(42,26),(36,20),(42,22)),('C',(30,42),(42,34),(30,34))])
        circle('stone',10,24,4)
