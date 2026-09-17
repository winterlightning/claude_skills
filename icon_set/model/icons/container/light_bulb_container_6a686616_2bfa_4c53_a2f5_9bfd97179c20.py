"""Electric Light Bulb Symbol: independently authored container.

Construction plan: Round globe flows into a narrow base with two bands; mirrored shoulders preserve the bulb.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/work/bulb_6a686616-2bfa-4c53-a2f5-9bfd97179c20.svg. Lucide lightbulb original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '6a686616-2bfa-4c53-a2f5-9bfd97179c20'
SOURCE_PATH = 'pictographic-primitives/work/bulb_6a686616-2bfa-4c53-a2f5-9bfd97179c20.svg'
AUTHOR = 'gpt-6'


class LightBulbContainer(Container64):
    icon_id = 'light-bulb-container'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('light', 'bulb', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'bulb',(24,46),[('L',(24,42)),('A',(10,22),22,24,True),('A',(54,22),22,20,True),('A',(40,42),22,24,True),('L',(40,46))])
        poly('base',(24,46),(24,54),(40,54),(40,46),(24,46));join('base','bulb')
        path(self,'tip',(26,54),[('L',(26,56)),('A',(38,56),6,6,False),('L',(38,54))]);join('tip','base')
