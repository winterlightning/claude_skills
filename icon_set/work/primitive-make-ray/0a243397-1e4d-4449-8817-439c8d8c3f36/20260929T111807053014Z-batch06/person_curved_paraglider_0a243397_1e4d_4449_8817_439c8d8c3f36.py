"""The rejected paraglider compressed the body and legs into its harness. Raised and deepened the curved canopy, exposed a torso below the suspension junction and lengthened the two hanging legs. Omitted the disconnected canopy-edge stubs.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='0a243397-1e4d-4449-8817-439c8d8c3f36'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-curved-paraglider/20260929T111229Z-thuan-mac/reference/paraglider_0a243397-1e4d-4449-8817-439c8d8c3f36.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-curved-paraglider'
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

        path('canopy',(6,16),[('A',(42,16),18,10,True)])
        poly('suspension-left',(6,16),(14,32),(24,32));poly('suspension-right',(42,16),(34,32),(24,32));join('suspension-left','canopy');join('suspension-right','canopy')
        circle('head',24,20,4)
        line('torso',(24,32),(24,36));join('torso','suspension-left');join('torso','suspension-right')
        poly('legs',(18,42),(24,36),(30,42));join('legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
