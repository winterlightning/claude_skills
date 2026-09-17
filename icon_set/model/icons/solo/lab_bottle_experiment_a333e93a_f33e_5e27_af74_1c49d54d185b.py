"""A symmetric laboratory flask with a straight rim and a liquid level. Repaired in place from bad-stroke feedback."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a333e93a-f33e-5e27-af74-1c49d54d185b'
SOURCE_PATH = 'pictographic-primitives/science/lab bottle experiment_a333e93a-f33e-5e27-af74-1c49d54d185b.svg'
AUTHOR = 'gpt-6'

class LabBottleExperiment(Solo48):
    icon_id = 'lab-bottle-experiment'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'bottle', 'experiment', 'science')

    def build(self) -> None:
        # Symmetric flask: shared neck, sloping shoulders, tangent base corners.
        # Lucide flask-conical supplies the continuous outline and liquid line.
        # VRECT_L centerline extremes: (8, 4)-(40, 44).
        axis = 24
        left_neck, right_neck = axis - 6, axis + 6
        self.add_line('rim-left', (14, 4), (left_neck, 4))
        self.add_line('rim-middle', (left_neck, 4), (right_neck, 4))
        self.add_line('rim-right', (right_neck, 4), (34, 4))
        self.add_contour('rim', 'rim-left', 'rim-middle', 'rim-right')
        self.add_line('neck-right', (right_neck, 4), (right_neck, 16))
        self.add_line('shoulder-right-upper', (right_neck, 16), (36, 28))
        self.add_line('shoulder-right-lower', (36, 28), (40, 36))
        self.add_line('base-right', (40, 36), (40, 40))
        self.add_arc('corner-right', (40, 40), (36, 44), radius_x=4)
        self.add_line('base', (36, 44), (12, 44))
        self.add_arc('corner-left', (12, 44), (8, 40), radius_x=4)
        self.add_line('base-left', (8, 40), (8, 36))
        self.add_line('shoulder-left-lower', (8, 36), (12, 28))
        self.add_line('shoulder-left-upper', (12, 28), (left_neck, 16))
        self.add_line('neck-left', (left_neck, 16), (left_neck, 4))
        self.add_contour('bottle', 'neck-right', 'shoulder-right-upper', 'shoulder-right-lower', 'base-right',
                         'corner-right', 'base', 'corner-left', 'base-left',
                         'shoulder-left-lower', 'shoulder-left-upper', 'neck-left')
        self.add_line('liquid', (12, 28), (36, 28))
        self.relate('connect', 'rim', 'bottle')
        self.relate('connect', 'bottle', 'liquid')
