'photo-vignette: independent smooth-curve repair.\n\nConstruction: Circular vignette marker with a regular six-dot ring; equal dot radii and mirrored positions.\nKeyshape: CIRCLE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/circle.svg and atomic-debug/circle.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '8e307432-0868-448a-be7b-29a7dd769da1'
SOURCE_PATH = 'pictographic-primitives/photography/photo vignette_8e307432-0868-448a-be7b-29a7dd769da1.svg'
AUTHOR = 'gpt-6'


class PhotoVignette(Solo48):
    icon_id = 'photo-vignette'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('photo', 'vignette', 'photography')
    keyshape = Keyshape.CIRCLE

    def build(self):
        ellipse(self,'ring',24,24,20)
        for i,p in enumerate(((24,13),(14,19),(14,29),(24,35),(34,29),(34,19))): self.add_dot(f'dot-{i}',p)
        contacts(self)
