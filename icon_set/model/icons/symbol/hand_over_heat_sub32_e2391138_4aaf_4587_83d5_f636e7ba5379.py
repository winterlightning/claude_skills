"""Independent 32px profile of hand-over-heat.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e2391138-4aaf-4587-83d5-f636e7ba5379'
SOURCE_PATH = 'pictographic-primitives/symbol/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e2391138-4aaf-4587-83d5-f636e7ba5379', 'pictographic-primitives/symbol/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-over-heat',)
SOLO_SOURCE_ICON_IDS = ('hand-over-heat',)
REFERENCE_EXPORT_SHA256 = '7144bb3357aa279a4a7628efb46b92249dac4d41746e3302ba244ba39652c6e3'

class Drawing(Sub32):
    icon_id = 'hand-over-heat-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Hand side-on, palm down over heat: wrist cuff, back of the hand arching to rounded fingertips,
        # the thumb hanging below the palm, three heat waves rising underneath.
        self.add_bezier('back', (2, 4), ((10, 2), (20, 2), (26, 4)))
        self.add_arc('tip', (26, 4), (26, 12), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('fingers', (26, 12), (14, 12))
        self.add_line('thumb-1', (14, 12), (10, 16))
        self.add_line('thumb-2', (10, 16), (6, 12))
        self.add_line('palm', (6, 12), (2, 12))
        self.add_line('wrist', (2, 12), (2, 4))
        self.add_contour('hand', 'back', 'tip', 'fingers', 'thumb-1', 'thumb-2', 'palm', 'wrist', closed=True)
        self.add_line('cuff-top', (2, 4), (2, 2))
        self.add_line('cuff-bottom', (2, 12), (2, 16))
        self.relate('connect', 'hand', 'cuff-top')
        self.relate('connect', 'hand', 'cuff-bottom')
        self.add_bezier('wave-1', (6, 24), ((3, 26), (9, 28), (6, 30)))
        self.add_bezier('wave-2', (16, 24), ((13, 26), (19, 28), (16, 30)))
        self.add_bezier('wave-3', (26, 24), ((23, 26), (29, 28), (26, 30)))
