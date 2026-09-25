"""Broad elbow drainpipe with three falling streams. Square x6..42 y6..42. Paired concentric quarter arcs own elbow; streams share y38..42 and step8. Source sets elbow and falling water. Lucide corner-down-right teaches tangent elbow. Omit double rim to preserve clearance."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '4c5aeecb-6fcf-4263-9573-d26b992703fa'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/drainage_4c5aeecb-6fcf-4263-9573-d26b992703fa.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'bent-drainpipe-with-falling-water-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ['Bent Drainpipe with Falling Water Lines']
    keywords = ['drainpipe', 'pipe', 'water', 'outlet', 'flow', 'plumbing', 'elbow']
    def build(self):
        self.add_line('upper',(6,6),(22,6))
        self.add_arc('outer-elbow',(22,6),(42,26),radius_x=20)
        self.add_line('outer-outlet',(42,26),(42,30))
        self.add_line('rim',(42,30),(26,30))
        self.add_line('inner-outlet',(26,30),(26,26))
        self.add_arc('inner-elbow',(26,26),(22,22),radius_x=4,sweep=False)
        self.add_line('lower',(22,22),(6,22))
        self.add_line('inlet',(6,22),(6,6))
        self.add_contour('pipe','upper','outer-elbow','outer-outlet','rim','inner-outlet','inner-elbow','lower','inlet',closed=True)
        for i in range(3):
            x=26+i*8
            self.add_line(f'water-{i}',(x,39),(x,42))
