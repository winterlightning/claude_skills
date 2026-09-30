"""The rejected uniform pockets are chevrons and the collar is a simple notch; restore two actual pocket outlines and a tailored collar. No written reviewer feedback.
Symbol plan: Lucide shirt: symmetric shoulders and body. Two outlined pockets retain the uniform identity; fine flap seams and button placket omitted.
Keyshape SQUARE, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='591915da-b4b5-4520-b0bf-1658414b5875'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__uniform-shirt-with-two-pockets/20260929T121814Z-thuan-mac/reference/fatigues_591915da-b4b5-4520-b0bf-1658414b5875.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='uniform-shirt-with-two-pockets'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('uniform', 'shirt', 'with', 'two', 'pockets')

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

        self.path('shirt',(16,6),[('C',(6,20),(8,6),(6,12)),('L',(6,42)),('L',(42,42)),('L',(42,20)),('C',(32,6),(42,12),(40,6)),('L',(16,6))],True)
        self.add_polyline('collar',(16,6),(24,14),(32,6));self.relate('connect','collar','shirt')
        for x in (18,30):
            self.add_polyline(f'pocket-{x}',(x-4,24),(x+4,24),(x+4,32),(x-4,32),closed=True)
