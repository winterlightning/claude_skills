'Eye: balanced smooth almond-like envelope and a circular iris with generous clear space.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a73a3ea1-b1ee-5adb-a13b-215a290d268a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/view_a73a3ea1-b1ee-5adb-a13b-215a290d268a.svg'
AUTHOR = 'gpt-6'

class View(Solo48):
    icon_id = 'view'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('view', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('upper', (4, 24), (44, 24), radius_x=20, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('lower', (44, 24), (4, 24), radius_x=20, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('iris-top', (17, 24), (31, 24), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('iris-bottom', (31, 24), (17, 24), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('eye', *('upper', 'lower'), closed=True)
        self.add_contour('iris', *('iris-top', 'iris-bottom'), closed=True)
