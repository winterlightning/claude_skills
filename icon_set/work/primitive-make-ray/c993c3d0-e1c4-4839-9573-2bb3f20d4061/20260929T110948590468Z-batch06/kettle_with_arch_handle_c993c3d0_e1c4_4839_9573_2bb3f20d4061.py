"""The rejected kettle had a flat rectangular body and angular side loop. Restored the domed body, broad overhead handle and rising pouring spout; omitted the tiny lid knob.
Plan: Lucide cooking-pot: coherent vessel outline and attached handle. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='c993c3d0-e1c4-4839-9573-2bb3f20d4061'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__kettle-with-arch-handle/20260929T110722Z-thuan-mac/reference/kettle_c993c3d0-e1c4-4839-9573-2bb3f20d4061.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='kettle-with-arch-handle'
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

        path('body',(6,32),[('A',(18,20),12,12,True),('A',(30,32),12,12,True),('L',(30,42)),('L',(6,42)),('L',(6,32))],True)
        path('handle',(6,32),[('L',(6,14)),('A',(14,6),8,8,True),('L',(22,6)),('A',(30,14),8,8,True),('L',(30,32))])
        join('body','handle')
        path('spout',(30,32),[('L',(38,22)),('L',(42,22)),('L',(40,34)),('L',(30,42))]);join('spout','body')
