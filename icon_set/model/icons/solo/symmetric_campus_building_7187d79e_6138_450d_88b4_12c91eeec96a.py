'A campus building has a raised central section topped by a triangular roof. An arched doorway and upper arched window align between two lower wings with square windows.\nPlan: Raised central campus block with pitched roof and lower wings; central arch.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7187d79e-6138-450d-88b4-12c91eeec96a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/campus_7187d79e-6138-450d-88b4-12c91eeec96a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'symmetric-campus-building'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('symmetric', 'campus', 'building')

    # Repair: Retain all three window positions as compact marks, with a smaller central arched doorway.
    # Repair: Raise the doorway apex to preserve an open arch above the baseline and space the upper window clear of it.
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

        poly('building',(4,40),(4,24),(14,24),(14,16),(24,8),(34,16),(34,24),(44,24),(44,40),(28,40),(20,40),(4,40))
        path('door',(20,40),[('L',(20,34)),('A',(28,34),4,4,True),('L',(28,40))]);join('door','building')
        line('upper-window',(24,19),(24,20))
        self.add_dot('left-window',(12,32));self.add_dot('right-window',(36,32))
