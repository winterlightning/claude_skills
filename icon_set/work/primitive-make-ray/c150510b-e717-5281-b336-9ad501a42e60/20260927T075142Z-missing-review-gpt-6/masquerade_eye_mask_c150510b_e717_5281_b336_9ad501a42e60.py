"""Revision of masquerade-eye-mask. Opened two almond eye holes and redrew the upper brow and lower cheek as a balanced masquerade mask.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""Masquerade Party Eye Mask.
Plan: Mirrored mask with lifted corners, nose dips and two circular eye openings. Extrema (4,10)-(44,38).
Reference: No useful local Lucide eye-mask match; mirrored smooth cheeks and equal eyes.
Reduction: Almond openings reduced to circles to retain clear holes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c150510b-e717-5281-b336-9ad501a42e60'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__masquerade-eye-mask/20260927T074149Z-thuan-mac-1/reference/party mask_c150510b-e717-5281-b336-9ad501a42e60.svg'
AUTHOR = "gpt-6"


class Batch26Icon(Solo48):
    icon_id = 'masquerade-eye-mask'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('masquerade', 'party', 'eye', 'mask')

    def build(self):

        self.add_bezier('top',(4,8),((12,8),(18,8),(24,14)),((30,8),(36,8),(44,8)))
        self.add_line('right',(44,8),(44,28))
        self.add_arc('right-cheek',(44,28),(34,40),radius_x=10,radius_y=12)
        self.add_bezier('lower',(34,40),((29,40),(29,36),(24,36)),((19,36),(19,40),(14,40)))
        self.add_arc('left-cheek',(14,40),(4,28),radius_x=10,radius_y=12)
        self.add_line('left',(4,28),(4,8))
        self.add_contour('mask','top','right','right-cheek','lower','left-cheek','left',closed=True)
        for i,x in enumerate((16,32)):
            self.add_bezier(f'eye-{i}-upper',(x-4,25),((x-2,18),(x+2,18),(x+4,25)))
            self.add_bezier(f'eye-{i}-lower',(x+4,25),((x+2,32),(x-2,32),(x-4,25)))
            self.add_contour(f'eye-{i}',f'eye-{i}-upper',f'eye-{i}-lower',closed=True)
