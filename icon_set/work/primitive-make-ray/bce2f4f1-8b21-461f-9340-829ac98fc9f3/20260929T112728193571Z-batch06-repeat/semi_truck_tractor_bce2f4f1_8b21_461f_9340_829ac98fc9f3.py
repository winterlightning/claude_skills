"""The rejected tractor cab was undersized and its wheels hung on long stalks. Enlarged and rounded the cab, lowered the chassis toward the wheels and rebuilt the side window. Retained all three axles.
Plan: Lucide truck: rounded cab corners and wheels close to the chassis. Keyshape HRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='bce2f4f1-8b21-461f-9340-829ac98fc9f3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__semi-truck-tractor/20260929T112544Z-thuan-mac/reference/truck cargo 1_bce2f4f1-8b21-461f-9340-829ac98fc9f3.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='semi-truck-tractor'
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

        for j,x in enumerate((7,21,40)):
         circle(f'wheel-{j}',x,37,3)
        path('cab',(26,29),[('L',(26,8)),('L',(32,8)),('A',(38,14),6,6,True),('L',(40,16)),('L',(44,24)),('L',(44,29)),('L',(40,29)),('L',(26,29))],True)
        poly('chassis',(4,29),(7,29),(21,29),(26,29));join('chassis','cab')
        for j,x in enumerate((7,21,40)):
         line(f'axle-{j}',(x,29),(x,34));join(f'axle-{j}',f'wheel-{j}');join(f'axle-{j}','cab' if j==2 else 'chassis')
        poly('window',(34,16),(34,24),(44,24));join('window','cab')
