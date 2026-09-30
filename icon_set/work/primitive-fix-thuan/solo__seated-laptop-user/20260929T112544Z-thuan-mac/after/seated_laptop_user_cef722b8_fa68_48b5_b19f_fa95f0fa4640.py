"""The rejected seated user had an angular chair and square hip. Restored the rounded hip, bent leg and curved chair support while retaining the open laptop and left-facing working pose.
Plan: Human full_body_ref.png: circular head, coherent limbs and exact 4-unit detached head gap; Lucide armchair: rounded seat transitions; laptop: open screen/base. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='cef722b8-fa68-48b5-b19f-fa95f0fa4640'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seated-laptop-user/20260929T112544Z-thuan-mac/reference/work from home user sit_cef722b8-fa68-48b5-b19f-fa95f0fa4640.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='seated-laptop-user'
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

        circle('head',28,9,5)
        line('torso',(28,22),(28,30))
        path('body-leg',(28,30),[('A',(24,34),4,4,True),('L',(17,34)),('A',(13,38),4,4,False),('L',(10,44))]);join('body-leg','torso')
        poly('arm',(28,22),(22,26),(14,26));join('arm','torso')
        poly('screen',(8,14),(12,26),(14,26));join('screen','arm')
        path('chair',(40,20),[('L',(40,34)),('A',(32,42),8,8,True),('L',(28,42))])
        line('seat',(24,34),(40,34));join('seat','chair');join('seat','body-leg')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
