"""The rejected embrace was one straight diagonal stroke ending loosely. Curved the embracing arm into a rounded hand reaching across the other person, keeping the adjacent heads and broad shoulders. Both detached heads retain four ink units to their own shoulders.
Plan: Human user.svg: round heads and broad shoulders; source arm crossing its neighbor. Keyshape HRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e9273110-9f8b-46ca-8cfa-ca10641cf14b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__side-by-side-hug/20260929T112716Z-thuan-mac/reference/hugger_e9273110-9f8b-46ca-8cfa-ca10641cf14b.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='side-by-side-hug'
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

        for x in (14,34):circle(f'head-{x}',x,14,6)
        path('left-body',(4,40),[('L',(4,38)),('C',(14,28),(4,32),(8,28))])
        path('right-body',(34,28),[('A',(44,38),10,10,True),('L',(44,40))])
        path('embrace',(14,28),[('C',(32,40),(20,30),(26,39))]);join('embrace','left-body')
