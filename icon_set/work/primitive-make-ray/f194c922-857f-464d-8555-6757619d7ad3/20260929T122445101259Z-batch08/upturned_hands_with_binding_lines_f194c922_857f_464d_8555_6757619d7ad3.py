"""The rejected raised hands have abbreviated thumbs and detached stripes; restore extended fingers and a clearer binding across the wrists. No written reviewer feedback.
Extended the raised hands, clarified the thumbs and brought the upper binding across the wrists.
Construction: Lucide hand original and atomic-debug; shared human reference. Mirrored hands.
Omissions: Two binding strokes replace three; fine finger bends reduced.
Keyshape: SQUARE. Balanced overall composition; centerline extremes (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f194c922-857f-464d-8555-6757619d7ad3'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__upturned-hands-with-binding-lines/20260929T121814Z-thuan-mac/reference/hostage fasten_f194c922-857f-464d-8555-6757619d7ad3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='upturned-hands-with-binding-lines'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('upturned', 'hands', 'with', 'binding', 'lines')

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

        for side in (0,1):
            x=lambda a:48-a if side else a
            sw=not side
            self.path(f'hand-{side}',(x(12),34),[('C',(x(6),20),(x(8),28),(x(6),24)),('L',(x(6),10)),('A',(x(14),10),4,4,sw),('L',(x(14),22)),('L',(x(20),28)),('L',(x(20),34))])
            self.add_line(f'thumb-{side}',(x(14),22),(x(16),18));self.relate('connect',f'thumb-{side}',f'hand-{side}')
        self.add_polyline('binding-top',(10,34),(12,34),(20,34),(28,34),(36,34),(38,34))
        self.add_line('binding-bottom',(10,42),(38,42))
        self.relate('connect','binding-top','hand-0');self.relate('connect','binding-top','hand-1')
