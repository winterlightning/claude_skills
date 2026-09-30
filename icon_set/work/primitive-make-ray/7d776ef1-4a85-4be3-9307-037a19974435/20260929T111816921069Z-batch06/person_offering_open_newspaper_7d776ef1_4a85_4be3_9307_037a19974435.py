"""The rejected supporting arm had a sharp elbow and the pages appeared stiff. Rounded the extended forearm into a supporting hand while preserving the open two-page sheet and central fold; omitted tiny printed text.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap; Lucide book-open: paired pages around a shared fold. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='7d776ef1-4a85-4be3-9307-037a19974435'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-offering-open-newspaper/20260929T111229Z-thuan-mac/reference/newspaper give_7d776ef1-4a85-4be3-9307-037a19974435.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-offering-open-newspaper'
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

        circle('head',10,10,4)
        poly('torso',(10,22),(10,24),(10,42))
        path('arm',(10,24),[('L',(16,34)),('A',(22,38),7,7,False),('L',(32,38))]);join('arm','torso')
        poly('paper',(24,16),(33,12),(42,16),(42,28),(33,24),(24,28),(24,16))
        line('fold',(33,12),(33,24));join('fold','paper')
        self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
