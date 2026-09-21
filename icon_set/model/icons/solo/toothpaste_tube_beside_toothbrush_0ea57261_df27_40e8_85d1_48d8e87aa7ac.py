'A capped toothpaste tube stands beside an upright toothbrush. The tube narrows toward its broad lower cap, while three short horizontal bristles project left from the brush head.\nPlan: Tapered tube and single-stroke brush; cap and two bristles at 8-unit intervals.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ea57261-df27-40e8-85d1-48d8e87aa7ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/body care toothbrush paste_0ea57261-df27-40e8-85d1-48d8e87aa7ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toothpaste-tube-beside-toothbrush'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('toothpaste', 'tube', 'beside', 'toothbrush')

    # Repair: Split the brush at the bristle attachment.
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

        poly('tube',(6,6),(26,6),(22,34),(10,34),(6,6))
        poly('cap',(10,34),(10,42),(22,42),(22,34));join('tube','cap')
        path('brush',(42,42),[('L',(42,14)),('L',(42,6)),('L',(34,6))])
        line('bristle',(34,14),(42,14));join('brush','bristle')
