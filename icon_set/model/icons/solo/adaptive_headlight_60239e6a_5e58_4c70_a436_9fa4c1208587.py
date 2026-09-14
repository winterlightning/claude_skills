"""A D-shaped adaptive headlamp with three sloping beams and an attached upper tick. HRECT_L ink (6,6)-(42,42). No useful exact Lucide match; a circle owns the lamp and attachment point."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60239e6a-5e58-4c70-a436-9fa4c1208587'
SOURCE_PATH = 'pictographic-primitives/transportation/adaptive light 1_60239e6a-5e58-4c70-a436-9fa4c1208587.svg'
AUTHOR = 'gpt-6'

class AdaptiveHeadlight(Solo48):
    icon_id = 'adaptive-headlight'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('headlight', 'adaptive', 'lamp', 'beam', 'car', 'dashboard', 'lighting', 'indicator')

    def build(self) -> None:
        # The tick meets the circular face at the exact 5-12-13 circle point.
        self.add_line('lamp-flat',(29,14),(29,40))
        self.add_arc('lamp-lower',(29,40),(41,22),radius_x=13,sweep=False)
        self.add_arc('lamp-upper',(41,22),(29,14),radius_x=13,sweep=False)
        self.add_contour('lamp','lamp-flat','lamp-lower','lamp-upper',closed=True)
        for i in range(3):
            y=12+i*12
            self.add_line(f'beam-{i}',(4,y+4),(17,y-2))
        self.add_line('adaptive-tick',(41,22),(42,8))
        self.relate('connect','adaptive-tick','lamp')
