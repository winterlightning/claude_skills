"""Left-facing standing songbird; extremes (2,2)-(46,46). Lucide bird informs rounded breast, wing and attached legs; asymmetric profile retained."""
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
    category = "nature/animals"
    aliases = ()
    keywords = ('bird', 'songbird', 'standing', 'wing', 'beak', 'wildlife', 'garden', 'perch')

    def build(self) -> None:
        self.add_arc('crown', (8, 12), (20, 2), radius_x=12, radius_y=10, sweep=True)
        self.add_arc('nape', (20, 2), (30, 8), radius_x=12, radius_y=12, sweep=True)
        self.add_line('back', (30, 8), (46, 38))
        self.add_line('tail', (46, 38), (35, 36))
        self.add_arc('belly', (35, 36), (24, 38), radius_x=20, radius_y=16, sweep=True)
        self.add_arc('belly-left', (24, 38), (12, 29), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('chest', (12, 29), (8, 12), radius_x=24, radius_y=24, sweep=True)
        self.add_contour('body', 'crown', 'nape', 'back', 'tail', 'belly', 'belly-left', 'chest', closed=True)
        self.add_line('beak', (8, 12), (2, 12))
        self.relate("connect", 'beak', 'body')
        self.add_arc('wing', (22, 16), (33, 29), radius_x=11, radius_y=13, sweep=False)
        self.add_line('leg-left', (24, 38), (21, 46))
        self.add_line('leg-right', (35, 36), (32, 46))
        self.relate("connect", 'leg-left', 'body')
        self.relate("connect", 'leg-right', 'body')
