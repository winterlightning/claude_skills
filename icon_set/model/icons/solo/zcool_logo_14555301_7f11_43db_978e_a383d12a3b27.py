"""A Z inside a flame-shaped logo.
Symbol plan and construction: flame: a coherent curved flame silhouette with intentional tips.
Keyshape: SQUARE preserves the round lower body and rising upper tips.
Omissions: The smallest third flame notch.
Review: Two defining tips and the Z remain clear; the tiny tertiary notch was removed to open the crowded contour. Flame asymmetry follows the source."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='14555301-7f11-43db-978e-a383d12a3b27'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_40/zcool logo_14555301-7f11-43db-978e-a383d12a3b27.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='zcool-logo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('zcool', 'logo')

    # Visible extrema (4, 4, 44, 44); centerline extremes (6, 6, 42, 42).
    # For CIRCLE the envelope is radial: center (24,24), centerline radius 20.
    def build(self):
        # Three flame tips over a round lower bowl with an independently drawn Z.
        self.add_bezier('flame-upper',(30,6),((30,11),(29,14),(28,17)),
            ((34,17),(38,14),(42,12)),((42,28),(38,42),(24,42)))
        self.add_bezier('flame-lower',(24,42),((12,42),(6,38),(6,26)),
            ((6,18),(12,12),(21,11)),((25,10),(28,8),(30,6)))
        self.add_contour('flame','flame-upper','flame-lower',closed=True)
        self.add_polyline('z',(17,25),(25,25),(17,33),(25,33))
