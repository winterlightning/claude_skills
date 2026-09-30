"""The rejected person had outstretched horizontal arms and a bowl-like ground ring. Lowered both arms toward the sides and flattened the ground ellipse around the feet to suggest a marked location.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='49e0b9d1-bc0c-4794-9bf3-4015f1ce8d7a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-location/20260929T111229Z-thuan-mac/reference/location user_49e0b9d1-bc0c-4794-9bf3-4015f1ce8d7a.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-location'
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

        circle('head',24,9,5)
        line('torso',(24,22),(24,29));poly('arms',(16,28),(16,24),(24,22),(32,24),(32,28));join('arms','torso')
        poly('legs',(20,34),(24,29),(28,34));join('legs','torso')
        path('ground',(12,31),[('C',(8,37),(9,33),(8,35)),('C',(24,44),(8,41),(15,44)),('C',(40,37),(33,44),(40,41)),('C',(36,31),(40,35),(39,33))])
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
