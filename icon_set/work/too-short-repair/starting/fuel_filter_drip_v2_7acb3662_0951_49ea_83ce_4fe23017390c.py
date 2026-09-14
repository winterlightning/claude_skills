# Variant of fuel-filter-drip; parent file remains unchanged.
"""Fuel Filter with Drip, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7acb3662-0951-49ea-83ce-4fe23017390c'
SOURCE_PATH = 'pictographic-primitives/transportation/fuel filter warning_7acb3662-0951-49ea-83ce-4fe23017390c.svg'
AUTHOR = 'gpt-6'

class FuelFilterDripVariant2(Solo48):
    icon_id = 'fuel-filter-drip-v2'
    variant_of = 'fuel-filter-drip'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('fuel filter', 'filter', 'fuel', 'drip', 'warning', 'diesel', 'dashboard', 'car')

    def build(self) -> None:
        self.add_polyline('flange', (8, 6), (12, 6), (36, 6), (40, 6))
        self.add_polyline('bowl', (12, 6), (12, 14), (12, 18), (24, 24), (36, 18), (36, 14), (36, 6))
        self.relate('connect', 'flange', 'bowl')
        self.add_line('liquid', (12, 14), (36, 14))
        self.relate('connect', 'liquid', 'bowl')
        self.add_line('drop-right', (24, 33), (28, 40))
        self.add_arc('drop-base', (28, 40), (20, 40), radius_x=4)
        self.add_line('drop-left', (20, 40), (24, 33))
        self.add_contour('drop', 'drop-right', 'drop-base', 'drop-left', closed=True)
