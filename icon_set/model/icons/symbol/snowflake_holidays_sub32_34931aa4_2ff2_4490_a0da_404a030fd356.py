"""Independent 32px profile of snowflake-holidays.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '34931aa4-2ff2-4490-a0da-404a030fd356'
SOURCE_PATH = 'pictographic-primitives/holidays/snowflake_34931aa4-2ff2-4490-a0da-404a030fd356.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('34931aa4-2ff2-4490-a0da-404a030fd356', 'pictographic-primitives/holidays/snowflake_34931aa4-2ff2-4490-a0da-404a030fd356.svg'),)
PROFILE_SOURCE_KEYS = ('solo/snowflake-holidays',)
SOLO_SOURCE_ICON_IDS = ('snowflake-holidays',)
REFERENCE_EXPORT_SHA256 = '47724b202bb6ad0617ec783d8734dc850c6c8f0bdf883c065e9f225fb20e6ad5'

class Drawing(Sub32):
    icon_id = 'snowflake-holidays-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Snowflake: three crossing arms with a short fork at each tip, forks 4 units clear of the next arm.
        self.add_line('arm-a', (16, 5), (16, 27))
        self.add_line('arm-b', (6, 10), (26, 22))
        self.add_line('arm-c', (6, 22), (26, 10))
        self.relate('connect', 'arm-a', 'arm-b')
        self.relate('connect', 'arm-a', 'arm-c')
        self.relate('connect', 'arm-b', 'arm-c')
        self.add_line('fork-0-l', (16, 5), (13, 2))
        self.relate('connect', 'arm-a', 'fork-0-l')
        self.add_line('fork-0-r', (16, 5), (19, 2))
        self.relate('connect', 'arm-a', 'fork-0-r')
        self.add_line('fork-1-l', (26, 10), (27, 6))
        self.relate('connect', 'arm-c', 'fork-1-l')
        self.add_line('fork-1-r', (26, 10), (30, 11))
        self.relate('connect', 'arm-c', 'fork-1-r')
        self.add_line('fork-2-l', (26, 22), (30, 21))
        self.relate('connect', 'arm-b', 'fork-2-l')
        self.add_line('fork-2-r', (26, 22), (27, 26))
        self.relate('connect', 'arm-b', 'fork-2-r')
        self.add_line('fork-3-l', (16, 27), (19, 30))
        self.relate('connect', 'arm-a', 'fork-3-l')
        self.add_line('fork-3-r', (16, 27), (13, 30))
        self.relate('connect', 'arm-a', 'fork-3-r')
        self.add_line('fork-4-l', (6, 22), (5, 26))
        self.relate('connect', 'arm-c', 'fork-4-l')
        self.add_line('fork-4-r', (6, 22), (2, 21))
        self.relate('connect', 'arm-c', 'fork-4-r')
        self.add_line('fork-5-l', (6, 10), (2, 11))
        self.relate('connect', 'arm-b', 'fork-5-l')
        self.add_line('fork-5-r', (6, 10), (5, 6))
        self.relate('connect', 'arm-b', 'fork-5-r')
