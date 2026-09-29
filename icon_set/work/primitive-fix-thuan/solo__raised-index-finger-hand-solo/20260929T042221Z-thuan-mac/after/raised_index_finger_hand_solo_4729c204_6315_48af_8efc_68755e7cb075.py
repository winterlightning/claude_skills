"""One upright pointer with a long index, three rounded curled fingers, a diagonal thumb and a broad rounded palm; shared 6-unit curled-finger pitch.
Reference comparison: The rejected hand shortened the raised index and compressed or omitted curled digits. Feedback asks to recover the intended hand gesture.
Construction references: Lucide pointer and hand: continuous palm silhouette, round digit caps and attached finger creases.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4729c204-6315-48af-8efc-68755e7cb075'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__raised-index-finger-hand-solo/20260929T042221Z-thuan-mac/reference/finger_4729c204-6315-48af-8efc-68755e7cb075.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'raised-index-finger-hand-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.path('hand',(16,27),('L',(16,10)),('A',(24,10),4,4,True),('L',(24,21)),('A',(30,21),3,3,True),('L',(30,23)),('A',(36,23),3,3,True),('L',(36,25)),('A',(42,25),3,3,True),('L',(42,30)),('A',(30,42),12,12,True),('L',(24,42)),('A',(14,37),12,12,True),('L',(7,27)),('A',(13,23),4,4,True),('L',(16,27)),closed=True)
        for x,y in [(24,21),(30,23),(36,25)]:
            self.add_line(f'finger-{x}',(x,y),(x,y+5))
            self.relate('connect','hand',f'finger-{x}')

Drawing.exception = {'reason': 'User authorized visual exceptions. Retain all five anatomical digits and the long index: 6-unit finger pitch intentionally leaves 2-unit ink slots, still distinct at native size; slight organic envelope variance is accepted.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'ea9c7c7a06fcd4d12d73f970e3c1b18de3eb56088254b063313682beb271b8c7'}
