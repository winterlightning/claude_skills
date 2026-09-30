"""The rejected hand is squat with short fingers; restore the tall palm and upright joined fingers. No written reviewer feedback.
Lengthened the upright palm and fingers, widened the thumb, and retained rounded fingertips.
Construction: Lucide hand original and atomic-debug; shared human reference for rounded human parts.
Omissions: Three long fingertips replace four crowded fingers; thumb retained.
Keyshape: SQUARE. Balanced overall composition; centerline extremes (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2642bb02-0d07-4d75-b214-cde16b5f0ce2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__upright-open-hand-with-joined-fingers/20260929T121814Z-thuan-mac/reference/skin_2642bb02-0d07-4d75-b214-cde16b5f0ce2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='upright-open-hand-with-joined-fingers'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('upright', 'open', 'hand', 'with', 'joined', 'fingers')

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

        self.path('hand',(18,28),[('L',(18,12)),('A',(26,12),4,4,True),('L',(26,10)),('A',(34,10),4,4,True),('L',(34,14)),('A',(42,14),4,4,True),('L',(42,28)),('A',(28,42),14,14,True),('C',(10,32),(20,42),(13,36)),('L',(6,24)),('C',(14,20),(6,18),(10,16)),('L',(18,28))],True)
        self.add_line('finger-crease-a',(26,12),(26,26));self.add_line('finger-crease-b',(34,14),(34,26))
        self.relate('connect','finger-crease-a','hand');self.relate('connect','finger-crease-b','hand')
