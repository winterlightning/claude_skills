"""Sparkling Fireworks Burst.
Plan: Five-ray star at left; separate curved and vertical trails suggest an irregular burst. Extrema (6,6)-(42,42).
Reference: No useful local Lucide match; the source supplies the deliberately asymmetric scattering.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47b84f76-ba07-4a3b-901f-942a22399096'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/firework_47b84f76-ba07-4a3b-901f-942a22399096.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'scattered-firework-trails'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/celebrations"
    aliases = ()
    keywords = ('sparkling', 'fireworks', 'burst')

    def build(self):

        center=(14,24)
        ends=((12,14),(6,22),(12,32),(22,30),(23,19))
        for i,p in enumerate(ends):self.add_line(f'ray-{i}',center,p)
        for i in range(5):
            for j in range(i+1,5):self.relate('connect',f'ray-{i}',f'ray-{j}')
        self.add_bezier('upper-trail',(32,22),((34,18),(38,16),(42,14)))
        self.add_bezier('lower-trail',(32,34),((36,34),(39,36),(42,38)))
        self.add_line('top-trail',(24,6),(24,10))
        self.add_line('bottom-trail',(24,40),(24,42))
