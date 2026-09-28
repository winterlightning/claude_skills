"""Symmetrical Brain Hemispheres: independently authored container.

Construction plan: Two broad mirrored lobed hemispheres share one central fissure. Three attached folds per side; no detached head or body.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/artificial-intelligence/brain_332132ff-8d97-4a2d-b994-a81128e1dc07.svg. Lucide brain original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus, heart and check pass automated checks.
The continuous central fissure remains intrinsic furniture; composition may need
to mask that seam behind a child, as the source chip composition does.
SQUARE preserves the broad top-view silhouette. Lucide brain informed shared
seam and attached fold construction; the source owns the four-lobe silhouette.
Human bust references are not applicable to this isolated organ.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '332132ff-8d97-4a2d-b994-a81128e1dc07'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_332132ff-8d97-4a2d-b994-a81128e1dc07.svg'
AUTHOR = 'gpt-6'

class BrainHemispheresContainer(Container64):
    icon_id = 'brain-hemispheres-container'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('brain', 'hemispheres', 'container')

    def build(self):
        # One shared central fissure; broad mirrored lobes own all fold nodes.
        self.add_line('fissure', (32, 14), (32, 54))
        for side in (-1, 1):
            def p(x, y): return (32 + side*x, y)
            sw = side == 1
            outline = f'hemisphere-{side}'
            path(self, outline, p(0,14), [
                ('A',p(20,14),10,12,sw),
                ('A',p(20,38),10,12,sw),
                ('A',p(16,54),8,8,sw),
                ('A',p(0,54),8,8,sw),
            ])
            self.relate('connect', 'fissure', outline)
            path(self,f'fold-top-{side}',p(20,14),[('A',p(12,22),8,8,sw)])
            path(self,f'fold-middle-{side}',p(20,38),[('A',p(12,36),8,8,sw)])
            path(self,f'fold-bottom-{side}',p(16,54),[('A',p(12,46),8,8,sw)])
            for name in ('top','middle','bottom'):
                self.relate('connect',outline,f'fold-{name}-{side}')
        self.relate('connect','hemisphere--1','hemisphere-1')
