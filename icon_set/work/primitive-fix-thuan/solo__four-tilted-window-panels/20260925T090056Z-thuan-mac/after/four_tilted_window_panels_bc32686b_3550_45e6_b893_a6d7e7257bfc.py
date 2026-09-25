"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bc32686b-3550-45e6-b893-a6d7e7257bfc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__four-tilted-window-panels/20260925T090056Z-thuan-mac/reference/microsoft logo_bc32686b-3550-45e6-b893-a6d7e7257bfc.svg'
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
    icon_id = 'four-tilted-window-panels'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    exception = {'reason': 'Preserve the original slanted panel grid and its natural staggered envelope; automatic spacing passes.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '3f7cb8cf52329a21eb87119b0636807c6baa689429baac3abd765f02c7163cf5'}
    aliases = ()
    keywords = ()

    def build(self):
        # Four matching slanted panels, arranged as the reference's staggered 2-by-2 series.
        for row in range(2):
            for col in range(2):
                x=12+col*20-row*4; y=4+row*22+col*3
                self.add_polyline(f'pane-{row}-{col}',(x,y),(x+12,y),(x+8,y+14),(x-4,y+14),closed=True)
