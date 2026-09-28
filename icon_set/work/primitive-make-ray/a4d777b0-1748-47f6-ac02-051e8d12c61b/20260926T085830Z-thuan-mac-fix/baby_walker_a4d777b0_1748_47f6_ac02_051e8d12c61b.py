"""A broad tray and hanging seat supported by two curved wheeled legs. Open lower construction keeps the wheels distinct.
References: Supplied original; shared geometric construction principles.
Authored directly on SOLO48; original retained for comparison."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "a4d777b0-1748-47f6-ac02-051e8d12c61b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__baby-walker/20260926T085631Z-thuan-mac/reference/walker waling car_a4d777b0-1748-47f6-ac02-051e8d12c61b.svg"
AUTHOR = "claude-opus-5-5"

class BabyWalker(Solo48):
    icon_id = 'baby-walker'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ()
    keywords = ('baby', 'walker')

    def build(self):
        # Symbol plan (SQUARE 6..42): side-view walker as in the reference.
        # Tray: rounded bar (6,6)-(34,14) r3, bottom edge split at the post (x12)
        # and the seat (x20, x28). Post x12 from tray to base, split where the
        # rightward arm leaves it (y32). Hanging seat: U from the tray, bottom y23
        # (9 above the arm). Arm y32 runs right to 42; a box body x24..38 hangs
        # under it onto a flat base y42 from x6 to x38. No wheels.
        L = self.add_line
        join = lambda a, b: self.relate("connect", a, b)
        L("tray-top", (9, 6), (31, 6))
        self.add_arc("tray-tr", (31, 6), (34, 9), radius_x=3, radius_y=3, sweep=True)
        L("tray-right", (34, 9), (34, 11))
        self.add_arc("tray-br", (34, 11), (31, 14), radius_x=3, radius_y=3, sweep=True)
        L("tray-b1", (31, 14), (28, 14))
        L("tray-b2", (28, 14), (20, 14))
        L("tray-b3", (20, 14), (12, 14))
        L("tray-b4", (12, 14), (9, 14))
        self.add_arc("tray-bl", (9, 14), (6, 11), radius_x=3, radius_y=3, sweep=True)
        L("tray-left", (6, 11), (6, 9))
        self.add_arc("tray-tl", (6, 9), (9, 6), radius_x=3, radius_y=3, sweep=True)
        self.add_contour("tray", "tray-top", "tray-tr", "tray-right", "tray-br", "tray-b1", "tray-b2",
                         "tray-b3", "tray-b4", "tray-bl", "tray-left", "tray-tl", closed=True)
        L("seat-l", (20, 14), (20, 19))
        self.add_arc("seat-bottom", (20, 19), (28, 19), radius_x=4, radius_y=4, sweep=False)
        L("seat-r", (28, 19), (28, 14))
        self.add_contour("seat", "seat-l", "seat-bottom", "seat-r")
        join("tray", "seat")
        L("post-upper", (12, 14), (12, 32))
        L("post-lower", (12, 32), (12, 42))
        L("arm-a", (12, 32), (24, 32))
        L("arm-b", (24, 32), (38, 32))
        L("arm-c", (38, 32), (42, 32))
        L("body-l", (24, 32), (24, 42))
        L("body-r", (38, 32), (38, 42))
        L("base-a", (6, 42), (12, 42))
        L("base-b", (12, 42), (24, 42))
        L("base-c", (24, 42), (38, 42))
        for a, b in (("tray", "post-upper"), ("post-upper", "post-lower"), ("post-upper", "arm-a"),
                     ("post-lower", "arm-a"), ("arm-a", "arm-b"), ("arm-b", "arm-c"), ("arm-a", "body-l"),
                     ("arm-b", "body-l"), ("arm-b", "body-r"), ("arm-c", "body-r"), ("post-lower", "base-a"),
                     ("post-lower", "base-b"), ("base-a", "base-b"), ("base-b", "base-c"), ("body-l", "base-b"),
                     ("body-l", "base-c"), ("body-r", "base-c")):
            join(a, b)
