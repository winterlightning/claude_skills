"""A large circle holds eight short strokes radiating evenly around an empty centre, like a starburst.

Plan: Circular border and eight radial strokes sharing one center.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: asterisk: shared radial center.
Simplification: All eight rays retained; central gap closes into a shared junction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99aca13e-621b-4224-a7d5-50e282c5a5ba'
SOURCE_PATH = 'pictographic-primitives/logos/jasmine logo_99aca13e-621b-4224-a7d5-50e282c5a5ba.svg'
AUTHOR = 'gpt-6'


class JasmineLogo(Solo48):
    icon_id = 'jasmine-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('jasmine', 'testing', 'javascript', 'starburst', 'logo', 'brand', 'developer')

    def build(self):
        self.add_arc('ca',(44,24),(4,24),radius_x=20)
        self.add_arc('cb',(4,24),(44,24),radius_x=20)
        self.add_contour('circle','ca','cb',closed=True)
        ends=[(24,13),(32,16),(35,24),(32,32),(24,35),(16,32),(13,24),(16,16)]
        for i,p in enumerate(ends):self.add_line(f'ray{i}',(24,24),p)
        for i in range(8):
         for j in range(i):self.relate('connect',f'ray{i}',f'ray{j}')
