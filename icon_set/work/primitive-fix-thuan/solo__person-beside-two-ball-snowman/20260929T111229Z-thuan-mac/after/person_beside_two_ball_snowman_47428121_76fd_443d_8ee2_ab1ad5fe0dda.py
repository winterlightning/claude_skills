"""The rejected person extended the longer arm away from the snowman. Repositioned the figure and extended its left arm toward the snowman, retaining two rounded snowballs and the standing pose. Omitted the thin snowman twig.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap. Keyshape HRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='47428121-76fd-443d-8ee2-ab1ad5fe0dda'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-beside-two-ball-snowman/20260929T111229Z-thuan-mac/reference/build snowman_47428121-76fd-443d-8ee2-ab1ad5fe0dda.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-beside-two-ball-snowman'
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

        path('snowman',(10,22),[('C',(6,16),(6,20),(6,18)),('A',(14,8),8,8,True),('A',(22,16),8,8,True),('C',(18,22),(22,18),(22,20)),('C',(24,30),(22,24),(24,26)),('C',(14,40),(24,36),(20,40)),('C',(4,30),(8,40),(4,36)),('C',(10,22),(4,26),(6,24))],True)
        circle('head',38,12,4)
        line('torso',(38,24),(38,32));poly('arms',(31,24),(38,24),(44,30));join('arms','torso')
        poly('legs',(34,40),(38,32),(42,40));join('legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
