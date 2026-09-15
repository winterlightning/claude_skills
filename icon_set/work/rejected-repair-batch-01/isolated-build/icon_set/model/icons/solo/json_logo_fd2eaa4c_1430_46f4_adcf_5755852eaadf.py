"""A large circle wraps around a smaller tilted oval ring, the two joined by a swirling stroke like interlocking curly braces.

Plan: Outer circle and inner ring with opposing sweeping connectors.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected at-sign: nested circular flow.
Simplification: Tilted oval regularized; two opposing swirl connectors retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd2eaa4c-1430-46f4-adcf-5755852eaadf'
SOURCE_PATH = 'pictographic-primitives/logos/json logo_fd2eaa4c-1430-46f4-adcf-5755852eaadf.svg'
AUTHOR = 'gpt-6'


class JsonLogo(Solo48):
    icon_id = 'json-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('json', 'data', 'format', 'swirl', 'logo', 'brand', 'developer')

    def build(self):
        self.add_arc('oa',(24,4),(24,44),radius_x=20)
        self.add_arc('ob',(24,44),(24,4),radius_x=20)
        self.add_contour('outer','oa','ob',closed=True)
        self.add_arc('ia',(24,14),(24,34),radius_x=10)
        self.add_arc('ib',(24,34),(24,14),radius_x=10)
        self.add_contour('inner','ia','ib',closed=True)
        self.add_bezier('upper',(24,4),((33,7),(33,14),(24,14)))
        self.add_bezier('lower',(24,44),((15,41),(15,34),(24,34)))
        for name in ('upper','lower'):
         self.relate('connect',name,'outer')
         self.relate('connect',name,'inner')
