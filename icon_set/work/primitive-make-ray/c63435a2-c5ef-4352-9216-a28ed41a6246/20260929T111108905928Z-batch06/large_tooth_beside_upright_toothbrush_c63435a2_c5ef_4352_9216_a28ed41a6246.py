"""The rejected tooth had angular roots and a sharp crown dip. Redrew a smooth crown and rounded separated roots with a wide central opening beside the upright toothbrush.
Plan: No useful direct match. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='c63435a2-c5ef-4352-9216-a28ed41a6246'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__large-tooth-beside-upright-toothbrush/20260929T110722Z-thuan-mac/reference/dentist_c63435a2-c5ef-4352-9216-a28ed41a6246.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='large-tooth-beside-upright-toothbrush'
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

        path('tooth',(6,16),[('C',(14,6),(6,6),(10,6)),('C',(22,6),(18,9),(18,9)),('C',(30,16),(26,6),(30,6)),('L',(30,36)),('A',(22,36),4,6,True),('L',(22,30)),('A',(14,30),4,4,False),('L',(14,36)),('A',(6,36),4,6,True),('L',(6,16))],True)
        poly('brush',(42,42),(42,30),(42,22),(38,22))
        line('bristle',(38,30),(42,30));join('brush','bristle')
