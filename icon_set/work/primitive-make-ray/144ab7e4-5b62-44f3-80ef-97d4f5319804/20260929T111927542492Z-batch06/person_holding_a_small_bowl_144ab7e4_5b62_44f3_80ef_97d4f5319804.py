"""The rejected arm sloped down away from the body instead of crossing in front as in the source. Redrew a bent rounded arm across the torso to support the bowl, with a larger centered head.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='144ab7e4-5b62-44f3-80ef-97d4f5319804'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-holding-a-small-bowl/20260929T111229Z-thuan-mac/reference/beggar_144ab7e4-5b62-44f3-80ef-97d4f5319804.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-holding-a-small-bowl'
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

        circle('head',17,10,6)
        line('torso',(17,24),(17,44))
        path('arm',(17,24),[('L',(12,24)),('A',(8,28),4,4,False),('L',(8,32)),('A',(12,36),4,4,False),('L',(26,36))]);join('arm','torso')
        path('bowl',(26,36),[('L',(40,36)),('A',(26,36),7,7,True)],True);join('bowl','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
