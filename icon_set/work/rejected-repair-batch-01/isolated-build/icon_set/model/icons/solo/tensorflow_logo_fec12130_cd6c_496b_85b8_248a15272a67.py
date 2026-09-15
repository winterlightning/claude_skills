"""Roof-angled T with a branching F arm. Reduce the outlined extrusion to single strokes and preserve the upright stem and right-side branch."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fec12130-cd6c-496b-85b8-248a15272a67'
SOURCE_PATH = 'pictographic-primitives/logos/tensorflow logo_fec12130-cd6c-496b-85b8-248a15272a67.svg'
AUTHOR = 'gpt-6'

class TensorflowLogo(Solo48):
    icon_id = 'tensorflow-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('tensorflow', 'machine-learning', 'ai', 'letter-t', 'logo', 'brand', 'google')

    def build(self):
        # Plan: Roof-angled T with a branching F arm. Reduce the outlined extrusion to single strokes and preserve the upright stem and right-side branch.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('roof',(6,18),(24,6),(42,18))
        self.add_polyline('stem',(24,6),(24,26),(24,42))
        self.add_line('f-arm',(24,26),(38,34))
        self.relate('connect','roof','stem');self.relate('connect','stem','f-arm')

