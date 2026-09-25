"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3ea1561a-0ad1-4359-8da5-b2d62f6fc199'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__foggy-cloud/20260925T090056Z-thuan-mac/reference/weather cloud wind 1_3ea1561a-0ad1-4359-8da5-b2d62f6fc199.svg'
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
    icon_id = 'foggy-cloud'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    exception = {'reason': 'Preserve natural cloud envelope; exact eight-unit cloud/fog centerline gap is visually open despite conservative curved check.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '167fe50416cc6269b3d3a456e0150fba71e91d39d086635ffd20c10ecf25e00f'}
    aliases = ()
    keywords = ()

    def build(self):
        self.add_line('cloud-base',(12,28),(29,28))
        self.add_arc('cloud-left',(12,28),(12,14),radius_x=7)
        self.add_arc('cloud-top',(12,14),(34,14),radius_x=11,radius_y=10)
        self.add_arc('cloud-right',(34,14),(38,28),radius_x=8)
        self.add_contour('cloud','cloud-base')
        self.add_contour('cloud-silhouette','cloud-left','cloud-top','cloud-right')
        self.relate('connect','cloud','cloud-silhouette')
        self.add_line('fog-1',(6,36),(34,36))
        self.add_line('fog-2',(12,44),(28,44))
