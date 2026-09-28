'Hammerhead: preserved arcing shark silhouette, with wider separation between the two splash strokes.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '81d0c757-f2c2-5412-a942-65c0af7e738d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__leaping-hammerhead/20260927T072903Z-thuan-mac-1/reference/shark hammer fish_81d0c757-f2c2-5412-a942-65c0af7e738d.svg'
AUTHOR = "gpt-6"


class LeapingHammerhead(Solo48):
    icon_id = 'leaping-hammerhead'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('hammerhead', 'shark', 'jump', 'leap', 'sea', 'splash', 'ocean', 'marine')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('body-1', (7, 21), (24, 6), radius_x=24, radius_y=24, large_arc=False, sweep=True)
        self.add_line('body-2', (24, 6), (30, 7))
        self.add_line('body-3', (30, 7), (22, 17))
        self.add_arc('body-4', (22, 17), (36, 19), radius_x=32, radius_y=26, large_arc=False, sweep=True)
        self.add_line('body-5', (36, 19), (42, 13))
        self.add_line('body-6', (42, 13), (40, 25))
        self.add_arc('body-7', (40, 25), (28, 42), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('body-8', (28, 42), (18, 42))
        self.add_line('body-9', (18, 42), (20, 31))
        self.add_line('body-10', (20, 31), (22, 33))
        self.add_arc('body-11', (22, 33), (31, 27), radius_x=6, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('body-12', (31, 27), (20, 19), radius_x=23, radius_y=23, large_arc=False, sweep=True)
        self.add_line('body-13', (20, 19), (16, 28))
        self.add_line('body-14', (16, 28), (7, 21))
        self.add_line('splash-1', (6, 40), (8, 42))
        self.add_line('splash-high-1', (6, 31), (8, 32))
        self.add_contour('body', *('body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12', 'body-13', 'body-14'), closed=True)
        self.add_contour('splash', *('splash-1',), closed=False)
        self.add_contour('splash-high', *('splash-high-1',), closed=False)
