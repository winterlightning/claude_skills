"""The rejected large fish was a thin crescent. Broadened its body by making the open mouth shallower, and retained the distinct smaller fish with a tail. Omitted eye and gill details.
Plan: Lucide fish: broad curved body with a simple tail. Keyshape HRECT_M; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='ef3909ee-ca34-4bc7-88ca-385329aa590a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__large-fish-pursuing-small-fish/20260929T110722Z-thuan-mac/reference/business big small fish_ef3909ee-ca34-4bc7-88ca-385329aa590a.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='large-fish-pursuing-small-fish'
    keyshape=Keyshape.HRECT_M
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

        path('large',(28,10),[('C',(10,24),(16,10),(10,16)),('C',(28,38),(10,32),(16,38)),('L',(23,24)),('L',(28,10))],True)
        poly('tail',(4,16),(10,24),(4,32));join('tail','large')
        circle('small',40,24,4)
        poly('small-tail',(33,20),(36,24),(33,28));join('small-tail','small')
