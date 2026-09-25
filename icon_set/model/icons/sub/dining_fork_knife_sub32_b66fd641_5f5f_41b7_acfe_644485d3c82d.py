"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b66fd641-5f5f-41b7-acfe-644485d3c82d'
SOURCE_PATH = 'pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('three-tined fork', 'rounded fork bowl with central tine continuing into handle', 'upright curved knife blade with heel', 'long knife handle')

class Drawing(Sub32):
    icon_id = 'dining-fork-knife-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    keywords = ('dining', 'fork', 'and', 'knife')


    def build(self):
        # Fork uses two tangent quarters; the central tine continues to its handle.
        self.add_line('fork-left',(4,2),(4,10))
        self.add_arc('fork-bottom-left',(4,10),(10,16),radius_x=6,sweep=False)
        self.add_arc('fork-bottom-right',(10,16),(16,10),radius_x=6,sweep=False)
        self.add_line('fork-right',(16,10),(16,2))
        self.add_contour('fork-cup','fork-left','fork-bottom-left','fork-bottom-right','fork-right')
        self.add_line('fork-center',(10,2),(10,16))
        self.add_line('fork-handle',(10,16),(10,30))
        self.relate('connect','fork-bottom-left','fork-center','fork-handle')
        self.relate('connect','fork-bottom-right','fork-center','fork-handle')
        self.add_line('knife-back',(22,2),(22,18))
        self.add_bezier('knife-edge',(22,2),((26,6),(28,11),(28,18)))
        self.add_line('knife-heel',(28,18),(22,18))
        self.add_contour('blade','knife-edge','knife-heel')
        self.add_line('knife-handle',(22,18),(22,30))
        self.relate('connect','knife-back','knife-edge')
        self.relate('connect','knife-back','knife-heel','knife-handle')

