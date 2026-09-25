'A tulip bloom has three rounded pointed petals overlapping above a straight stalk. Two broad leaves extend outward near its base, with the right leaf sitting slightly lower.\nPlan: Tulip cup with three-point crown, straight stem and two open leaf curves.\nConstruction reference: Lucide flower-2 original and atomic-debug: simple stem and symmetric leaf curves.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf688152-38d6-4d2c-84e0-5399edca85e8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bud_bf688152-38d6-4d2c-84e0-5399edca85e8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tulip-with-two-spreading-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tulip', 'with', 'two', 'spreading', 'leaves')

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

        path('flower',(14,6),[('L',(20,10)),('L',(24,4)),('L',(28,10)),('L',(34,6)),('L',(34,14)),('A',(24,24),10,10,True),('A',(14,14),10,10,True),('L',(14,6))],True)
        poly('stem',(24,24),(24,40),(24,44));join('stem','flower')
        path('left',(8,28),[('C',(24,40),(8,38),(16,40))]);path('right',(40,28),[('C',(24,40),(40,38),(32,40))]);join('left','stem');join('right','stem');join('left','right')
