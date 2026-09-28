"""Cold Temperature Snowflake."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'efb96faf-efa9-431a-819d-93b28b3f7c8a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/temperature snowflake 1_efb96faf-efa9-431a-819d-93b28b3f7c8a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'branched-cold-snowflake'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('snowflake', 'cold', 'ice', 'frozen', 'winter', 'crystal', 'temperature')

    def build(self):
        # Plan: Six radiating ice arms with forked vertical ends. Lucide snowflake shared center and repeated branches. Fine lateral twigs omitted for clearance. Envelope (6,6)-(42,42). Opposite arms mirrored.
        self.add_polyline('vertical',(24,6),(24,14),(24,24),(24,34),(24,42))
        self.add_polyline('diag-a',(6,14),(24,24),(42,34))
        self.add_polyline('diag-b',(6,34),(24,24),(42,14))
        for a,b in (('vertical','diag-a'),('vertical','diag-b'),('diag-a','diag-b')):self.relate('connect',a,b)
        self.add_polyline('top-fork',(16,6),(24,14),(32,6));self.relate('connect','top-fork','vertical')
        self.add_polyline('bottom-fork',(16,42),(24,34),(32,42));self.relate('connect','bottom-fork','vertical')
