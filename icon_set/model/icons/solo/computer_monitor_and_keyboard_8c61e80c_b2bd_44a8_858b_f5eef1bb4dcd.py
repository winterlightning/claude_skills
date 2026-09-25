"""Computer Monitor and Keyboard. Empty standalone subject, per explicit user correction.
Lucide monitor: tangent rounded corners. Screen and keyboard share x=24 symmetry; screen-to-keyboard centerline gap is 8. Empty face and keyboard preserved.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '8c61e80c-b2bd-44a8-858b-f5eef1bb4dcd'
SOURCE_PATH = 'pictographic-primitives/container/monitor keyboard_8c61e80c-b2bd-44a8-858b-f5eef1bb4dcd.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'computer-monitor-and-keyboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('computer', 'monitor', 'and', 'keyboard')
    def build(self):
        x0,y0,x1,y1,r=6,6,42,26,4
        self.add_line("screen-top",(x0+r,y0),(x1-r,y0))
        self.add_arc("screen-ne",(x1-r,y0),(x1,y0+r),radius_x=r)
        self.add_line("screen-right",(x1,y0+r),(x1,y1-r))
        self.add_arc("screen-se",(x1,y1-r),(x1-r,y1),radius_x=r)
        self.add_line("screen-bottom",(x1-r,y1),(x0+r,y1))
        self.add_arc("screen-sw",(x0+r,y1),(x0,y1-r),radius_x=r)
        self.add_line("screen-left",(x0,y1-r),(x0,y0+r))
        self.add_arc("screen-nw",(x0,y0+r),(x0+r,y0),radius_x=r)
        self.add_contour("screen",*("screen-"+s for s in ("top","ne","right","se","bottom","sw","left","nw")),closed=True)
        self.add_polyline("keyboard",(10,34),(38,34),(42,42),(6,42),closed=True)
