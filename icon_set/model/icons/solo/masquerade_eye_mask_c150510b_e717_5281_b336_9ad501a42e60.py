"""Masquerade Party Eye Mask.
Plan: Mirrored mask with lifted corners, nose dips and two circular eye openings. Extrema (4,10)-(44,38).
Reference: No useful local Lucide eye-mask match; mirrored smooth cheeks and equal eyes.
Reduction: Almond openings reduced to circles to retain clear holes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c150510b-e717-5281-b336-9ad501a42e60'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/party mask_c150510b-e717-5281-b336-9ad501a42e60.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'masquerade-eye-mask'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/celebrations"
    aliases = ()
    keywords = ('masquerade', 'party', 'eye', 'mask')

    def build(self):

        self.add_bezier('top',(4,10),((12,10),(18,10),(24,16)),((30,10),(36,10),(44,10)))
        self.add_line('right',(44,10),(44,24))
        self.add_arc('right-cheek',(44,24),(34,38),radius_x=10,radius_y=14)
        self.add_bezier('lower',(34,38),((29,38),(29,34),(24,34)),((19,34),(19,38),(14,38)))
        self.add_arc('left-cheek',(14,38),(4,24),radius_x=10,radius_y=14)
        self.add_line('left',(4,24),(4,10))
        self.add_contour('mask','top','right','right-cheek','lower','left-cheek','left',closed=True)
        for i,x in enumerate((16,32)):
            self.add_arc(f'eye-{i}-a',(x-3,24),(x+3,24),radius_x=3)
            self.add_arc(f'eye-{i}-b',(x+3,24),(x-3,24),radius_x=3)
            self.add_contour(f'eye-{i}',f'eye-{i}-a',f'eye-{i}-b',closed=True)
