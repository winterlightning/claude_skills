"""Stereo Music Listening Headphones: independently authored container.

Construction plan: One semicircular headband connects two rounded ear cups; bilateral symmetry.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/audio/headphones_90ffd8be-8c2b-43c1-9cda-658b2b74c820.svg. Lucide headphones original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '90ffd8be-8c2b-43c1-9cda-658b2b74c820'
SOURCE_PATH = 'pictographic-primitives/audio/headphones_90ffd8be-8c2b-43c1-9cda-658b2b74c820.svg'
AUTHOR = 'gpt-6'


class HeadphonesContainer(Container64):
    icon_id = 'headphones-container'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('headphones', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'band',(10,38),[('L',(10,24)),('A',(54,24),22,22,True),('L',(54,38))])
        path(self,'left-cup',(10,38),[('L',(8,38)),('A',(2,44),6,6,False),('L',(2,56)),('A',(8,62),6,6,False),('L',(10,62)),('L',(10,38))],True)
        path(self,'right-cup',(54,38),[('L',(56,38)),('A',(62,44),6,6,True),('L',(62,56)),('A',(56,62),6,6,True),('L',(54,62)),('L',(54,38))],True)
        join('band','left-cup');join('band','right-cup')
