'A typewriter holds a tall sheet with one folded upper corner behind its carriage. A broad lower housing has a curved central recess, with short roller ends projecting sideways.\nPlan: Typewriter housing, paper with folded corner, short roller ends; open paper recess. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e6749e6-21e4-420f-8e6f-915643ba5e1f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/content typing machine 1_8e6749e6-21e4-420f-8e6f-915643ba5e1f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'typewriter-with-folded-corner-paper'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('typewriter', 'with', 'folded', 'corner', 'paper')

    # Repair: Omit the tiny folded-corner triangle after its opening failed; preserve tall paper and the typewriter carriage recess.
    # Repair: Restore projecting roller ends around the tall sheet and narrow the lower housing so the source reads as a typewriter rather than a plain paper tray.
    # Repair: Restore projecting roller ends around the tall sheet and retain the broad lower housing so the source reads as a typewriter rather than a plain paper tray.
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

        poly('paper',(14,26),(14,18),(14,6),(34,6),(34,18),(34,26))
        path('body',(6,26),[('L',(14,26)),('C',(34,26),(16,36),(32,36)),('L',(42,26)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,26))],True);join('body','paper')
        line('roller-left',(6,18),(14,18));line('roller-right',(34,18),(42,18));join('roller-left','paper');join('roller-right','paper')
