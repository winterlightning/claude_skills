"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd931a080-b0aa-5280-b50e-074e997cbca4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__fishing-line/20260925T090056Z-thuan-mac/reference/fishing line_d931a080-b0aa-5280-b50e-074e997cbca4.svg'
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
    icon_id = 'fishing-line'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'outdoors'
    exception = {'reason': 'Preserve the narrow upright hook silhouette and its purposeful acute barb.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '7f97a883399e9f205e009c50c8c13b27e3a4a0bc51004ed45f34e4fc25e63e6c'}
    aliases = ()
    keywords = ()

    def build(self):
        circle(self,'float',30,15,4)
        self.add_line('line-top',(30,4),(30,11))
        self.add_line('line-bottom',(30,19),(30,32))
        self.add_arc('hook',(30,32),(10,32),radius_x=10)
        self.add_line('barb-1',(10,32),(10,27))
        self.add_line('barb-2',(10,27),(15,33))
        self.add_contour('hook-line','line-bottom','hook','barb-1','barb-2')
        self.relate('connect','float','line-top')
        self.relate('connect','float','hook-line')
