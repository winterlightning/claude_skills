"""Replace the short central water dash with two aligned falling-water marks, giving the dam a clearer discharge pattern.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6411cee5-9e14-533a-9adf-d5bcd2213734'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/water dam_6411cee5-9e14-533a-9adf-d5bcd2213734.svg'
AUTHOR = 'gpt-6'

class HydroelectricDam(Solo48):
    icon_id = 'hydroelectric-dam-centerline-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('dam', 'hydroelectric', 'water', 'reservoir', 'spillway', 'power', 'energy', 'infrastructure')

    def build(self):
        self.add_polyline('left-pier', (4, 28), (4, 8), (12, 8), (12, 16), (12, 28), closed=True)
        self.add_polyline('right-pier', (36, 28), (36, 16), (36, 8), (44, 8), (44, 28), closed=True)
        self.add_line('crest', (12, 16), (36, 16))
        self.relate('connect', 'crest', 'left-pier')
        self.relate('connect', 'crest', 'right-pier')
        self.add_line('flow-left', (20, 24), (20, 28))
        self.add_line('flow-right', (28, 24), (28, 28))
        self.add_arc('wave-left', (4, 37), (24, 37), radius_x=10, radius_y=3, sweep=False)
        self.add_arc('wave-right', (24, 37), (44, 37), radius_x=10, radius_y=3, sweep=False)
        self.add_contour('water', 'wave-left', 'wave-right', closed=False)
    variant_of = 'hydroelectric-dam'
    variant_label = 'Batch 01 centerline repair'
