"""Two Party Hats.
Plan: Two conical hats with equal small circular pompoms, taller on the left. Extrema (6,6)-(42,42).
Reference: No useful local Lucide party-hat pair match; equal circular pompoms and simple cone silhouettes.
Reduction: Overlap removed to keep both hats legible; curved hems retained, and short ties attach the pompoms.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b88b6396-c9c7-52cb-81e7-a50d04a9d8f0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/party hats_b88b6396-c9c7-52cb-81e7-a50d04a9d8f0.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'overlapping-pompom-party-hats'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    aliases = ()
    keywords = ('two', 'party', 'hats')

    def build(self):
        for i,(x,y,apex) in enumerate(((13,9,20),(35,15,26))):
            self.add_arc(f'pom-{i}-a',(x,y-3),(x,y+3),radius_x=3)
            self.add_arc(f'pom-{i}-b',(x,y+3),(x,y-3),radius_x=3)
            self.add_contour(f'pom-{i}',f'pom-{i}-a',f'pom-{i}-b',closed=True)
            self.add_line(f'tie-{i}',(x,y+3),(x,apex))
            self.add_polyline(f'cone-{i}',(x-7,40),(x,apex),(x+7,40))
            self.add_arc(f'hem-{i}',(x+7,40),(x-7,40),radius_x=7,radius_y=2)
            self.relate('connect',f'cone-{i}',f'hem-{i}')
            self.relate('connect',f'tie-{i}',f'pom-{i}')
            self.relate('connect',f'tie-{i}',f'cone-{i}')
