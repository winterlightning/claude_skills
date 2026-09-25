'A straight vertical stem branches diagonally to the left and right at different heights. Three circular nodes cap the central stem and the two slanted branches.\nPlan: Vertical stem with three capped branches; left and right branches emerge at different heights.\nConstruction reference: network: round nodes use exact cardinal connection points.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f5900f6-5a24-49f0-8fab-d7cab2a4b8df'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/branch_2f5900f6-5a24-49f0-8fab-d7cab2a4b8df.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'branching-stem-with-round-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('branching', 'stem', 'with', 'round', 'nodes')

    # Repair: Smaller node outlines and wider branch offsets open certified internal gaps; separate branch heights retained.
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

        circle('top',24,10,4);circle('left',10,24,4);circle('right',38,28,4)
        poly('stem',(24,14),(24,34),(24,38),(24,42))
        line('left-link',(14,24),(24,34));line('right-link',(34,28),(24,38))
        join('stem','top');join('stem','left-link');join('stem','right-link');join('left','left-link');join('right','right-link')
