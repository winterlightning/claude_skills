"A toothbrush crosses diagonally above a two rooted molar, with its bristle head hanging beneath the left end. The tooth's rounded crown dips centrally above its deeply separated roots.\nPlan: Small rounded two-root tooth beneath diagonal single-stroke brush with two bristles.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0b304e7-acb0-4e8f-9bd4-d6957e4d6065'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/dentistry tooth brush_e0b304e7-acb0-4e8f-9bd4-d6957e4d6065.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'angled-toothbrush-above-small-molar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('angled', 'toothbrush', 'above', 'small', 'molar')

    # Repair: Correct cubic root extrema to the exact envelope.
    # Repair: Remove crossing crown curves and rebuild two open roots.
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

        poly('brush',(6,6),(22,14),(42,14))
        line('bristle',(6,6),(6,14));join('brush','bristle')
        path('tooth',(6,28),[('C',(14,24),(6,20),(10,24)),('L',(22,24)),('C',(32,28),(30,20),(32,24)),('L',(30,36)),('C',(22,36),(30,44),(26,44)),('L',(18,30)),('L',(14,36)),('C',(6,36),(10,44),(6,44)),('L',(6,28))],True)
