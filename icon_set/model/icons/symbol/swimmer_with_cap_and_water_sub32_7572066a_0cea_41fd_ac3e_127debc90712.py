"""Independent 32px profile of swimmer-with-cap-and-water.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7572066a-0cea-41fd-ac3e-127debc90712'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/swim compete_7572066a-0cea-41fd-ac3e-127debc90712.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7572066a-0cea-41fd-ac3e-127debc90712', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/swim compete_7572066a-0cea-41fd-ac3e-127debc90712.svg'),)
PROFILE_SOURCE_KEYS = ('solo/swimmer-with-cap-and-water',)
SOLO_SOURCE_ICON_IDS = ('swimmer-with-cap-and-water',)
REFERENCE_EXPORT_SHA256 = '4eeea497954343d9b5627b02964c3fcd0433aff4ad6259f71c20e3642c36b876'

class Drawing(Sub32):
    icon_id = 'swimmer-with-cap-and-water-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Swimmer: head in a swim cap (cap line across), above a wave.
        self.add_arc('head-1', (8, 10), (24, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('head-2', (24, 10), (8, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('cap', (8, 10), (24, 10))
        self.add_arc('wave-1', (2, 28), (16, 28), radius_x=7, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('wave-2', (16, 28), (30, 28), radius_x=7, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('wave', 'wave-1', 'wave-2')
        self.relate('connect', 'head', 'cap')
