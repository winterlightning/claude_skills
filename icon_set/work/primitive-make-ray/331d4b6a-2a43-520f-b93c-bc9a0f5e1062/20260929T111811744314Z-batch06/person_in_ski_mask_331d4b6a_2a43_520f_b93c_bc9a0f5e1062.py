"""The rejected mask had one goggle-shaped opening unlike the source two eye holes. Restored two separate round eye openings with a centered mouth and symmetric balaclava silhouette.
Plan: Human user.svg: head and shoulders; Lucide venetian-mask: paired eye placement. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='331d4b6a-2a43-520f-b93c-bc9a0f5e1062'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-in-ski-mask/20260929T111229Z-thuan-mac/reference/tools criminal mask_331d4b6a-2a43-520f-b93c-bc9a0f5e1062.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-in-ski-mask'
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

        path('hood',(8,44),[('A',(14,38),6,6,True),('L',(14,36)),('A',(8,30),6,6,True),('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,30)),('A',(34,36),6,6,True),('L',(34,38)),('A',(40,44),6,6,True)])
        circle('eye-left',18,20,2);circle('eye-right',30,20,2)
        line('mouth',(21,31),(27,31))
