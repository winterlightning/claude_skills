'Two plain human busts stand side by side with separate round heads at the same height. Their broad rounded shoulders overlap slightly in the center and end along a shared horizontal base.\nPlan: Two heads with separate shoulder forms; radius5 heads bottom16, torso apex24 yields exact4 ink gap. Retain two people and overlap; oval heads normalized to circular human vocabulary.\nConstruction reference: human_ref/user.svg and Lucide users original/atomic-debug: circular heads and broad round shoulders; solo group detached-head gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c55ad6d-4ec1-4723-85f5-67fb352b1544'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/sibling_4c55ad6d-4ec1-4723-85f5-67fb352b1544.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pair-of-equal-height-shoulder-busts'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('pair', 'of', 'equal', 'height', 'shoulder', 'busts')

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

        circle('head-left',14,11,5);circle('head-right',34,11,5)
        path('body-left',(6,42),[('L',(6,32)),('A',(14,24),8,8,True),('A',(22,32),8,8,True),('L',(22,42)),('L',(6,42))],True)
        path('body-right',(22,32),[('C',(34,24),(24,26),(28,24)),('A',(42,32),8,8,True),('L',(42,42)),('L',(22,42))]);join('body-left','body-right')
