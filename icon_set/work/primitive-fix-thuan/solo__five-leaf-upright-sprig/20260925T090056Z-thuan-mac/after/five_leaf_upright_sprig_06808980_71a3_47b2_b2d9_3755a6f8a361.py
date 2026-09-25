"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '06808980-71a3-47b2-b2d9-3755a6f8a361'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__five-leaf-upright-sprig/20260925T090056Z-thuan-mac/reference/alfalfa_06808980-71a3-47b2-b2d9-3755a6f8a361.svg'
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
    icon_id = 'five-leaf-upright-sprig'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    exception = {'reason': 'Preserve five attached leaves and their tapered junctions; all leaf interiors remain open at 48 pixels.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': 'aad6494e0b841ff0e31f3cc438edc86e21962b32730c3416ca7cac5e7f4225de'}
    aliases = ()
    keywords = ()

    def build(self):
        self.add_line('stem',(24,18),(24,44))
        leaf(self,'top',(24,4),(24,18),9)
        self.relate('connect','top','stem')
        for i,y in enumerate((28,40)):
            for side in (-1,1):
                name=f'leaf-{i}-{side}'
                leaf(self,name,(24,y),(24+side*16,y-10),15)
                self.relate('connect',name,'stem')
