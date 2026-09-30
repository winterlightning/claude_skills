"""The rejected horn was a tilted rectangular megaphone detached from the supporting gesture. Restored a broad curved flare and a clear mouthpiece held by the bent arm; kept the kneeling legs.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap; Lucide megaphone: flared bell and narrow mouthpiece. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='507a15ed-aace-4478-ab31-b39936e3a104'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-holding-horn-to-face/20260929T111229Z-thuan-mac/reference/blow instrument_507a15ed-aace-4478-ab31-b39936e3a104.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-holding-horn-to-face'
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

        circle('head',36,12,6)
        line('torso',(36,26),(36,34))
        poly('legs',(36,42),(36,34),(20,34),(20,42),(10,42));join('legs','torso')
        poly('arm',(36,26),(24,26),(22,18));join('arm','torso')
        path('horn',(6,6),[('C',(22,12),(12,10),(18,12)),('L',(22,18)),('C',(6,22),(16,18),(10,20)),('L',(6,6))],True);join('horn','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
