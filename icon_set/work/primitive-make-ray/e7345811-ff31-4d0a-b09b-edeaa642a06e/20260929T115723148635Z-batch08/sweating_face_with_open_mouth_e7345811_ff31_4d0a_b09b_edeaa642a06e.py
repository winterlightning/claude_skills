"""The rejected face has one eye and a tiny round mouth; restore two eyes and the broad worried open mouth beside the sweat drop. No written feedback.
Symbol plan: No useful exact Lucide face match; circular face arcs and mirrored mouth. Fine brows omitted; outline opens behind sweat.
Keyshape SQUARE, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e7345811-ff31-4d0a-b09b-edeaa642a06e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__sweating-face-with-open-mouth/20260929T115301Z-thuan-mac/reference/face tongue sweat_e7345811-ff31-4d0a-b09b-edeaa642a06e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='sweating-face-with-open-mouth'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('sweating', 'face', 'with', 'open', 'mouth')

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

        self.path('face',(24,6),[('A',(6,24),18,18,False),('A',(24,42),18,18,False),('C',(40,34),(32,42),(38,39))])
        self.path('sweat',(38,6),[('L',(42,18)),('A',(34,18),4,4,True),('L',(38,6))],True)
        self.add_dot('eye-left',(17,17));self.add_dot('eye-right',(27,17))
        self.path('mouth',(18,32),[('A',(30,32),6,7,True),('L',(18,32))],True)
