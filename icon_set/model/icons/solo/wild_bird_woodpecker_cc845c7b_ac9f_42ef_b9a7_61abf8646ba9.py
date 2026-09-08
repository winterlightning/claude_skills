"""woodpecker-on-trunk: source silhouette re-authored on SOLO48.

Lucide bird informs coherent body arcs and sparse detail.
Keyshape VRECT_XL; extremes obtained from the SOLO48 contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc845c7b-ac9f-42ef-b9a7-61abf8646ba9'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird woodpecker_cc845c7b-ac9f-42ef-b9a7-61abf8646ba9.svg'
AUTHOR = 'gpt-6'


class WoodpeckerOnTrunk(Solo48):
    icon_id = 'woodpecker-on-trunk'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('woodpecker', 'tree', 'trunk', 'bird', 'peck', 'forest', 'beak', 'climbing')

    def build(self) -> None:
        self.add_line('trunk-top', (43, 2), (43, 46))
        self.add_arc('head', (5, 14), (21, 14), radius_x=8, radius_y=8, sweep=True)
        self.add_line('beak-top', (21, 14), (33, 10))
        self.add_line('beak-bottom', (33, 10), (23, 22))
        self.add_arc('breast', (23, 22), (23, 36), radius_x=16, radius_y=16, sweep=True)
        self.add_line('tail', (23, 36), (11, 46))
        self.add_line('back', (11, 46), (11, 20))
        self.add_arc('nape', (11, 20), (5, 14), radius_x=6, radius_y=6, sweep=False)
        self.add_contour('bird', 'head', 'beak-top', 'beak-bottom', 'breast', 'tail', 'back', 'nape', closed=True)
        self.add_line('grip', (23, 36), (43, 36))
        self.relate("connect", 'bird', 'grip')
        self.relate("connect", 'trunk-top', 'grip')
