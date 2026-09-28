'Snowflake: six balanced arms with real shared branch nodes replace misaligned overlapping twigs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34931aa4-2ff2-4490-a0da-404a030fd356'
SOURCE_PATH = 'pictographic-primitives/holidays/snowflake_34931aa4-2ff2-4490-a0da-404a030fd356.svg'
AUTHOR = 'gpt-6'

class SnowflakeHolidays(Solo48):
    icon_id = 'snowflake-holidays'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    aliases = ()
    keywords = ('snowflake', 'holidays')

    def build(self) -> None:
        # Three axes and mirrored fork pairs share exact branch nodes.
        self.add_polyline('vertical',(24,6),(24,14),(24,24),(24,34),(24,42))
        self.add_polyline('diagonal-a',(6,14),(14,19),(24,24),(34,29),(42,34))
        self.add_polyline('diagonal-b',(6,34),(14,29),(24,24),(34,19),(42,14))
        for a,b in (('vertical','diagonal-a'),('vertical','diagonal-b'),('diagonal-a','diagonal-b')):self.relate('connect',a,b)
        for n,pts,owner in (('top',((18,9),(24,14),(30,9)),'vertical'),('bottom',((18,39),(24,34),(30,39)),'vertical'),('nw',((14,11),(14,19),(6,21)),'diagonal-a'),('se',((34,37),(34,29),(42,27)),'diagonal-a'),('sw',((6,27),(14,29),(14,37)),'diagonal-b'),('ne',((42,21),(34,19),(34,11)),'diagonal-b')):
            self.add_polyline(n,*pts);self.relate('connect',n,owner)
