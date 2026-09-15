"""Replace the sharp filter-bowl point with a rounded sump and keep the drop centered below its lowest point.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7acb3662-0951-49ea-83ce-4fe23017390c'
SOURCE_PATH = 'pictographic-primitives/transportation/fuel filter warning_7acb3662-0951-49ea-83ce-4fe23017390c.svg'
AUTHOR = 'gpt-6'

class FuelFilterDrip(Solo48):
    icon_id = 'fuel-filter-drip-centerline-v2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('fuel filter', 'filter', 'fuel', 'drip', 'warning', 'diesel', 'dashboard', 'car')

    def build(self) -> None:
        self.add_polyline('flange', (8, 4), (12, 4), (36, 4), (40, 4))
        self.add_polyline('bowl', (12, 4), (12, 14), (12, 18), (18, 22), (30, 22), (36, 18), (36, 14), (36, 4))
        self.relate('connect', 'flange', 'bowl')
        self.add_line('liquid', (12, 14), (36, 14))
        self.relate('connect', 'liquid', 'bowl')
        self.add_line('drop-right', (24, 33), (28, 40))
        self.add_arc('drop-base', (28, 40), (20, 40), radius_x=4)
        self.add_line('drop-left', (20, 40), (24, 33))
        self.add_contour('drop', 'drop-right', 'drop-base', 'drop-left', closed=True)
    variant_of = 'fuel-filter-drip'
    variant_label = 'Batch 01 centerline repair'
