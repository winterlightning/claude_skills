"""Fresh manual-fix reconstruction: complete original reference and geometric UI forms."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8d04928d-83dd-4d17-a7ec-1662a74d856b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__folded-awareness-ribbon/20260925T090056Z-thuan-mac/reference/ribbon_8d04928d-83dd-4d17-a7ec-1662a74d856b.svg'
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
    icon_id = 'folded-awareness-ribbon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    exception = {'reason': 'Preserve the recognizable ribbon width, folded loop and crossing strips; compact strip interiors remain open at native size.', 'approved_by': 'user (delegated visual exception judgment)', 'approved_on': '2026-09-25', 'svg_sha256': '60edf493a534a613da33f313994e4094f669319849b4f238d126fcd49c774f71'}
    aliases = ()
    keywords = ()

    def build(self):
        # Two broad crossing strips, open loop and visible folded top, rather than a single X stroke.
        self.add_arc('loop',(14,14),(34,14),radius_x=10)
        self.add_arc('right-outer',(34,14),(28,29),radius_x=30)
        self.add_line('left-tail-1',(28,29),(14,44))
        self.add_line('left-tail-2',(14,44),(8,38))
        self.add_line('left-tail-3',(8,38),(25,20))
        self.add_arc('inner-top',(25,20),(14,14),radius_x=20,sweep=False)
        self.add_contour('front','loop','right-outer','left-tail-1','left-tail-2','left-tail-3','inner-top',closed=True)
        self.add_arc('fold',(14,14),(34,14),radius_x=15,radius_y=7)
        self.add_polyline('back-tail',(28,29),(40,38),(34,44),(23,33))
        self.add_arc('back-left',(14,14),(19,26),radius_x=26,sweep=False)
