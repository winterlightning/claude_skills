'A continuous U-shaped curve rises into two upward pointing arrowheads at different heights. The right stem extends much higher than the left, above a broad rounded lower bend.\nPlan: Unequal-height upward ends on one smooth U bend.\nConstruction reference: Lucide arrow-up original and atomic-debug: open arrowheads joined to shaft.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64aa2f6c-f55b-4f9f-8700-1818ea4550e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/button arrow curve_64aa2f6c-f55b-4f9f-8700-1818ea4550e2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arrow-with-unequal-upward-ends'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('arrow', 'with', 'unequal', 'upward', 'ends')

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

        path('u',(14,22),[('L',(14,32)),('A',(34,32),10,10,False),('L',(34,6))])
        poly('left',(6,30),(14,22),(22,30));poly('right',(26,14),(34,6),(42,14));join('left','u');join('right','u')
