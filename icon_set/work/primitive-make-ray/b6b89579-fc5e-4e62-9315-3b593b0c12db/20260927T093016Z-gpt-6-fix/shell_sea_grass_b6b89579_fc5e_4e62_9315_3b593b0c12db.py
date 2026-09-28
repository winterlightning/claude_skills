from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b6b89579-fc5e-4e62-9315-3b593b0c12db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__shell-with-seagrass/20260927T092933Z-thuan-mac-1/reference/shell sea grass_b6b89579-fc5e-4e62-9315-3b593b0c12db.svg'
AUTHOR = "gpt-6"


class ShellWithSeagrass(Solo48):
    icon_id = 'shell-with-seagrass'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('shell', 'seagrass', 'seaweed', 'ocean', 'beach', 'marine', 'clam', 'underwater')

    def build(self) -> None:
        self.add_arc('shell', (6, 42), (42, 42), radius_x=18, radius_y=15, sweep=True, large_arc=False)
        self.add_line('base', (42, 42), (6, 42))
        self.add_contour('clam', 'shell', 'base', closed=True)
        self.add_arc('left-a', (10, 7), (10, 15), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('left-b', (10, 15), (10, 21), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('left', 'left-a', 'left-b', closed=False)
        self.add_arc('middle-a', (24, 6), (24, 10), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('middle-b', (24, 10), (24, 18), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('middle', 'middle-a', 'middle-b', closed=False)
        self.add_arc('right-a', (38, 7), (38, 15), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('right-b', (38, 15), (38, 21), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('right', 'right-a', 'right-b', closed=False)
