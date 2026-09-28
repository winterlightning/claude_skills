"""A large circle wraps around a smaller tilted oval ring, the two joined by a swirling stroke like interlocking curly braces.

Plan: Outer circle and inner ring with opposing sweeping connectors.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected at-sign: nested circular flow.
Simplification: Tilted oval regularized; two opposing swirl connectors retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'fd2eaa4c-1430-46f4-adcf-5755852eaadf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__json-logo/20260927T070927Z-thuan-mac-1/reference/json logo_fd2eaa4c-1430-46f4-adcf-5755852eaadf.svg'
AUTHOR = 'gpt-6'


class JsonLogo(Solo48):
    icon_id = 'json-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('json', 'data', 'format', 'swirl', 'logo', 'brand', 'developer')

    def build(self):
        self.add_arc('oa',(24,4),(24,44),radius_x=20)
        self.add_arc('ob',(24,44),(24,4),radius_x=20)
        self.add_contour('outer','oa','ob',closed=True)
        self.add_arc('ia',(24,12),(24,36),radius_x=8,radius_y=12)
        self.add_arc('ib',(24,36),(24,12),radius_x=8,radius_y=12)
        self.add_contour('inner','ia','ib',closed=True)
        self.add_bezier('upper',(24,4),((34,7),(32,12),(24,12)))
        self.add_bezier('lower',(24,44),((14,41),(16,36),(24,36)))
        for name in ('upper','lower'):
         self.relate('connect',name,'outer')
         self.relate('connect',name,'inner')
