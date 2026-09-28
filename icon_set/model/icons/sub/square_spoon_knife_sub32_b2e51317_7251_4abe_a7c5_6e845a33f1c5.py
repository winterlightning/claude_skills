"""Complete square, circular spoon and curved knife reference reconstruction."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b2e51317-7251-4abe-a7c5-6e845a33f1c5'
SOURCE_PATH = 'pictographic-primitives/other/square folk_b2e51317-7251-4abe-a7c5-6e845a33f1c5.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square frame', 'circular spoon bowl', 'attached vertical spoon handle', 'upright knife with curved blade and horizontal heel', 'vertical knife handle')

class SquareSpoonKnife(Sub32):
    icon_id = 'square-spoon-knife-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    aliases = ('dining', 'cutlery')
    keywords = ('spoon', 'knife', 'square', 'food', 'restaurant')

    def build(self):
        # One rounded enclosure and two utensils. The spoon owns its circular
        # bowl and handle attachment; the knife owns blade, heel and handle.
        points = [(4,2),(28,2),(30,4),(30,28),(28,30),(4,30),(2,28),(2,4)]
        for i,a in enumerate(points):
            b=points[(i+1)%8]
            if i%2: self.add_arc(f'frame-{i}',a,b,radius_x=2)
            else: self.add_line(f'frame-{i}',a,b)
        self.add_contour('frame',*[f'frame-{i}' for i in range(8)],closed=True)
        cx,cy,radius = 11,12,4
        # Start/end the bowl at its true handle attachment.
        self.add_arc('bowl-left',(cx,cy+radius),(cx,cy-radius),radius_x=radius)
        self.add_arc('bowl-right',(cx,cy-radius),(cx,cy+radius),radius_x=radius)
        self.add_contour('bowl','bowl-left','bowl-right',closed=True)
        self.add_line('spoon-handle',(cx,cy+radius),(cx,24))
        self.relate('connect','bowl-left','spoon-handle')
        self.relate('connect','bowl-right','spoon-handle')
        self.add_line('knife-back',(20,9),(20,18))
        self.add_bezier('knife-edge',(20,9),((23,12),(25,15),(25,18)))
        self.add_line('knife-heel',(25,18),(20,18))
        self.add_contour('blade','knife-edge','knife-heel',closed=False)
        self.add_line('knife-handle',(20,18),(20,24))
        self.relate('connect','knife-back','knife-edge')
        self.relate('connect','knife-back','knife-heel')
        self.relate('connect','knife-back','knife-handle')
        self.relate('connect','knife-heel','knife-handle')
