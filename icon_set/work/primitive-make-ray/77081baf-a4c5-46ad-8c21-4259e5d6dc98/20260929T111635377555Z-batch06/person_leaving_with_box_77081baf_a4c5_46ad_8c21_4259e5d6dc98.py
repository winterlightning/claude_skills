"""The rejected box seemed suspended from a short diagonal line. Bent the arm beneath the box so the person visibly carries it and rounded the doorway corners. Kept the departing stride and omitted the small door knob.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='77081baf-a4c5-46ad-8c21-4259e5d6dc98'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-leaving-with-box/20260929T111229Z-thuan-mac/reference/worker lay off fired user sad door box_77081baf-a4c5-46ad-8c21-4259e5d6dc98.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-leaving-with-box'
    keyshape=Keyshape.SQUARE
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

        path('door',(18,42),[('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(22,6))])
        circle('head',32,14,4)
        line('torso',(32,26),(32,32));poly('legs',(28,42),(32,32),(42,42));join('legs','torso')
        poly('box',(16,24),(24,24),(24,32),(16,32),(16,24))
        poly('arm',(32,26),(30,32),(24,32));join('arm','torso');join('arm','box')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
