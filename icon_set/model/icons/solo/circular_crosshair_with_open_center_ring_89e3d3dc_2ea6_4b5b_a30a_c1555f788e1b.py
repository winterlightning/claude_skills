'A circular target has four straight crosshair arms extending beyond its outer rim. The arms stop at a small central ring, leaving its interior empty and dividing the surrounding circle into quarters.\nPlan: Four radial crosshair arms through an outer ring, stopping at a central ring. Cardinal junctions are real shared endpoints.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89e3d3dc-2ea6-4b5b-a30a-c1555f788e1b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/southeast_89e3d3dc-2ea6-4b5b-a30a-c1555f788e1b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-crosshair-with-open-center-ring'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('circular', 'crosshair', 'with', 'open', 'center', 'ring')

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

        for name,r in [('outer',14),('inner',3)]:
         path(name,(24-r,24),[('A',(24,24-r),r,r,True),('A',(24+r,24),r,r,True),('A',(24,24+r),r,r,True),('A',(24-r,24),r,r,True)],True)
        for name,pts in [('left',[(4,24),(10,24),(21,24)]),('right',[(27,24),(38,24),(44,24)]),('up',[(24,4),(24,10),(24,21)]),('down',[(24,27),(24,38),(24,44)])]:
         poly(name,*pts);join(name,'outer');join(name,'inner')
