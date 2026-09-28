'An open paint pail tilts toward the lower right with an oval rim and rounded lower corners. A single pointed paint drop sits below and beside its opening.\nPlan: Tilted open paint pail with a separate drop. Broad diagonal rim, rounded lower pail corner; source has no handle.\nConstruction reference: paint-bucket: separate drop and tilted vessel, without adding a source-absent handle.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78957ac2-2cd6-40d7-880e-fe1886f1b394'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/color bucket_78957ac2-2cd6-40d7-880e-fe1886f1b394.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tilted-open-paint-pail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('tilted', 'open', 'paint', 'pail')

    # Repair: Move the pail left to make room for its detached drop without shrinking the drop.
    # Repair: A true tilted capsule rim with ten-unit separation replaces the pinched oval; body joins the rim at exact circular points.
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

        path('rim',(25,7),[('L',(37,16)),('A',(39,20),5,5,True),('A',(34,25),5,5,True),('A',(31,24),5,5,True),('L',(19,15)),('A',(17,11),5,5,True),('A',(22,6),5,5,True),('A',(25,7),5,5,True)],True)
        path('pail',(17,11),[('L',(6,29)),('L',(6,33)),('A',(12,39),6,6,False),('L',(17,39)),('L',(34,25))]);join('pail','rim')
        path('drop',(38,33),[('C',(42,38),(39,34),(42,35)),('A',(34,38),4,4,True),('C',(38,33),(34,35),(37,34))],True)
