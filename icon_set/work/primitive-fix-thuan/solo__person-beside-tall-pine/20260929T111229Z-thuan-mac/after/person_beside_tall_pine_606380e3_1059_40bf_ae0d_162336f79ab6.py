"""The rejected figure had a small head and diagonally spread arms, unlike the standing reference. Enlarged the head and lowered both arms beside the torso; broadened the lower pine tier. Kept two tiers to avoid crowded branch notches.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap; Lucide tree-pine: tiered outline and central trunk. Keyshape HRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='606380e3-1059-40bf-ae0d-162336f79ab6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-beside-tall-pine/20260929T111229Z-thuan-mac/reference/camping trekking tree_606380e3-1059-40bf-ae0d-162336f79ab6.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-beside-tall-pine'
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

        circle('head',10,13,5)
        line('torso',(10,26),(10,34));poly('arms',(4,30),(10,26),(16,30));join('arms','torso')
        poly('legs',(6,40),(10,34),(14,40));join('legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        poly('tree',(34,8),(42,20),(38,20),(44,32),(34,32),(24,32),(30,20),(26,20),(34,8))
        line('trunk',(34,32),(34,40));join('trunk','tree')
