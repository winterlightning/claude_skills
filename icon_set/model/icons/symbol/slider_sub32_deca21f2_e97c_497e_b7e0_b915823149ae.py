"""Independent 32px profile of slider.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'deca21f2-e97c-497e-b7e0-b915823149ae'
SOURCE_PATH = 'pictographic-primitives/symbol/slider_deca21f2-e97c-497e-b7e0-b915823149ae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('deca21f2-e97c-497e-b7e0-b915823149ae', 'pictographic-primitives/symbol/slider_deca21f2-e97c-497e-b7e0-b915823149ae.svg'),)
PROFILE_SOURCE_KEYS = ('solo/slider',)
SOLO_SOURCE_ICON_IDS = ('slider',)
REFERENCE_EXPORT_SHA256 = '76ba943f150a3731d3b32e22a1cbaec306e2d311fc8d58ed54e08cc610633ffd'

class Drawing(Sub32):
    icon_id = 'slider-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Sliders: two tracks, each with a round knob.
        for k, (y, x) in enumerate(((8, 10), (24, 22))):
            self.add_arc(f'knob-{k}-1', (x - 4, y), (x + 4, y), radius_x=4, radius_y=4, large_arc=False, sweep=True)
            self.add_arc(f'knob-{k}-2', (x + 4, y), (x - 4, y), radius_x=4, radius_y=4, large_arc=False, sweep=True)
            self.add_contour(f'knob-{k}', f'knob-{k}-1', f'knob-{k}-2', closed=True)
            self.add_line(f'track-{k}-a', (2, y), (x - 4, y))
            self.add_line(f'track-{k}-b', (x + 4, y), (30, y))
            self.relate('connect', f'knob-{k}', f'track-{k}-a')
            self.relate('connect', f'knob-{k}', f'track-{k}-b')
