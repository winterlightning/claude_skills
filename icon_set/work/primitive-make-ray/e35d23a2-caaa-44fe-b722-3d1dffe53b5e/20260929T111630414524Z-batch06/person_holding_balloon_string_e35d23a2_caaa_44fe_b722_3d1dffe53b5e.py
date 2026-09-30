"""The rejected drawing introduced spread walking legs although the reference is a cropped standing torso. Restored the cropped straight torso and relaxed rear arm while retaining the oval balloon, string and bent holding arm.
Plan: Human full_body_ref.png: round head, coherent limbs, vertical head/torso alignment and exact 4-unit ink gap; Lucide balloon: rounded balloon taper and string. Keyshape VRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e35d23a2-caaa-44fe-b722-3d1dffe53b5e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-holding-balloon-string/20260929T111229Z-thuan-mac/reference/hold balloon_e35d23a2-caaa-44fe-b722-3d1dffe53b5e.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='person-holding-balloon-string'
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

        circle('head',13,15,5)
        line('torso',(13,28),(13,44))
        poly('arm',(13,28),(22,33),(33,33));join('arm','torso')
        path('balloon',(33,4),[('C',(40,11),(37,4),(40,7)),('C',(33,23),(40,16),(36,21)),('C',(26,11),(30,21),(26,16)),('C',(33,4),(26,7),(29,4))],True)
        line('string',(33,23),(33,33));join('string','balloon');join('string','arm')
        path('back-arm',(13,28),[('A',(8,33),5,5,False),('L',(8,38))]);join('back-arm','torso');join('back-arm','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
