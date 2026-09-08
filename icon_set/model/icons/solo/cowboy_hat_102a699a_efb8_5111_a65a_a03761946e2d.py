"""Western hat with pinched crown and upswept brim. HRECT_L (2,8)-(46,40) retains the wide hat silhouette. Lucide hat-glasses informed sloping crown sides; symmetric front view."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '102a699a-efb8-5111-a65a-a03761946e2d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/hat cowboy_102a699a-efb8-5111-a65a-a03761946e2d.svg'
AUTHOR = 'astra-chatgpt'


class CowboyHat(Solo48):
    icon_id = 'cowboy-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('hat', 'cowboy hat', 'western', 'stetson', 'brim', 'ranch', 'headwear', 'country')

    def build(self) -> None:
        self.add_polyline('crown', (11, 29), (16, 8), (24, 12), (32, 8), (37, 29), closed=False)
        self.add_arc('brim-top', (2, 24), (46, 24), radius_x=30, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('brim-base', (46, 24), (2, 24), radius_x=22, radius_y=16, sweep=True, large_arc=False)
        self.add_contour('brim', 'brim-top', 'brim-base', closed=True)
        self.relate("connect", 'crown', 'brim')
