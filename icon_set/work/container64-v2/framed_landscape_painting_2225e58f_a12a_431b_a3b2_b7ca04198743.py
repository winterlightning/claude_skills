"""A wide framed landscape with two mountain peaks and a sun. HRECT_L spans x=2..62 and y=10..54. Lucide image informs the rounded enclosure and compact landscape. The outer frame owns a separate inset opening and mountains/sun. Angular peaks replace fine source curvature for clarity.

Source rendered and inspected before authoring. Preserve the saved user classification.
Lucide image and ticket-x originals and atomic geometry informed coherent contours
and rounded enclosures; human reference used only for the three human scenes.
Hosting via compose.py using existing sub IDs: plus-sign-batch-04 invalid, heart-state-63 invalid, check-mark invalid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (framed-landscape-painting HRECT_L -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4. Hand-repaired after the fit: 8-unit matte; sun and hills re-seated inside the opening.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '2225e58f-a12a-431b-a3b2-b7ca04198743'
SOURCE_PATH = 'pictographic-primitives/entertainment/museum painting_2225e58f-a12a-431b-a3b2-b7ca04198743.svg'
AUTHOR = 'claude-opus-5-5'


class QueueIcon(Container64):
    icon_id = 'framed-landscape-painting'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ('Framed Landscape Painting',)
    keywords = ('framed', 'landscape', 'painting')

    def build(self) -> None:
        self.add_line('frame-0', (9, 12), (55, 12))
        self.add_arc('frame-1', (55, 12), (60, 16), radius_x=5, radius_y=4)
        self.add_line('frame-2', (60, 16), (60, 48))
        self.add_arc('frame-3', (60, 48), (55, 52), radius_x=5, radius_y=4)
        self.add_line('frame-4', (55, 52), (9, 52))
        self.add_arc('frame-5', (9, 52), (4, 48), radius_x=5, radius_y=4)
        self.add_line('frame-6', (4, 48), (4, 16))
        self.add_arc('frame-7', (4, 16), (9, 12), radius_x=5, radius_y=4)
        self.add_line('opening-1', (12, 20), (52, 20))
        self.add_line('opening-2', (52, 20), (52, 44))
        self.add_line('opening-3', (52, 44), (12, 44))
        self.add_line('opening-4', (12, 44), (12, 20))
        self.add_line('hills-1', (19, 38), (28, 34))
        self.add_line('hills-2', (28, 34), (33, 38))
        self.add_line('hills-3', (33, 38), (41, 27))
        self.add_line('hills-4', (41, 27), (46, 38))
        self.add_arc('sun-a', (18, 28), (22, 28), radius_x=2)
        self.add_arc('sun-b', (22, 28), (18, 28), radius_x=2)
        self.add_contour('frame', 'frame-0', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7', closed=True)
        self.add_contour('opening', 'opening-1', 'opening-2', 'opening-3', 'opening-4')
        self.add_contour('hills', 'hills-1', 'hills-2', 'hills-3', 'hills-4')
        self.add_contour('sun', 'sun-a', 'sun-b', closed=True)
