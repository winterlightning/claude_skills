'A rounded square outlet plate surrounds a broad horizontal hexagonal recess with softened corners. The recess is blank, with no visible pin holes or switches inside the outlined opening.\nPlan: Rounded outer outlet plate and single hexagonal recessed socket.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a29f7be-5f66-47a5-af04-831b2b22386d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/power outlet type j_6a29f7be-5f66-47a5-af04-831b2b22386d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'outlet-plate-with-hexagonal-recess'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('outlet', 'plate', 'with', 'hexagonal', 'recess')

    # Repair: Give the nested socket9-unit side clearance instead of a curved8-unit boundary.
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

        path('plate',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        poly('socket',(18,16),(30,16),(33,24),(30,32),(18,32),(15,24),(18,16))
