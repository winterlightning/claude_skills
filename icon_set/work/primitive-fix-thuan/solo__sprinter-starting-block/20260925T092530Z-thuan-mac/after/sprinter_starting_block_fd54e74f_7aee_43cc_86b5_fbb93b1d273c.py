"""Running ready: a sprinter's foot and shoe set on the track, toe down,
beside the sloped pedal of a starting block.

Symbol plan: the leg/shoe is two open runs meeting the ground at the toe
node - the front (shin, instep with two lace ticks at split nodes 8 apart,
toe curve) and the back (calf, rounded heel, straight sole). The block is
an open wedge standing on two ground-line nodes; its pedal face is parallel
to the sole and 8+ from it. The ground line is split at the toe and at the
block's corners. Deliberately asymmetric (a side view).
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: footprints / shoe outline (open leg strokes into a toe,
lace ticks); the block follows Lucide's wedge/triangle construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fd54e74f-7aee-43cc-86b5-fbb93b1d273c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__sprinter-starting-block/20260925T092530Z-thuan-mac/reference/running ready starting block_fd54e74f-7aee-43cc-86b5-fbb93b1d273c.svg"
AUTHOR = "claude-opus-5-5"


class SprinterStartingBlock(Solo48):
    icon_id = "sprinter-starting-block"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("starting block", "ready to run", "sprint start")
    keywords = ("running", "sprint", "starting block", "race", "shoe", "track")

    def build(self) -> None:
        ground, toe = 42, (15, 42)
        laces = (22, 30)
        # Front of leg and shoe.
        self.add_line("front-1", (6, 12), (13, 18))
        self.add_line("front-2", (13, 18), (13, laces[0]))
        self.add_line("front-3", (13, laces[0]), (13, laces[1]))
        self.add_bezier("front-4", (13, laces[1]), ((12, 35), (11, 40), toe))
        self.add_contour("front", "front-1", "front-2", "front-3", "front-4")
        for index, y in enumerate(laces, 1):
            self.add_line(f"lace-{index}", (13, y), (17, y))
            self.relate("connect", "front", f"lace-{index}")
        # Back of leg: calf, heel, sole.
        self.add_line("back-1", (23, 6), (33, 12))
        self.add_bezier("back-2", (33, 12), ((37, 14.5), (36, 18), (33, 22)))
        self.add_line("back-3", (33, 22), toe)
        self.add_contour("back", "back-1", "back-2", "back-3")
        # Ground and starting block.
        self.add_line("ground-1", (10, ground), toe)
        self.add_line("ground-2", toe, (26, ground))
        self.add_line("ground-3", (26, ground), (42, ground))
        self.add_contour("ground", "ground-1", "ground-2", "ground-3")
        self.add_polyline("block", (26, ground), (36, 31), (42, ground))
        for part in ("front", "back", "block"):
            self.relate("connect", "ground", part)
        self.relate("connect", "front", "back")
