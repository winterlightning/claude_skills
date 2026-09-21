'Two people appear as circular heads above rounded shoulder blocks. The left figure is slightly taller and wider, with its shoulder overlapping the upper left edge of the smaller right torso.\nPlan: Two heads with separate shoulder forms; radius5 heads bottom16, torso apex24 yields exact4 ink gap. Retain two people and overlap; oval heads normalized to circular human vocabulary.\nConstruction reference: human_ref/user.svg and Lucide users original/atomic-debug: circular heads and broad round shoulders; solo group detached-head gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a33b1513-8e9a-47e2-bfc0-67370010520d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/roommate_a33b1513-8e9a-47e2-bfc0-67370010520d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-adjacent-person-busts'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('two', 'adjacent', 'person', 'busts')

    # Repair: Retain the larger left foreground head and smaller rear figure. Both head bottoms18 and shoulder apex26 give exact4 ink gaps.
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

        circle('head-left',14,12,6);circle('head-right',34,13,5)
        path('body-left',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('A',(22,34),8,8,True),('L',(22,42)),('L',(6,42))],True)
        path('body-right',(22,34),[('C',(34,26),(24,28),(28,26)),('A',(42,34),8,8,True),('L',(42,42)),('L',(22,42))]);join('body-left','body-right')
