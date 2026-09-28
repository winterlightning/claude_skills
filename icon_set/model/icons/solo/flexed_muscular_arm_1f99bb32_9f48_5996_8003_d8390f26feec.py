'A muscular arm bends sharply upward at the elbow, ending in a clenched fist above the shoulder. Curved interior lines distinguish the forearm, biceps and the upper body at the right edge.\nPlan: Flexed arm with clenched fist, inner forearm and biceps bulge; coherent asymmetric silhouette. Extrema6,6,42,42.\nConstruction reference: Lucide biceps-flexed original/atomic-debug: continuous flexed-arm contour; human_ref/full_body_ref.png for simple anatomy.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f99bb32-9f48-5996-8003-d8390f26feec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-11/strenght ability_1f99bb32-9f48-5996-8003-d8390f26feec.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flexed-muscular-arm-clenched-fist'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('flexed', 'muscular', 'arm')

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
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

        path('arm',(6,34),[('C',(17,6),(6,18),(9,6)),('C',(27,12),(24,6),(27,7)),('A',(23,16),4,4,True),('L',(19,16)),('L',(17,30)),('C',(29,27),(21,26),(25,26)),('C',(42,31),(35,24),(42,26)),('C',(30,42),(42,38),(36,42)),('L',(16,42)),('C',(6,34),(10,42),(6,39))],True)
