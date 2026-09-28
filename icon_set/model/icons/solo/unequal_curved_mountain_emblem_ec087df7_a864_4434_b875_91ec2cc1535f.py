'Two pointed forms rise from a common horizontal level, with the larger peak on the right. Their inward-facing edges bow smoothly, while the outer slopes stay mostly straight.\nPlan: Two unequal curved peaks preserve broad asymmetric emblem.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec087df7-a864-4434-b875-91ec2cc1535f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/atlassian logo_ec087df7-a864-4434-b875-91ec2cc1535f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unequal-curved-mountain-emblem'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('unequal', 'curved', 'mountain', 'emblem')

    # Repair: Separate inward bowed slopes without changing the two unequal peaks.
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

        path('left',(4,40),[('L',(12,24)),('C',(16,40),(20,32),(16,36)),('L',(4,40))],True)
        path('right',(28,8),[('L',(44,40)),('L',(32,40)),('C',(28,8),(26,24),(20,22))],True)
