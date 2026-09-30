"""The rejected car floated above detached wheels and had a short hood stub. Connected the wheels to the chassis, rounded the bumpers and raised a clearly hinged hood. Omitted window divisions.
Plan: Lucide car: rounded body and matched wheels; source raised hood. Keyshape HRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='de4837e9-fc58-4000-be76-deb74b0a3723'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__side-view-car-with-open-hood/20260929T112716Z-thuan-mac/reference/car hood release_de4837e9-fc58-4000-be76-deb74b0a3723.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='side-view-car-with-open-hood'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                members.append(member);here=end
            self.add_contour(name,*members,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*pts): self.add_polyline(name,*pts)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r): path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('body',(4,26),[('L',(4,22)),('A',(8,18),4,4,True),('L',(16,18)),('L',(24,8)),('L',(32,8)),('L',(40,18)),('A',(44,22),4,4,True),('L',(44,26)),('L',(36,26)),('L',(12,26)),('L',(4,26))],True)
        for x in (12,36):
         circle(f'wheel-{x}',x,37,3)
         line(f'axle-{x}',(x,26),(x,34));join(f'axle-{x}','body');join(f'axle-{x}',f'wheel-{x}')
        poly('hood',(16,18),(8,8),(4,8));join('hood','body')
