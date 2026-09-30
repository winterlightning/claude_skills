"""A clipped page encloses an upper-left sun and a two-peak mountain silhouette. Lower peak deliberately differs from higher right peak. Lucide file-image informed page and circular-sun construction, source supplies detached closed landscape.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: invalid, review, invalid. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: VRECT_XL; fine source details simplified only for native readability.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (landscape-picture-media-file VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '41f3ad63-cd17-441d-b26d-945da63c6f7c'
SOURCE_PATH = 'pictographic-primitives/files/image file_41f3ad63-cd17-441d-b26d-945da63c6f7c.svg'
AUTHOR = 'claude-opus-5-5'


class Icon(Container64):
    icon_id = 'landscape-picture-media-file'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    categories = ('files', 'other', 'primitives-generate')
    aliases = ('Landscape Picture Media File',)
    keywords = ('landscape', 'picture', 'media', 'file')

    def build(self) -> None:
        self.add_line('page-upper-1', (12, 4), (41, 4))
        self.add_line('page-upper-2', (41, 4), (54, 18))
        self.add_line('page-upper-3', (54, 18), (54, 57))
        self.add_arc('page-br', (54, 57), (52, 60), radius_x=2, radius_y=3)
        self.add_line('page-bottom', (52, 60), (12, 60))
        self.add_arc('page-bl', (12, 60), (10, 57), radius_x=2, radius_y=3)
        self.add_line('page-left', (10, 57), (10, 7))
        self.add_arc('page-tl', (10, 7), (12, 4), radius_x=2, radius_y=3)
        self.add_arc('sun-top', (21, 22), (31, 22), radius_x=5)
        self.add_arc('sun-bottom', (31, 22), (21, 22), radius_x=5)
        self.add_line('mountains-1', (18, 51), (26, 38))
        self.add_line('mountains-2', (26, 38), (31, 44))
        self.add_line('mountains-3', (31, 44), (39, 32))
        self.add_line('mountains-4', (39, 32), (47, 51))
        self.add_line('mountains-5', (47, 51), (18, 51))
        self.add_contour('page', 'page-upper-1', 'page-upper-2', 'page-upper-3', 'page-br', 'page-bottom', 'page-bl', 'page-left', 'page-tl', closed=True)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
        self.add_contour('mountains', 'mountains-1', 'mountains-2', 'mountains-3', 'mountains-4', 'mountains-5', closed=True)
