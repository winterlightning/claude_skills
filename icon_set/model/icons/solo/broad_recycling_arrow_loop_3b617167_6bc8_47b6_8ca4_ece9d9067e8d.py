'Three broad bent arrows form an open triangular recycling loop. Their outlined shafts bend around the corners and end in angular points, with small gaps separating the arrows around the empty center.\nPlan: Three broad recycling arrows around an open center; keep arrow directions and three-part count.\nConstruction reference: Lucide recycle from prior inspected reference: three separate arrow paths; source broad shafts retained in first attempt.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b617167-6bc8-47b6-8ca4-ece9d9067e8d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/recycle_3b617167-6bc8-47b6-8ca4-ece9d9067e8d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broad-recycling-arrow-loop'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('broad', 'recycling', 'arrow', 'loop')

    # Repair: Attempt open three-arrow construction after broad outlined shafts crowded each other; require fidelity review of the reduction.
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

        path('top',(14,14),[('L',(19,6)),('L',(25,6)),('L',(34,18))]);poly('head-top',(24,16),(34,18),(38,8));join('top','head-top')
        path('right',(42,28),[('L',(42,38)),('A',(38,42),4,4,True),('L',(26,42))]);poly('head-right',(32,34),(26,42),(34,42));join('right','head-right')
        path('left',(16,42),[('L',(10,42)),('A',(6,38),4,4,True),('L',(6,24))]);poly('head-left',(6,32),(6,24),(14,28));join('left','head-left')
