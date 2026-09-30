"""The rejected face has one eye and a tiny round mouth; restore two eyes and the broad worried open mouth beside the sweat drop. No written feedback.
Restored both eyes and a broad arched open mouth, with clear space beside the sweat drop.
No useful exact local Lucide face match. The supplied reference informs the worried mouth and sweat. Eyes sit left of the enlarged drop; the mouth and circular face are centered at x=24.
Omissions: Fine eyebrows omitted. Face outline opens behind the enlarged sweat drop to retain clearance.
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
        self.add_dot('eye-left',(17,17));self.add_dot('eye-right',(25,17))
        self.path('mouth',(18,31),[('A',(30,31),6,6,True),('L',(18,31))],True)
