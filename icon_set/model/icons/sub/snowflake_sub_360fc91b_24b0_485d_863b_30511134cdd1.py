"""Snowflake: A vertical and horizontal axis cross at the centre, each carrying two short angled branches near its outer ends. The resulting snowflake has four evenly distributed branching arms.

Construction: Four branched arms share one centre, with branch points derived from cardinal axes.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '360fc91b-24b0-485d-863b-30511134cdd1'
SOURCE_PATH = 'pictographic-primitives/state/snowflake 1_360fc91b-24b0-485d-863b-30511134cdd1.svg'
AUTHOR = 'gpt-6'


class SnowflakeSub(Sub32):
    icon_id = 'snowflake-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('snowflake', 'vertical', 'horizontal', 'axis', 'cross', 'centre', 'carrying', 'short')

    def build(self):
        self.add_polyline("vertical",(16,2),(16,16),(16,30))
        self.add_polyline("horizontal",(2,16),(16,16),(30,16))
        self.relate("connect","vertical","horizontal")
        for name,points,axis in (("top",((10,4),(16,10),(22,4)),"vertical"),("bottom",((10,28),(16,22),(22,28)),"vertical"),("left",((4,10),(10,16),(4,22)),"horizontal"),("right",((28,10),(22,16),(28,22)),"horizontal")):
            self.add_polyline(name,*points)
            self.relate("connect",axis,name)
