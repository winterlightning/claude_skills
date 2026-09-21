'Three small circular nodes are joined by sweeping curved lines in a rotating triangular arrangement. Each curve wraps around the outside before meeting the next node, leaving open gaps along the outer silhouette.\nPlan: Redux orbit emblem with three open sweep curves and circular nodes.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb47004b-f404-423b-86db-835fad7f0bcb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/redux logo_eb47004b-f404-423b-86db-835fad7f0bcb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'redux-three-lobed-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('redux', 'three', 'lobed', 'emblem')

    # Repair: Separate three orbit sweeps and reposition nodes to protect their radial clearance.
    # Repair: Move lower-right node away from upper orbit and shorten lower sweep to protect the left node.
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

        circle('node-a',18,18,2);circle('node-b',14,30,2);circle('node-c',30,30,2)
        path('orbit-a',(14,28),[('C',(6,20),(6,28),(6,26)),('C',(18,6),(6,10),(10,6)),('C',(32,10),(24,6),(30,6))]);join('node-b','orbit-a')
        path('orbit-b',(20,18),[('C',(42,28),(34,18),(42,20)),('L',(42,34))]);join('node-a','orbit-b')
        path('orbit-c',(30,32),[('C',(20,42),(30,38),(28,42)),('C',(6,40),(12,42),(6,42))]);join('node-c','orbit-c')
