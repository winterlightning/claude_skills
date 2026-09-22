"""Two differently sized clipped documents share a baseline above a single width marker. Common rounded page construction and cap spans are shared; intentional size difference follows the reference. Lucide files informed page contour.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: invalid, review, review. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: HRECT_XL; fine source details simplified only for native readability.
"""
from ._base import Container64
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '5bfa4543-d323-4064-a674-4f59d7473845'
SOURCE_PATH = 'pictographic-primitives/files/paper sizes two document measure 1_5bfa4543-d323-4064-a674-4f59d7473845.svg'
AUTHOR = "gpt-6"

def page(icon, prefix, left, top, right, bottom, cut=10, radius=3):
    pts=[(left+radius,top),(right-cut,top),(right,top+cut),(right,bottom-radius)]
    for j,(a,b) in enumerate(zip(pts,pts[1:]),1):
        icon.add_line(prefix+"-upper-"+str(j),a,b)
    icon.add_arc(prefix+"-br",pts[-1],(right-radius,bottom),radius_x=radius)
    icon.add_line(prefix+"-bottom",(right-radius,bottom),(left+radius,bottom))
    icon.add_arc(prefix+"-bl",(left+radius,bottom),(left,bottom-radius),radius_x=radius)
    icon.add_line(prefix+"-left",(left,bottom-radius),(left,top+radius))
    icon.add_arc(prefix+"-tl",(left,top+radius),pts[0],radius_x=radius)
    icon.add_contour(prefix,prefix+"-upper-1",prefix+"-upper-2",prefix+"-upper-3",prefix+"-br",prefix+"-bottom",prefix+"-bl",prefix+"-left",prefix+"-tl",closed=True)

class Icon(Container64):
    icon_id = 'document-paper-size-measurement'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'files'
    aliases = ('Document Paper Size Measurement',)
    keywords = ('document', 'paper', 'size', 'measurement')
    def build(self):
        page(self,"small",2,18,26,42,cut=8,radius=3)
        page(self,"large",36,6,62,42,cut=10,radius=3)
        self.add_line("dimension",(2,54),(62,54))
        for j,x in enumerate((2,62)):
            self.add_line("cap-"+str(j)+"-a",(x,50),(x,54))
            self.add_line("cap-"+str(j)+"-b",(x,54),(x,58))
            self.relate("connect","dimension","cap-"+str(j)+"-a","cap-"+str(j)+"-b")
