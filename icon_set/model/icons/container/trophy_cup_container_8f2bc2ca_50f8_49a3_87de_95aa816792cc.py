"""Victory Achievement Trophy Cup: independently authored container.

Construction plan: Symmetric deep cup, two loop handles, flared stem and plinth; preserve all trophy features.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/business/trophy_8f2bc2ca-50f8-49a3-87de-95aa816792cc.svg. Lucide trophy original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '8f2bc2ca-50f8-49a3-87de-95aa816792cc'
SOURCE_PATH = 'pictographic-primitives/business/trophy_8f2bc2ca-50f8-49a3-87de-95aa816792cc.svg'
AUTHOR = 'gpt-6'


class TrophyCupContainer(Container64):
    icon_id = 'trophy-cup-container'
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('trophy', 'cup', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'cup',(14,2),[('L',(14,22)),('A',(32,44),18,22,False),('A',(50,22),18,22,False),('L',(50,2)),('L',(14,2))],True)
        for side in (-1,1):
            x=32+side*18
            path(self,f'handle-{side}',(x,10),[('L',(32+side*30,10)),('A',(x,22),12,12,side>0)])
            join('cup',f'handle-{side}')
        poly('stem',(24,54),(32,44),(40,54));join('stem','cup')
        poly('base',(18,54),(46,54),(46,62),(18,62),closed=True);join('base','stem')
