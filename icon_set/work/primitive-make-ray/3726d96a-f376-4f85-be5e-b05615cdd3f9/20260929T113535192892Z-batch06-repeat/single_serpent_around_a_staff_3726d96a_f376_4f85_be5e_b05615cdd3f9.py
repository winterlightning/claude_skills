"""The rejected serpent was an undifferentiated S-shaped stroke resembling a currency symbol. Added a rounded snake head and lengthened the lower coil while keeping a single serpent around the upright staff. Omitted the tiny eye and staff finial.
Plan: No useful direct Lucide match; source single winding serpent and upright staff. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='3726d96a-f376-4f85-be5e-b05615cdd3f9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__single-serpent-around-a-staff/20260929T112716Z-thuan-mac/reference/rod of asclepius_3726d96a-f376-4f85-be5e-b05615cdd3f9.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='single-serpent-around-a-staff'
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

        poly('staff',(24,4),(24,12),(24,28),(24,42),(24,44))
        path('snake',(34,12),[('L',(24,12)),('C',(8,20),(12,12),(8,14)),('C',(24,28),(8,26),(15,28)),('C',(38,35),(35,28),(38,30)),('C',(24,42),(38,40),(28,42))]);join('snake','staff')
        circle('head',37,12,3);join('head','snake')
