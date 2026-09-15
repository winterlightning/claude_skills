"""A triangle built from three interlocking angled bands, with a smaller inverted triangle opening at its centre and clipped corners.

Plan: Hexagonal outer contour and triangular opening share the vertical axis; colour-band seams are merged.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: No useful exact logo match; shared angular band junctions.
Simplification: Band seam intersections omitted to remove two undersized triangular holes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5801c614-e252-4017-b458-23e423b033fa'
SOURCE_PATH = 'pictographic-primitives/logos/google drive logo_5801c614-e252-4017-b458-23e423b033fa.svg'
AUTHOR = 'gpt-6'


class GoogleDriveLogo(Solo48):
    icon_id = 'google-drive-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-drive', 'google', 'drive', 'storage', 'logo', 'brand', 'cloud')

    def build(self):
        # Merge colour seams; keep the three-band silhouette and triangular opening.
        self.add_polyline('outer',(19,8),(29,8),(44,32),(38,40),(10,40),(4,32),closed=True)
        self.add_polyline('opening',(24,20),(31,32),(17,32),closed=True)
