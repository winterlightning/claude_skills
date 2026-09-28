"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '050049d7-8f68-4624-933b-04727efa4974'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flat-mouthed-face-with-half-circle-eyes-batch038/20260925T090056Z-thuan-mac/reference/face rolling eyes_050049d7-8f68-4624-933b-04727efa4974.svg'
AUTHOR = "gpt-6"

def circle(self,name,x,y,r):
    self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
    self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
    self.add_contour(name,name+'-a',name+'-b',closed=True)

def leaf(self,name,a,b,r):
    self.add_arc(name+'-a',a,b,radius_x=r)
    self.add_arc(name+'-b',b,a,radius_x=r)
    self.add_contour(name,name+'-a',name+'-b',closed=True)

class Revision(Solo48):
    icon_id = 'flat-mouthed-face-with-half-circle-eyes-batch038'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    exception = {'reason': 'Preserve the reference half-lidded expression with clear eye openings; face-to-eye spacing is visually acceptable at native size.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': 'a59c996bfe3d2ed3eec869b66811090f88011936430d14b7661ec7aecf3323af'}
    aliases = ()
    keywords = ()

    def build(self):
        circle(self,'face',24,24,20)
        for i,x in enumerate((15,33)):
            self.add_line(f'lid-{i}',(x-5,18),(x+5,18))
            self.add_arc(f'eye-{i}',(x+5,18),(x-5,18),radius_x=5,radius_y=6)
            self.add_contour(f'eye-loop-{i}',f'lid-{i}',f'eye-{i}',closed=True)
        self.add_line('mouth',(18,33),(30,33))
