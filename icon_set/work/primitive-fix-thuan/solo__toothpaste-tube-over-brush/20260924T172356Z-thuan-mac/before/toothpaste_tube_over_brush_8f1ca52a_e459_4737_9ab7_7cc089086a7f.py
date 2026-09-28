'A toothpaste tube angles downward toward a horizontal toothbrush, with a separate curl of paste between them. The brush has a short bristled head and a bent handle extending right.\nPlan: Angled toothpaste tube above a bent horizontal brush; paste suggested as single curved stroke.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f1ca52a-e459-4737-9ab7-7cc089086a7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/brush toothpaste 2_8f1ca52a-e459-4737-9ab7-7cc089086a7f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toothpaste-tube-over-brush'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('toothpaste', 'tube', 'over', 'brush')

    # Repair: Shorten second bristle for clearance to angled tube.
    # Repair: Split the brush spine at the second bristle.
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

        poly('tube',(24,6),(42,16),(28,28),(20,24),(24,6))
        line('nozzle',(20,24),(16,28));join('tube','nozzle')
        path('brush',(6,42),[('L',(14,42)),('L',(26,42)),('C',(34,38),(30,42),(30,38)),('L',(42,38))])
        line('bristle-a',(6,34),(6,42));line('bristle-b',(14,38),(14,42));join('brush','bristle-a');join('brush','bristle-b')
