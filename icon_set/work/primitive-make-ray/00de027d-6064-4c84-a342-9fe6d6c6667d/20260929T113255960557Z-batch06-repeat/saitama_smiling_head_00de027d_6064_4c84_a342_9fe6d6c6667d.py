"""The rejected Saitama head was a generic round smiley. Restored the taller bald head and lower jaw proportions with small ears, understated eyes and an open smile. Omitted the fine nose and brows.
Plan: Human user.svg: rounded head; Lucide face-slightly-smiling: sparse facial placement. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='00de027d-6064-4c84-a342-9fe6d6c6667d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__saitama-smiling-head/20260929T112716Z-thuan-mac/reference/onepunchman saitama_00de027d-6064-4c84-a342-9fe6d6c6667d.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='saitama-smiling-head'
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

        path('face',(10,24),[('L',(10,18)),('A',(38,18),14,14,True),('L',(38,24)),('L',(38,30)),('A',(10,30),14,14,True),('L',(10,24))],True)
        line('ear-left',(8,24),(10,24));line('ear-right',(38,24),(40,24));join('ear-left','face');join('ear-right','face')
        self.add_dot('eye-left',(19,17));self.add_dot('eye-right',(29,17))
        path('smile',(18,28),[('L',(30,28)),('A',(18,28),6,6,True)],True)
