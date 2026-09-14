"""Right-facing cobra with a smooth flared hood, S-shaped neck and pointed tail curl. Rounded contour construction preserves the supplied silhouette; tongue omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '722cb33f-03cc-5935-ab1a-86a1ade0a234'
SOURCE_PATH = 'pictographic-primitives/animals/cobra head side_722cb33f-03cc-5935-ab1a-86a1ade0a234.svg'
AUTHOR = 'gpt-6'


class CobraHead(Solo48):
    icon_id = 'cobra-head'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('cobra', 'snake', 'hood', 'reptile', 'serpent', 'venom', 'head', 'profile')

    def build(self) -> None:
        # VRECT_XL visible (6,6)-(42,42); centerlines (6,6)-(42,42).
        self.add_arc('coil', (6,42), (11,42), radius_x=6, radius_y=2)
        self.add_line('coil-top', (11,42), (17,42))
        self.add_arc('back-low', (17,42), (11,32), radius_x=6, radius_y=12, sweep=False)
        self.add_arc('hood-low', (11,32), (6,20), radius_x=6, radius_y=12)
        self.add_arc('hood-top', (6,20), (23,6), radius_x=18)
        self.add_arc('crown', (23,6), (37,10), radius_x=14, radius_y=8)
        self.add_arc('snout', (37,10), (29,18), radius_x=8)
        self.add_line('jaw', (29,18), (27,18))
        self.add_arc('throat', (27,18), (21,24), radius_x=6, sweep=False)
        self.add_arc('neck-upper', (21,24), (25,30), radius_x=4, radius_y=6, sweep=False)
        self.add_arc('neck-lower', (25,30), (29,36), radius_x=4, radius_y=6)
        self.add_line('neck-base', (29,36), (27,42))
        self.add_arc('tail-inner', (27,42), (40,24), radius_x=13, radius_y=20, sweep=False)
        self.add_line('tail-tip', (40,24), (42,32))
        self.add_arc('tail-outer', (42,32), (37,42), radius_x=6, radius_y=14)
        self.add_contour('silhouette', 'coil', 'coil-top', 'back-low', 'hood-low', 'hood-top', 'crown', 'snout', 'jaw', 'throat', 'neck-upper', 'neck-lower', 'neck-base', 'tail-inner', 'tail-tip', 'tail-outer')
