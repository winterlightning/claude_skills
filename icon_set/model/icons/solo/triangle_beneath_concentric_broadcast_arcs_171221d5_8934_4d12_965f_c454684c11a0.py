'A broad triangular mark with rounded corners sits beneath three concentric open arcs. The arcs curve around an empty center above the triangle, and their lower ends stop on either side.\nPlan: Triangle antenna beneath concentric waves; reduce wave series from three to two. Extrema8,4,40,44.\nConstruction reference: Lucide wifi: concentric arc construction; triangle retained from original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '171221d5-8934-4d12-965f-c454684c11a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sharing data blutooth_171221d5-8934-4d12-965f-c454684c11a0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triangle-beneath-concentric-broadcast-arcs'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('triangle', 'beneath', 'concentric', 'broadcast', 'arcs')

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

        for n,r in enumerate((16,7)):path(f'wave-{n}',(24-r,20),[('A',(24,20-r),r,r,True),('A',(24+r,20),r,r,True)])
        poly('antenna',(24,28),(36,44),(12,44),(24,28))
