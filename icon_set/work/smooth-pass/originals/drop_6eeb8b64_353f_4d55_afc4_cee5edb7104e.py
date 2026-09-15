"""Drop (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6eeb8b64-353f-4d55-afc4-cee5edb7104e'
SOURCE_PATH = 'icons-json/smileys/drop_6eeb8b64-353f-4d55-afc4-cee5edb7104e.json'
AUTHOR = 'gpt-6'

class DropSmileys(Solo48):
    icon_id = 'drop-smileys'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('drop', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0', (24, 35), (31, 28), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e1-1', (23, 5), (8, 29), radius_x=38, radius_y=38, large_arc=False, sweep=False)
        self.add_arc('e1-2', (8, 29), (16, 42), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_line('e1-3', (16, 42), (24, 44))
        self.add_line('e1-4', (24, 44), (32, 42))
        self.add_arc('e1-5', (32, 42), (40, 29), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_arc('e1-6', (40, 29), (24, 4), radius_x=41, radius_y=41, large_arc=False, sweep=False)
        self.add_line('e1-7', (24, 4), (23, 5))
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7'), closed=True)
