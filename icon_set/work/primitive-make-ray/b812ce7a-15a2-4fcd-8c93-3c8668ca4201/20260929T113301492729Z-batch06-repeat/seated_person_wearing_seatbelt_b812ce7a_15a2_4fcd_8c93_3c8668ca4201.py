"""The rejected seated body looked like a square crossed-out symbol. Rounded the shoulders around the detached head and preserved the diagonal seatbelt, hanging legs and seat edges. Head outline y14 to shoulders y22 leaves exactly four ink units.
Plan: Human user.svg: rounded shoulders and detached circular head; source diagonal restraint. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='b812ce7a-15a2-4fcd-8c93-3c8668ca4201'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seated-person-wearing-seatbelt/20260929T112716Z-thuan-mac/reference/fasten seal belt_b812ce7a-15a2-4fcd-8c93-3c8668ca4201.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='seated-person-wearing-seatbelt'
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

        circle('head',24,9,5)
        path('shoulders',(12,36),[('L',(12,26)),('A',(16,22),4,4,True),('L',(24,22)),('L',(32,22)),('A',(36,26),4,4,True),('L',(36,36))])
        poly('left-leg',(12,36),(12,40),(12,44),(20,44));join('left-leg','shoulders')
        poly('right-leg',(36,36),(36,44),(28,44));join('right-leg','shoulders')
        line('belt',(36,26),(12,40));join('belt','shoulders');join('belt','left-leg')
        line('seat-left',(8,36),(12,36));line('seat-right',(36,36),(40,36));join('seat-left','shoulders');join('seat-right','shoulders');join('seat-left','left-leg');join('seat-right','right-leg')
