'A tall straight mast carries a small right pointing triangular pennant near its top. The mast continues below the flag to a short horizontal base, leaving the surrounding area empty.\nPlan: Mast with small triangular flag and broad perpendicular foot.\nConstruction reference: Lucide flag-triangle-right original and atomic-debug: triangle shares flagpole endpoints.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '37fa01b0-1055-4bc6-969d-eed8f2b7a86d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mast_37fa01b0-1055-4bc6-969d-eed8f2b7a86d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triangular-pennant-on-footed-mast'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('triangular', 'pennant', 'on', 'footed', 'mast')

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

        poly('mast',(12,4),(12,28),(12,44));poly('flag',(12,4),(40,16),(12,28));join('flag','mast')
        poly('foot',(8,44),(12,44),(28,44));join('mast','foot')
