"""microsoft-visual-studio-logo-1: smooth geometric reconstruction on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c2d7127b-4a91-4f1f-9461-fcc33608bdcb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__microsoft-visual-studio-logo-1/20260927T153322Z-thuan-mac-1/reference/microsoft visual studio logo 1_c2d7127b-4a91-4f1f-9461-fcc33608bdcb.svg'
AUTHOR = "gpt-6"
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MicrosoftVisualStudioLogo1(Solo48):
    icon_id = 'microsoft-visual-studio-logo-1'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('microsoft', 'visual', 'studio', 'logo', 'logos')

    def build(self):
        # Horizontally broad infinity loops, as in the original thin-line mark.
        points = [
            ((24,24),(18,16),(17,10),(12,10)),
            ((12,10),(7,10),(4,17),(4,24)),
            ((4,24),(4,31),(7,38),(12,38)),
            ((12,38),(17,38),(18,32),(24,24)),
            ((24,24),(30,16),(31,10),(36,10)),
            ((36,10),(41,10),(44,17),(44,24)),
            ((44,24),(44,31),(41,38),(36,38)),
            ((36,38),(31,38),(30,32),(24,24)),
        ]
        for n, (start, c1, c2, end) in enumerate(points):
            self.add_bezier(f'loop-{n}', start, (c1, c2, end))
        self.add_contour('infinity', *(f'loop-{n}' for n in range(8)), closed=True)
