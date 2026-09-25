'A line descends on the left, rounds upward from a deep lower bend, and arches over at the top. Its rightmost vertical section ends in an open downward arrowhead.\nPlan: A flowing vertical line makes opposing U-bends and ends in a downward head. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80755080-33d0-42e7-9bca-68d0d18ad221'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/diagram dash wave down_80755080-33d0-42e7-9bca-68d0d18ad221.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-down-after-two-opposing-bends'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('arrow', 'down', 'after', 'two', 'opposing', 'bends')

    # Repair: Restore both sides of the downward arrowhead by bringing its shaft inward; preserve opposing bends.
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

        path('shaft',(6,6),[('L',(6,33)),('A',(15,42),9,9,False),('A',(24,33),9,9,False),('L',(24,11)),('A',(29,6),5,5,True),('A',(34,11),5,5,True),('L',(34,28))])
        poly('head',(26,20),(34,28),(42,20));join('head','shaft')
