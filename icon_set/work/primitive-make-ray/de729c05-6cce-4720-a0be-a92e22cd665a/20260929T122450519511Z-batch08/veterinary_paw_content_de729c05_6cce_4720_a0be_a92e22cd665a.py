"""The rejected paw toes are dots and the medical cross nearly disappears; restore outlined toes and a larger cross. No written reviewer feedback.
Symbol plan: Lucide paw-print: repeated rounded toes above broad pad. Three circular toes match source count; mirrored pad.
Keyshape SQUARE, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='de729c05-6cce-4720-a0be-a92e22cd665a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__veterinary-paw-content/20260929T121814Z-thuan-mac/reference/paw print with a cross_de729c05-6cce-4720-a0be-a92e22cd665a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='veterinary-paw-content'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('veterinary', 'paw', 'content')

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

        for i,(x,y) in enumerate(((24,9),(9,16),(39,16))):self.circle(f'toe-{i}',x,y,3)
        self.path('pad',(12,42),[('A',(6,36),6,6,True),('C',(24,25),(6,30),(18,25)),('C',(42,36),(30,25),(42,30)),('A',(36,42),6,6,True),('L',(12,42))],True)
        self.add_polyline('cross-h',(20,34),(24,34),(28,34));self.add_polyline('cross-v',(24,30),(24,34),(24,38));self.relate('connect','cross-h','cross-v')
