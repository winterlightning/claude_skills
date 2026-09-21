'A single palm tree rises from a low semicircular island with a flat base. Four broad curved fronds spread from the top of its straight trunk, with pointed tips bending outward.\nPlan: Straight palm trunk, four broad open curved fronds and island arch.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1511e95-9a98-487e-846a-f2846ba62cde'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/oasis_e1511e95-9a98-487e-846a-f2846ba62cde.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'palm-small-island'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('palm', 'small', 'island')

    # Repair: Set frond top endpoints at exact y6 while retaining natural bowed fronds.
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

        line('trunk',(24,16),(24,34))
        for name,start,steps in [('a',(6,6),[('C',(24,16),(14,6),(20,6))]),('b',(42,6),[('C',(24,16),(34,6),(28,6))]),('c',(6,24),[('C',(24,16),(6,14),(16,12))]),('d',(42,24),[('C',(24,16),(42,14),(32,12))])]:
         path(name,start,steps);join(name,'trunk')
        for a,b in [('a','b'),('a','c'),('a','d'),('b','c'),('b','d'),('c','d')]:join(a,b)
        path('island',(6,42),[('C',(24,34),(10,36),(16,34)),('C',(42,42),(32,34),(38,36)),('L',(6,42))],True);join('trunk','island')
