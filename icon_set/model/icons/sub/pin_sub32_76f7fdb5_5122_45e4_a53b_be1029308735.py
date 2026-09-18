"""Independent 32px profile of pin.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '76f7fdb5-5122-45e4-a53b-be1029308735'
SOURCE_PATH = 'pictographic-primitives/interface-essential/pin_76f7fdb5-5122-45e4-a53b-be1029308735.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('76f7fdb5-5122-45e4-a53b-be1029308735', 'pictographic-primitives/interface-essential/pin_76f7fdb5-5122-45e4-a53b-be1029308735.svg'), ('9b4b8603-58f9-4f81-8664-658ab7045658', 'pictographic-primitives/interface-essential/pin_9b4b8603-58f9-4f81-8664-658ab7045658.svg'), ('79f28f0f-6da1-42b3-a142-474d81fe6b26', 'pictographic-primitives/state/pin wave_79f28f0f-6da1-42b3-a142-474d81fe6b26.svg'))
PROFILE_SOURCE_KEYS = ('solo/pin', 'solo/pin-9b4b8603', 'solo/pin-wave')
SOLO_SOURCE_ICON_IDS = ('pin', 'pin-9b4b8603', 'pin-wave')
REFERENCE_EXPORT_SHA256 = '267d1985c489b24572604f32fc408010b1c0590304c66b4756ffb33ebc8ca294'

class Drawing(Sub32):
    icon_id = 'pin-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (5, 13), (27, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_bezier('p1-r1-2', (27, 13), ((27, 20), (20, 26), (16, 30)))
        self.add_bezier('p1-r1-3', (16, 30), ((12, 26), (5, 20), (5, 13)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_arc('p2-r1-1', (13, 13), (20, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (20, 13), (13, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
