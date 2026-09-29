"""A large circle is crossed by a single smooth wave that rises from the left edge to a crest near the centre and falls to the right edge.

Plan: Circle radius 20 with a two-part smooth wave joined at its left and right cardinal points.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: No useful exact local Lucide match; tangent-continuous wave inside a circle.
Simplification: Single wave retained; deliberate off-centre crest.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8555acb-9beb-49f8-8fcb-c5960dfa8ebb'
SOURCE_PATH = 'pictographic-primitives/logos/grooveshark logo_e8555acb-9beb-49f8-8fcb-c5960dfa8ebb.svg'
AUTHOR = 'gpt-6'


class GroovesharkLogo(Solo48):
    icon_id = 'grooveshark-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('grooveshark', 'music', 'wave', 'logo', 'brand', 'streaming', 'audio')

    def build(self):
        self.add_arc('circle-top',(4,24),(44,24),radius_x=20)
        self.add_arc('circle-bottom',(44,24),(4,24),radius_x=20)
        self.add_contour('circle','circle-top','circle-bottom',closed=True)
        self.add_bezier('wave',(4,24),((10,24),(10,12),(18,12)),((28,12),(28,24),(44,24)))
        self.relate('connect','circle','wave')
