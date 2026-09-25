"""Decorative Flower Vase: independently authored container.

Construction plan: Narrow open neck expands into a rounded pear-shaped vase; ellipse shoulders share an axis.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.svg. Lucide droplet original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'aa457b72-c0c6-4f42-99fe-76451340672d'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.svg'
AUTHOR = 'gpt-6'


class FlowerVaseContainer(Container64):
    icon_id = 'flower-vase-container'
    category = 'decoration'
    categories = ('decoration', 'other', 'primitives-generate')
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('flower', 'vase', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'vase',(18,2),[('L',(46,2)),('L',(40,12)),('L',(40,18)),('A',(54,42),20,26,True),('A',(40,62),14,20,True),('L',(24,62)),('A',(10,42),14,20,True),('A',(24,18),20,26,True),('L',(24,12)),('L',(18,2))],True)
