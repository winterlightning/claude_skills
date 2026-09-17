"""Symmetrical Brain Hemispheres: independently authored container.

Construction plan: Two mirrored lobed hemispheres separated by a central fissure; four broad lobes per side, no detached head or body.
Keyshape VRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/artificial-intelligence/brain_332132ff-8d97-4a2d-b994-a81128e1dc07.svg. Lucide brain original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (4, 0, 60, 64).
Hosting measured with compose.py: plus does not clear, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '332132ff-8d97-4a2d-b994-a81128e1dc07'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/brain_332132ff-8d97-4a2d-b994-a81128e1dc07.svg'
AUTHOR = 'gpt-6'


class BrainHemispheresContainer(Container64):
    icon_id = 'brain-hemispheres-container'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('brain', 'hemispheres', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        for side in (-1,1):
            def p(x,y):return (32+side*x,y)
            sw=side==1
            path(self,f'hemisphere-{side}',p(4,10),[('A',p(20,10),8,8,sw),('A',p(20,26),6,8,sw),('A',p(20,42),6,8,sw),('A',p(20,54),6,6,sw),('A',p(4,54),8,8,sw),('L',p(4,10))],True)
            path(self,f'crease-top-{side}',p(20,26),[('A',p(12,22),8,4,not sw)])
            path(self,f'crease-bottom-{side}',p(20,42),[('A',p(12,46),8,4,sw)])
            join(f'hemisphere-{side}',f'crease-top-{side}')
            join(f'hemisphere-{side}',f'crease-bottom-{side}')
