"""Four clear knuckles, folded thumb and wrist beneath four detached protest rays; lowered knuckles reserve breathing room for the rays.
Reference comparison: The rejected fist lost its curled-finger anatomy and wrist; the thumb became a slash or a flat capsule. Feedback asks for the raised closed-fist meaning.
Construction references: Lucide hand-fist: knuckle construction, opposing thumb and rounded palm; source controls upright pose.
Omissions: Minor palm crease simplified to one curved run.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '56d270cc-86ac-49c0-a72a-078631b992ea'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__raised-clenched-fist/20260929T042221Z-thuan-mac/reference/protest knuckle up_56d270cc-86ac-49c0-a72a-078631b992ea.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'raised-clenched-fist'
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
        self.path('fist',(10,27),('L',(10,19)),('A',(16,19),3,3,True),('L',(16,16)),('A',(22,16),3,3,True),('L',(22,14)),('A',(28,14),3,3,True),('L',(28,16)),('A',(34,16),3,3,True),('L',(34,20)),('L',(38,25)),('A',(38,33),8,8,True),('L',(33,40)),('L',(33,44)),('L',(15,44)),('L',(15,39)),('A',(10,27),18,18,True),closed=True)
        self.path('thumb',(34,20),('L',(26,20)),('A',(26,28),4,4,False),('L',(30,28)),('A',(24,34),9,9,False))
        self.relate('connect','fist','thumb')
        for x,y,end in [(16,19,27),(22,16,22),(28,16,19)]:
            self.add_line(f'knuckle-{x}',(x,y),(x,end));self.relate('connect','fist',f'knuckle-{x}')
        
        
        self.add_line('ray-left',(4,10),(6,12))
        self.add_line('ray-upper-left',(15,3),(16,6))
        self.add_line('ray-upper-right',(32,3),(31,6))
        self.add_line('ray-right',(40,12),(43,9))

Drawing.exception = {'reason': 'Clenched fingers have 6-unit pitch and thumb overlaps; anatomical slots below MIC are intentionally retained and readable. User authorized complete-gesture exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '0623c8a39ae89cd5dc08225ccc933d5f2891093e5e101b4ccc3fbd6850c8143b'}
