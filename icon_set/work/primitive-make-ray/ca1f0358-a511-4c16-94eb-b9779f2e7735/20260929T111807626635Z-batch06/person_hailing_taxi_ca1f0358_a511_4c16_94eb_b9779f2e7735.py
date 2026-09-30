"""The rejected taxi looked like stacked square blocks with an oversized roof sign. Rounded the car body and reduced the roof sign to a clear bar while retaining the raised hailing arm. Omitted lamps at this size.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap; Lucide car-taxi-front: curved body and small roof sign. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='ca1f0358-a511-4c16-94eb-b9779f2e7735'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-hailing-taxi/20260929T111229Z-thuan-mac/reference/taxi wave_ca1f0358-a511-4c16-94eb-b9779f2e7735.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-hailing-taxi'
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

        circle('head',10,10,4)
        line('torso',(10,22),(10,32));poly('legs',(6,42),(10,32),(14,42));join('legs','torso')
        poly('arms',(6,30),(10,22),(18,22),(24,8));join('arms','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        path('car',(26,30),[('L',(30,22)),('L',(38,22)),('L',(42,30)),('L',(42,36)),('A',(40,38),2,2,True),('L',(28,38)),('A',(26,36),2,2,True),('L',(26,30))],True)
        line('sign',(31,14),(37,14))
        line('hood',(26,30),(42,30));join('hood','car')
        line('tire-left',(28,38),(28,42));line('tire-right',(40,38),(40,42));join('tire-left','car');join('tire-right','car')
