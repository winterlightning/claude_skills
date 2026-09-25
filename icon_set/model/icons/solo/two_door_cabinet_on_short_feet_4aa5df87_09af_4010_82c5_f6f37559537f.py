'A low cabinet stands on two short rounded feet beneath a broad rectangular body. Two inset doors meet at the center, each carrying a small upright handle beside the shared seam.\nPlan: Two-door cabinet with center seam and short feet. Box4,8–44,40; omit tiny handles.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4aa5df87-09af-4010-82c5-f6f37559537f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/credenza_4aa5df87-09af-4010-82c5-f6f37559537f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-door-cabinet-on-short-feet'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'door', 'cabinet', 'on', 'short', 'feet')

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

        poly('body',(4,8),(24,8),(44,8),(44,32),(36,32),(24,32),(12,32),(4,32),(4,8))
        line('seam',(24,8),(24,32));join('seam','body')
        line('leg-l',(12,32),(12,40));line('leg-r',(36,32),(36,40));join('leg-l','body');join('leg-r','body')
