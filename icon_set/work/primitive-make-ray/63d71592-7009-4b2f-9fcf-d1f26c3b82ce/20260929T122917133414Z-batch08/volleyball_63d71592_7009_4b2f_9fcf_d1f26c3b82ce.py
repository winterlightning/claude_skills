"""The rejected ball has only three broad panels; restore the repeated curved volleyball seams. No written reviewer feedback.
Restored a fourth flowing panel seam and complete shared seam junctions.
Construction: Lucide volleyball original and atomic-debug: curved panel seams and shared junctions.
Omissions: Four broad seams replace six finer source seams.
Keyshape: CIRCLE. Radial centerline limit 20 around (24,24), preserving the natural circular or slender subject proportions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='63d71592-7009-4b2f-9fcf-d1f26c3b82ce'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__volleyball/20260929T121814Z-thuan-mac/reference/volleyball_63d71592-7009-4b2f-9fcf-d1f26c3b82ce.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='volleyball'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('volleyball',)

    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def build(self):

        self.circle('ball',24,24,20)
        self.path('main',(24,4),[('C',(20,24),(15,7),(14,18)),('C',(44,24),(28,19),(36,19))])
        self.path('lower',(20,24),[('C',(28,34),(25,27),(28,31)),('C',(24,44),(28,38),(27,41))]);self.relate('connect','main','lower')
        self.relate('connect','main','ball');self.relate('connect','lower','ball')
        self.path('left-panel',(4,24),[('C',(28,34),(10,35),(18,38))]);self.relate('connect','left-panel','ball');self.relate('connect','left-panel','lower')
