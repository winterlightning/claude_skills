"""The rejected victory hand has no folded fingers or thumb, so it resembles a fork; restore a palm crease beneath the two raised fingers. No written reviewer feedback.
Symbol plan: Lucide hand-metal and hand: rounded fingertips and folded-finger crease. Two raised fingers and open wrist preserved.
Keyshape VRECT_M, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e092cced-a3af-49d1-b7d5-7eb03a1a3b03'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__victory-hand/20260929T121814Z-thuan-mac/reference/toys finger_e092cced-a3af-49d1-b7d5-7eb03a1a3b03.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='victory-hand'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('victory', 'hand')

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

        self.path('hand',(16,44),[('L',(16,38)),('A',(10,32),6,6,True),('L',(10,8)),('A',(18,8),4,4,True),('L',(22,22)),('L',(26,22)),('L',(30,8)),('A',(38,8),4,4,True),('L',(34,28)),('L',(34,36)),('A',(30,40),4,4,True),('L',(30,44))])
        self.add_polyline('fold',(34,28),(22,28),(22,33));self.relate('connect','fold','hand')
