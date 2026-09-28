'A capped toothpaste tube stands beside an upright toothbrush. The tube narrows toward its broad lower cap, while three short horizontal bristles project left from the brush head.\nPlan: Tapered tube and single-stroke brush; cap and two bristles at 8-unit intervals.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0ea57261-df27-40e8-85d1-48d8e87aa7ac'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__toothpaste-tube-beside-toothbrush/20260927T173930Z-thuan-mac-1/reference/body care toothbrush paste_0ea57261-df27-40e8-85d1-48d8e87aa7ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'toothpaste-tube-beside-toothbrush'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
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
        line('bristle-upper',(34,14),(42,14));join('brush','bristle-upper')
        line('bristle-lower',(34,22),(42,22));join('brush','bristle-lower')
