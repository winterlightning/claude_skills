"""Three-House Neighbourhood. Three detached pitched-roof houses arranged one above two. The bottom pair shares dimensions and mirrors about x=24. Omit tiny doorways and overhanging eaves so all three silhouettes remain distinct.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide house: repeated closed pitched-roof contours. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c12b918-a1b5-448a-8f09-0c754a40d99f'
SOURCE_PATH = 'pictographic-primitives/real-estate/real estate neighbourhood_3c12b918-a1b5-448a-8f09-0c754a40d99f.svg'
AUTHOR = 'gpt-6'


class ThreeHouseNeighbourhood(Solo48):
    icon_id = 'three-house-neighbourhood'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "real-estate"
    categories = ("real-estate", "primitives")
    aliases = ()
    keywords = ('three', 'house', 'neighbourhood')

    def build(self) -> None:
        self.add_line('house-top-1', (24, 6), (32, 12))
        self.add_line('house-top-2', (32, 12), (32, 18))
        self.add_line('house-top-3', (32, 18), (16, 18))
        self.add_line('house-top-4', (16, 18), (16, 12))
        self.add_line('house-top-5', (16, 12), (24, 6))
        self.add_contour('house-top', 'house-top-1', 'house-top-2', 'house-top-3', 'house-top-4', 'house-top-5', closed=True)
        self.add_line('house-left-1', (13, 27), (20, 33))
        self.add_line('house-left-2', (20, 33), (20, 42))
        self.add_line('house-left-3', (20, 42), (6, 42))
        self.add_line('house-left-4', (6, 42), (6, 33))
        self.add_line('house-left-5', (6, 33), (13, 27))
        self.add_contour('house-left', 'house-left-1', 'house-left-2', 'house-left-3', 'house-left-4', 'house-left-5', closed=True)
        self.add_line('house-right-1', (35, 27), (42, 33))
        self.add_line('house-right-2', (42, 33), (42, 42))
        self.add_line('house-right-3', (42, 42), (28, 42))
        self.add_line('house-right-4', (28, 42), (28, 33))
        self.add_line('house-right-5', (28, 33), (35, 27))
        self.add_contour('house-right', 'house-right-1', 'house-right-2', 'house-right-3', 'house-right-4', 'house-right-5', closed=True)
