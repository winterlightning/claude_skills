"""A triangle built from three interlocking angled bands, with a smaller inverted triangle opening at its centre and clipped corners.

Plan: Hexagonal outer contour and triangular opening share the vertical axis; one diagonal and the base seams restore the interlocking band structure.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact logo match; shared angular band junctions.
Simplification: One of the crossing diagonals is omitted to protect the central opening.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5801c614-e252-4017-b458-23e423b033fa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-drive-logo/20260927T055620Z-thuan-mac-1/reference/google drive logo_5801c614-e252-4017-b458-23e423b033fa.svg'
AUTHOR = "gpt-6"


class GoogleDriveLogo(Solo48):
    icon_id = 'google-drive-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-drive', 'google', 'drive', 'storage', 'logo', 'brand', 'cloud')

    def build(self):
        # Merge colour seams; keep the three-band silhouette and triangular opening.
        self.add_polyline('outer',(19,8),(29,8),(44,32),(38,40),(10,40),(4,32),closed=True)
        self.add_polyline('opening',(24,20),(31,32),(17,32),closed=True)
        self.add_line('band-seam',(19,8),(24,20))
        self.relate('connect','band-seam','outer')
        self.relate('connect','band-seam','opening')
        self.add_line('base-seam-left',(4,32),(17,32))
        self.add_line('base-seam-right',(31,32),(44,32))
        for seam in ('base-seam-left','base-seam-right'):
            self.relate('connect',seam,'outer')
            self.relate('connect',seam,'opening')
