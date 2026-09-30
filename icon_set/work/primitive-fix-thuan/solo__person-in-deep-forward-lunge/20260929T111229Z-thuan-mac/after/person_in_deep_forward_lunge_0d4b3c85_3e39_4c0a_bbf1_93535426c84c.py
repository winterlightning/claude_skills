"""The rejected pose had a straight horizontal arm and rigid square leg turns. Restored the bent forward arm and rounded front knee while keeping the low rear leg and deep lunge.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap. Keyshape HRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='0d4b3c85-3e39-4c0a-bbf1-93535426c84c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-in-deep-forward-lunge/20260929T111229Z-thuan-mac/reference/lunge_0d4b3c85-3e39-4c0a-bbf1-93535426c84c.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-in-deep-forward-lunge'
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

        circle('head',22,12,4)
        line('torso',(22,24),(22,32))
        poly('arm',(22,24),(30,24),(38,20));join('arm','torso')
        path('legs',(4,40),[('L',(15,40)),('A',(19,38),5,5,False),('L',(22,32)),('L',(33,32)),('A',(37,36),4,4,True),('L',(37,40)),('L',(44,40))]);join('legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
