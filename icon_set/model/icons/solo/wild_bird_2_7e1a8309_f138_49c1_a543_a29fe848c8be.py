"""Left-facing standing songbird; extremes (6,6)-(42,42). Lucide bird informs rounded breast, wing and attached legs; asymmetric profile retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e1a8309-f138-49c1-a543-a29fe848c8be'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird 2_7e1a8309-f138-49c1-a543-a29fe848c8be.svg'
AUTHOR = 'gpt-6'


class WildBird(Solo48):
    icon_id = 'wild-bird'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('bird', 'songbird', 'standing', 'wing', 'beak', 'wildlife', 'garden', 'perch')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_bezier('crown', (8, 12), *(((10.04169387, 8.06218191), (14.86974844, 6), (20, 6)),))
        self.add_bezier('nape', (20, 6), *(((23.46489918, 6), (27.12983974, 6), (30, 8)),))
        self.add_line('back', (30, 8), (42, 38))
        self.add_line('tail', (42, 38), (35, 36))
        self.add_arc('belly', (35, 36), (24, 38), radius_x=20, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('belly-left', (24, 38), (12, 29), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_arc('chest', (12, 29), (8, 12), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_line('beak', (8, 12), (6, 12))
        self.add_arc('wing', (18, 16), (29, 29), radius_x=11, radius_y=13, large_arc=False, sweep=False)
        self.add_line('leg-left', (24, 38), (21, 42))
        self.add_line('leg-right', (35, 36), (32, 42))
        self.add_contour('body', *('crown', 'nape', 'back', 'tail', 'belly', 'belly-left', 'chest'), closed=True)
        self.relate('connect', *('beak', 'body'))
        self.relate('connect', *('leg-left', 'body'))
        self.relate('connect', *('leg-right', 'body'))
