"""motorboat-on-waves: reconstructed from the supplied transportation reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5f25920b-ce98-5b89-a827-60e4dee4611e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__motorboat-on-waves/20260927T032022Z-thuan-mac-1/reference/small boat_5f25920b-ce98-5b89-a827-60e4dee4611e.svg'
AUTHOR = "gpt-6"


class MotorboatOnWaves(Solo48):
    icon_id = 'motorboat-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('motorboat', 'boat', 'speedboat', 'waves', 'water', 'marine', 'sea', 'nautical')

    def build(self) -> None:
        # The reference's two water rows are retained beneath a shallow bow.
        self.add_polyline('hull', (6, 15), (13, 15), (33, 15), (42, 15),
                          (36, 23), (12, 23), closed=True)
        self.add_polyline('cabin', (13, 15), (17, 6), (26, 6), (33, 15))
        self.relate('connect', 'hull', 'cabin')
        self.add_line('upper-water', (6, 32), (42, 32))
        ids = []
        for j, (x1, x2) in enumerate(((6, 18), (18, 30), (30, 42))):
            name = f'lower-wave-{j}'
            self.add_arc(name, (x1, 41), (x2, 41), radius_x=6,
                         radius_y=1, sweep=(j % 2 == 0))
            ids.append(name)
        self.add_contour('lower-water', *ids)
