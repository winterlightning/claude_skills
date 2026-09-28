"""An upright document with a stepped notch at its top right edge holds three horizontal text lines.

Plan: Upright page with an intrinsic top-right step; text rows share a 9-unit pitch.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: file-text: page silhouette and repeated text strokes.
Simplification: Corner rounding omitted; stepped notch and three text rows retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f4cacc67-26d4-47e8-b34a-ab263a5379c5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-news-logo/20260927T055654Z-thuan-mac-1/reference/google news logo_f4cacc67-26d4-47e8-b34a-ab263a5379c5.svg'
AUTHOR = "gpt-6"


class GoogleNewsLogo(Solo48):
    icon_id = 'google-news-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-news', 'google', 'news', 'document', 'logo', 'brand', 'articles')

    def build(self):
        self.add_polyline('page',(8,4),(28,4),(40,16),(40,44),(8,44),closed=True)
        for i,(y,right) in enumerate(((18,23),(27,31),(36,25))):
            self.add_line(f'text-{i}',(17,y),(right,y))
