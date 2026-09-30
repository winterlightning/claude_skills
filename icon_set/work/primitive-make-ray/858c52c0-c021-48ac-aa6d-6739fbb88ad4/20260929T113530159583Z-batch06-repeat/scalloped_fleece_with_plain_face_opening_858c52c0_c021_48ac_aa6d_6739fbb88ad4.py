"""The rejected fleece looked like a rounded square with four notches. Restored repeated scallops around all four sides and retained a plain rounded face opening. Reduced the number of wool lobes to eight.
Plan: No useful direct Lucide match; shared elliptical scallops follow the source fleece. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='858c52c0-c021-48ac-aa6d-6739fbb88ad4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__scalloped-fleece-with-plain-face-opening/20260929T112716Z-thuan-mac/reference/shearling_858c52c0-c021-48ac-aa6d-6739fbb88ad4.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='scalloped-fleece-with-plain-face-opening'
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

        path('fleece',(12,10),[('A',(24,10),6,4,True),('A',(36,10),6,4,True),('L',(38,12)),('A',(38,24),4,6,True),('A',(38,36),4,6,True),('L',(36,38)),('A',(24,38),6,4,True),('A',(12,38),6,4,True),('L',(10,36)),('A',(10,24),4,6,True),('A',(10,12),4,6,True),('L',(12,10))],True)
        path('face',(19,19),[('L',(29,19)),('L',(29,24)),('A',(19,24),5,5,True),('L',(19,19))],True)
