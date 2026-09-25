'A bikini top and matching bottom are arranged vertically. The top has two rounded triangular cups and narrow shoulder straps, while the bottom curves inward toward a narrow crotch.\nPlan: Two bikini cups and separate curved bottom; mirror around24 and retain straps.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5002effe-d0b9-44d4-bf7e-f04e426d4473'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bikini_5002effe-d0b9-44d4-bf7e-f04e426d4473.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-piece-bikini-set'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'piece', 'bikini', 'set')

    # Repair: Use contained cup curves and lower the bottom for clear separation.
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

        path('left-cup',(14,12),[('C',(24,22),(18,14),(22,18)),('C',(8,22),(16,28),(8,28)),('L',(14,12))],True)
        path('right-cup',(34,12),[('L',(40,22)),('C',(24,22),(40,28),(32,28)),('C',(34,12),(28,18),(30,14))],True);join('left-cup','right-cup')
        line('strap-left',(14,4),(14,12));line('strap-right',(34,4),(34,12));join('strap-left','left-cup');join('strap-right','right-cup')
        path('bottom',(8,36),[('L',(40,36)),('C',(28,44),(34,38),(30,42)),('L',(20,44)),('C',(8,36),(18,42),(14,38))],True)
