"""The rejected pose had a rigid rectangular arm and a low detached head far left of the knees. Moved the aligned head and torso toward the folded knees and softened the seated back, with the arm wrapping toward the knee.
Plan: Human full_body_ref.png: circular head, coherent limbs and exact 4-unit detached head gap. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='2739b613-55fd-4f47-af97-f5cf90cb523d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seated-curled-person-solo-2739b613/20260929T112544Z-thuan-mac/reference/poverty person_2739b613-55fd-4f47-af97-f5cf90cb523d.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='seated-curled-person-solo-2739b613'
    keyshape=Keyshape.VRECT_L
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

        circle('head',16,12,6)
        line('torso',(16,26),(16,32))
        path('seat',(16,32),[('A',(24,42),10,10,False)]);join('seat','torso')
        poly('legs',(24,42),(32,30),(40,42));join('legs','seat')
        poly('arm',(16,26),(28,26),(32,30));join('arm','torso');join('arm','legs')
