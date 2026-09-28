"""A rounded lowercase d with a broad outlined slanted ascender.

The ascender shares the bowl at its upper right and keeps the source's
recognizable open bar instead of collapsing it to one diagonal stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '736f5f12-9937-43b3-9e38-dc6ced29e872'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-domains-logo/20260927T055616Z-thuan-mac-1/reference/google domain logo_736f5f12-9937-43b3-9e38-dc6ced29e872.svg'
AUTHOR = 'gpt-6'


class GoogleDomainsLogo(Solo48):
    icon_id = 'google-domains-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-domains', 'google', 'domain', 'letter-d', 'logo', 'brand', 'web')

    def build(self):
        self.add_arc('bowl-top',(6,29),(28,29),radius_x=11)
        self.add_arc('bowl-bottom',(28,29),(6,29),radius_x=11)
        self.add_contour('bowl','bowl-top','bowl-bottom',closed=True)
        self.add_polyline('ascender',(28,29),(32,6),(42,6),(34,42),(27,42))
        self.relate('connect','bowl','ascender')
