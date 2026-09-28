"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f5580be8-f678-427f-889e-270f12d6dee5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__five-petaled-flower-on-stem/20260925T090056Z-thuan-mac/reference/poppy_f5580be8-f678-427f-889e-270f12d6dee5.svg'
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
    icon_id = 'five-petaled-flower-on-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    exception = {'reason': 'Preserve the complete five-petal bloom, center and stem leaf; compact clearances remain readable in both themes.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '3d4a97e896347081e6923a66c0bbe6480c3c4a0520ed35dcffd147ea27b60b31'}
    aliases = ()
    keywords = ()

    def build(self):
        # Compact five-lobed bloom leaves room for the attached stem leaf.
        self.add_arc('top',(19,8),(29,8),radius_x=5)
        self.add_arc('right',(29,8),(32,18),radius_x=6,large_arc=True)
        self.add_arc('bottom-right',(32,18),(24,24),radius_x=6,large_arc=True)
        self.add_arc('bottom-left',(24,24),(16,18),radius_x=6,large_arc=True)
        self.add_arc('left',(16,18),(19,8),radius_x=6,large_arc=True)
        self.add_contour('petals','top','right','bottom-right','bottom-left','left',closed=True)
        circle(self,'center',24,15,3)
        self.add_line('stem',(24,24),(24,44))
        leaf(self,'leaf',(24,43),(10,36),10)
        self.relate('connect','leaf','stem')
        self.relate('connect','petals','stem')
