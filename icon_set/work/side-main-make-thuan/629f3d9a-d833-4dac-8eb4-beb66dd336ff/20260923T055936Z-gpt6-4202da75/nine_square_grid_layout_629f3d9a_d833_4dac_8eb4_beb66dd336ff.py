"""A rounded square divided into nine equal cells."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "629f3d9a-d833-4dac-8eb4-beb66dd336ff"
SOURCE_PATH = "pictographic-primitives/_uncategorized_21/grid_629f3d9a-d833-4dac-8eb4-beb66dd336ff.svg"
AUTHOR = "gpt-6"


class NineSquareGridLayout(Solo48):
    icon_id = "nine-square-grid-layout"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/layout"
    aliases = ("three by three grid", "nine cell layout")
    keywords = ("grid", "collage", "tiles", "layout")

    def build(self) -> None:
        # Shared grid coordinates 6, 18, 30, 42 give three equal 12-unit
        # cells per axis. The radius-four perimeter is split at every join.
        outline = []
        def line(name, a, b):
            self.add_line(name, a, b); outline.append(name)
        def arc(name, a, b):
            self.add_arc(name, a, b, radius_x=4); outline.append(name)
        for i, (a, b) in enumerate((((10, 6), (18, 6)),
                                    ((18, 6), (30, 6)),
                                    ((30, 6), (38, 6)))):
            line(f"top-{i}", a, b)
        arc("ne", (38, 6), (42, 10))
        for i, (a, b) in enumerate((((42, 10), (42, 18)),
                                    ((42, 18), (42, 30)),
                                    ((42, 30), (42, 38)))):
            line(f"right-{i}", a, b)
        arc("se", (42, 38), (38, 42))
        for i, (a, b) in enumerate((((38, 42), (30, 42)),
                                    ((30, 42), (18, 42)),
                                    ((18, 42), (10, 42)))):
            line(f"bottom-{2-i}", a, b)
        arc("sw", (10, 42), (6, 38))
        for i, (a, b) in enumerate((((6, 38), (6, 30)),
                                    ((6, 30), (6, 18)),
                                    ((6, 18), (6, 10)))):
            line(f"left-{2-i}", a, b)
        arc("nw", (6, 10), (10, 6))
        self.add_contour("outer-grid", *outline, closed=True)

        coords = (6, 18, 30, 42)
        for x in (18, 30):
            for i in range(3):
                self.add_line(f"v{x}-{i}", (x, coords[i]), (x, coords[i+1]))
        for y in (18, 30):
            for i in range(3):
                self.add_line(f"h{y}-{i}", (coords[i], y), (coords[i+1], y))

        for x, top, bottom in ((18, "top-0", "bottom-0"),
                               (30, "top-1", "bottom-1")):
            self.relate("connect", f"v{x}-0", top)
            self.relate("connect", f"v{x}-2", bottom)
        for y, left, right in ((18, "left-1", "right-0"),
                               (30, "left-2", "right-1")):
            self.relate("connect", f"h{y}-0", left)
            self.relate("connect", f"h{y}-2", right)
        for x, col in ((18, 0), (30, 1)):
            for y, row in ((18, 0), (30, 1)):
                for vi in (row, row+1):
                    for hi in (col, col+1):
                        self.relate("connect", f"v{x}-{vi}", f"h{y}-{hi}")
