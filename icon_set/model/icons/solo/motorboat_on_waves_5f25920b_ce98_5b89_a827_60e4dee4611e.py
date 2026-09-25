"""motorboat-on-waves: reconstructed from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f25920b-ce98-5b89-a827-60e4dee4611e'
SOURCE_PATH = 'pictographic-primitives/transportation/small boat_5f25920b-ce98-5b89-a827-60e4dee4611e.svg'
AUTHOR = 'gpt-6'


class MotorboatOnWaves(Solo48):
    icon_id = 'motorboat-on-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('motorboat', 'boat', 'speedboat', 'waves', 'water', 'marine', 'sea', 'nautical')

    def build(self) -> None:

        self.add_polyline('hull',(4,19),(12,19),(32,19),(44,19),(36,28),(8,28),(4,19))
        self.add_polyline('cabin',(12,19),(16,8),(24,8),(32,19))
        for a,bs in [('cabin-1',['hull-1','hull-2']),('cabin-3',['hull-2','hull-3'])]:
            for b in bs: self.relate('connect',a,b)
        # A single continuous wave replaces the two dense source water rows.
        self.add_arc('wave-a',(4,39),(14,39),radius_x=5,radius_y=1,sweep=False)
        self.add_arc('wave-b',(14,39),(24,39),radius_x=5,radius_y=1,sweep=True)
        self.add_arc('wave-c',(24,39),(34,39),radius_x=5,radius_y=1,sweep=False)
        self.add_arc('wave-d',(34,39),(44,39),radius_x=5,radius_y=1,sweep=True)
        self.add_contour('wave','wave-a','wave-b','wave-c','wave-d')
