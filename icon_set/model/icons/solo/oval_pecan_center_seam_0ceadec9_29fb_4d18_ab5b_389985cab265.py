'A tall oval pecan is divided by a straight vertical seam from top to bottom. Two curved interior grooves bow outward on either side, following the symmetrical shape of the shell.\nPlan: An oval shell split by its central seam. Remove paired inner grooves to preserve open half-shells. Extremes (8,4)-(40,44).\nConstruction reference: nut: smooth coherent shell; preserve the pecan oval rather than the acorn cap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ceadec9-29fb-4d18-ab5b-389985cab265'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pecan_0ceadec9-29fb-4d18-ab5b-389985cab265.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oval-pecan-center-seam'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('oval', 'pecan', 'center', 'seam')

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

        path('shell',(24,4),[('A',(40,24),16,20,True),('A',(24,44),16,20,True),('A',(8,24),16,20,True),('A',(24,4),16,20,True)],True)
        line('seam',(24,4),(24,44));join('shell','seam')
