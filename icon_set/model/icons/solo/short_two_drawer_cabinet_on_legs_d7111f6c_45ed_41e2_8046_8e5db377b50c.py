'A squat cabinet has a straight projecting top and rounded lower corners. Two broad inset drawers contain short horizontal pulls, and a pair of small legs extends below the body.\nPlan: Two drawer faces and integrated finger notches; feet attached to base.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7111f6c-45ed-41e2-8046-8e5db377b50c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/archive drawer table_d7111f6c-45ed-41e2-8046-8e5db377b50c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'short-two-drawer-cabinet-on-legs'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('short', 'two', 'drawer', 'cabinet', 'on', 'legs')

    # Repair: Restore a separate integrated finger notch on each drawer without crowding either drawer face.
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

        path('body',(4,8),[('L',(20,8)),('A',(28,8),4,4,False),('L',(44,8)),('L',(44,20)),('L',(44,32)),('L',(36,32)),('L',(12,32)),('L',(4,32)),('L',(4,20)),('L',(4,8))],True)
        path('divider',(4,20),[('L',(20,20)),('A',(28,20),4,4,False),('L',(44,20))]);join('divider','body')
        line('leg-l',(12,32),(12,40));line('leg-r',(36,32),(36,40));join('leg-l','body');join('leg-r','body')
