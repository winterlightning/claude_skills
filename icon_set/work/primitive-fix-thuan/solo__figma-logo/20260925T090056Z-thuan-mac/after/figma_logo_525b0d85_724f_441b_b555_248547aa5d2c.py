"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '525b0d85-724f-441b-b555-248547aa5d2c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__figma-logo/20260925T090056Z-thuan-mac/reference/figma logo_525b0d85-724f-441b-b555-248547aa5d2c.svg'
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
    icon_id = 'figma-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'logos'
    exception = {'reason': 'Preserve recognizable equal Figma cells and authentic touching circular logo geometry, including small tangency interstices.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '2c92ac27519580744a5557241c5936f91f8269266332b7798e027dc189b0a86e'}
    aliases = ()
    keywords = ()

    def build(self):
        # Shared seven-unit radii keep all five logo cells equal and aligned.
        self.add_line('top',(17,3),(31,3))
        self.add_arc('top-right',(31,3),(31,17),radius_x=7)
        self.add_line('bar',(31,17),(17,17))
        self.add_arc('top-left',(17,17),(17,3),radius_x=7)
        self.add_contour('cap','top','top-right','bar','top-left',closed=True)
        self.add_line('spine',(24,3),(24,38))
        self.add_arc('middle-left',(17,31),(17,17),radius_x=7)
        self.add_line('middle-bottom',(17,31),(24,31))
        self.add_arc('bottom',(24,38),(10,38),radius_x=7)
        self.add_arc('bottom-left',(10,38),(17,31),radius_x=7)
        self.add_contour('lower-left','bottom','bottom-left','middle-bottom')
        circle(self,'dot',31,24,7)
        self.relate('connect','cap','spine')
        self.relate('connect','cap','middle-left')
        self.relate('connect','middle-left','lower-left')
        self.relate('connect','lower-left','spine')
        self.relate('connect','cap','dot')
        self.relate('connect','spine','dot')
