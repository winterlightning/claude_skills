"""Document Size Comparison. Reference retains the complete subject following saved user classification.
Plan: SQUARE envelope; shared page/currency dimensions and true beam attachment nodes.
Lucide files informs page contour continuity; dollar-sign informs paired currency bowls.
Source supplies count, relative placement and intentional asymmetry. Decorative thickness omitted.
Hosting probes: plus-sign-state-131 and check-mark are invalid; heart-state-63
is review. The document pair is not a general-purpose symbol host.
"""
from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = '4a5055f4-a8f9-4b9e-b27f-72c9528663db'
SOURCE_PATH = 'pictographic-primitives/files/paper sizes two document measure_4a5055f4-a8f9-4b9e-b27f-72c9528663db.svg'
AUTHOR = "gpt-6"

class Drawing(Container64):
    icon_id = 'document-size-comparison'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ()
    keywords = ('document', 'size', 'comparison')

    def build(self):


        self.add_polyline('small-page',(2,38),(14,38),(22,46),(22,62),(2,62),closed=True)
        self.add_polyline('large-page',(30,22),(50,22),(62,34),(62,62),(30,62),closed=True)
        for name,l,r,y in [('small',2,22,28),('large',30,62,6)]:
            self.add_line(name+'-measure',(l,y),(r,y))
            for side,x in [('left',l),('right',r)]:
                cap=name+'-'+side
                self.add_polyline(cap,(x,y-4),(x,y),(x,y+4))
                self.relate('connect',name+'-measure',cap)
