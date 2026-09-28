"""Revision of overlapping-pompom-party-hats. Widened the two conical party hats and brought their curved brims into a shared overlap point beneath the two pompoms.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""Two Party Hats.
Plan: Two conical hats with equal small circular pompoms, taller on the left. Extrema (6,6)-(42,42).
Reference: No useful local Lucide party-hat pair match; equal circular pompoms and simple cone silhouettes.
Reduction: Overlap removed to keep both hats legible; curved hems retained, and short ties attach the pompoms.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b88b6396-c9c7-52cb-81e7-a50d04a9d8f0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__overlapping-pompom-party-hats/20260927T074149Z-thuan-mac-1/reference/party hats_b88b6396-c9c7-52cb-81e7-a50d04a9d8f0.svg'
AUTHOR = "gpt-6"


class Batch26Icon(Solo48):
    icon_id = 'overlapping-pompom-party-hats'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('two', 'party', 'hats')

    def build(self):
        for index,(x,y,half) in enumerate(((15,9,9),(33,15,9))):
            self.add_arc(f'pom-{index}-a',(x,y-3),(x,y+3),radius_x=3)
            self.add_arc(f'pom-{index}-b',(x,y+3),(x,y-3),radius_x=3)
            self.add_contour(f'pom-{index}',f'pom-{index}-a',f'pom-{index}-b',closed=True)
            apex=(x,y+3)
            self.add_polyline(f'cone-{index}',(x-half,40),apex,(x+half,40))
            self.add_arc(f'hem-{index}',(x+half,40),(x-half,40),radius_x=half,radius_y=2)
            self.relate('connect',f'pom-{index}',f'cone-{index}')
            self.relate('connect',f'cone-{index}',f'hem-{index}')
        self.relate('connect','cone-0','cone-1')
        self.relate('connect','hem-0','hem-1')
