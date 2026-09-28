"""A side-parted head with a long curling beard beside a three-pronged trident. Bounds (4,8)-(44,40). Three prongs share step8; small portrait retains flowing beard tips.
Construction reference: Human user.svg: coherent head outline; Lucide utensils: U-shaped tines and central shaft.
Omissions: Tiny facial marks omitted to retain readable beard and trident."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7de24ead-f89e-4e55-9f1f-a90902058d8e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__bearded-poseidon-with-trident/20260924T101756Z-thuan-mac/reference/poseidon_7de24ead-f89e-4e55-9f1f-a90902058d8e.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='bearded-poseidon-with-trident'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('poseidon',)
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('portrait',(5,15),[('L',(5,12)),('A',(9,8),4,4,True),('L',(15,8)),('A',(19,12),4,4,True),('L',(19,24)),('C',(24,32),(19,28),(21,31)),('C',(18,32),(22,33),(20,33)),('C',(21,39),(18,35),(19,37)),('C',(12,35),(17,40),(14,37)),('C',(5,40),(10,39),(7,40)),('C',(7,32),(8,37),(8,34)),('L',(4,33)),('C',(5,24),(5,30),(5,27)),('L',(5,15))],True)
        path('beard-top',(5,24),[('C',(19,24),(9,18),(15,18))]);join('beard-top','portrait')
        path('hair',(5,15),[('C',(12,10),(9,15),(11,12)),('C',(19,15),(13,13),(16,15))]);join('hair','portrait')
        path('prongs',(28,8),[('L',(28,16)),('A',(36,24),8,8,False),('A',(44,16),8,8,False),('L',(44,8))])
        line('shaft',(36,8),(36,40));join('shaft','prongs')
