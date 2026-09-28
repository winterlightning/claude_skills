"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6a1ecbd5-e710-49ac-8aeb-04d4c78b521a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flower/20260925T090056Z-thuan-mac/reference/flower_6a1ecbd5-e710-49ac-8aeb-04d4c78b521a.svg'
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
    icon_id = 'flower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'nature'
    exception = {'reason': 'Preserve natural fivefold flower proportions rather than a forced square envelope.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '2689b2fc85cfc0e593aeb954551a2b6af493aed6258254320deba907c84ef6ce'}
    aliases = ()
    keywords = ()

    def build(self):
        # Five distinct round lobes with mirrored left/right pairs.
        self.add_arc('top',(16,16),(32,16),radius_x=8)
        self.add_arc('right',(32,16),(36,28),radius_x=7,large_arc=True)
        self.add_arc('bottom-right',(36,28),(24,36),radius_x=8,large_arc=True)
        self.add_arc('bottom-left',(24,36),(12,28),radius_x=8,large_arc=True)
        self.add_arc('left',(12,28),(16,16),radius_x=7,large_arc=True)
        self.add_contour('petals','top','right','bottom-right','bottom-left','left',closed=True)
