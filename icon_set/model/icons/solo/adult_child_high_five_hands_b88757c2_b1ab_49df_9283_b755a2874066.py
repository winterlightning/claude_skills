"""Adult and Child High Five.
Plan: A larger left hand and smaller right hand meet at (26,26). Fingers are grouped into broad rounded lobes. Extrema (6,6)-(42,42).
Reference: human_ref/full_body_ref.png for reduction; Lucide hand: rounded finger lobes and an opposing thumb.
Reduction: Individual finger grooves grouped into broad finger pads; the overlapping palms are opened into a clear joined high-five silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b88757c2-b1ab-49df-9283-b755a2874066'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/family/play together_b88757c2-b1ab-49df-9283-b755a2874066.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'adult-child-high-five-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "family"
    categories = ("primitives", "family")
    aliases = ()
    keywords = ('adult', 'and', 'child', 'high', 'five')

    def build(self):
        self.add_polyline('adult-outer',(6,42),(10,38),(10,10))
        self.add_arc('adult-fingers',(10,10),(18,10),radius_x=4)
        self.add_polyline('adult-inner',(18,10),(18,22),(22,18),(26,22),(26,26),(18,38),(14,42))
        self.relate('connect','adult-outer','adult-fingers')
        self.relate('connect','adult-fingers','adult-inner')
        self.add_polyline('child-outer',(38,42),(42,34),(42,22))
        self.add_arc('child-fingers',(42,22),(34,22),radius_x=4,sweep=False)
        self.add_polyline('child-inner',(34,22),(34,30),(26,26),(26,34),(30,42))
        self.relate('connect','child-outer','child-fingers')
        self.relate('connect','child-fingers','child-inner')
        self.relate('connect','adult-inner','child-inner')
