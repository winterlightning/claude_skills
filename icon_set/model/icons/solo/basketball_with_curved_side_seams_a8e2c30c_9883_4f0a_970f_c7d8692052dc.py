'A round basketball is divided by a vertical and a horizontal seam crossing at its center. Two inward-curving side seams bow between the upper and lower edges of the ball.\nPlan: Basketball with crossing main seams and two bowed side seams, organized about shared cardinal nodes.\nConstruction reference: No useful exact Lucide match; source-specific construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8e2c30c-9883-4f0a-970f-c7d8692052dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/basketball_a8e2c30c-9883-4f0a-970f-c7d8692052dc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'basketball-with-curved-side-seams'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('basketball', 'with', 'curved', 'side', 'seams')

    # Repair: Split rim at the 12-16-20 circle attachment points and side seams at the horizontal junction.
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

        path('rim',(4,24),[('A',(8,12),20,20,True),('A',(24,4),20,20,True),('A',(40,12),20,20,True),('A',(44,24),20,20,True),('A',(40,36),20,20,True),('A',(24,44),20,20,True),('A',(8,36),20,20,True),('A',(4,24),20,20,True)],True)
        poly('vertical',(24,4),(24,24),(24,44));poly('horizontal',(4,24),(16,24),(24,24),(32,24),(44,24))
        join('rim','vertical');join('rim','horizontal');join('vertical','horizontal')
        path('left-seam',(8,12),[('C',(16,24),(12,14),(16,18)),('C',(8,36),(16,30),(12,34))])
        path('right-seam',(40,12),[('C',(32,24),(36,14),(32,18)),('C',(40,36),(32,30),(36,34))])
        for name in ('left-seam','right-seam'):join(name,'rim');join(name,'horizontal')
