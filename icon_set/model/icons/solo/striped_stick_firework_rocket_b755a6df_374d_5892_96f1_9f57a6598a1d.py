"""Striped Celebration Firework Rocket.
Plan: Diagonal rocket owns a band across its body and a stick at its base midpoint. Extrema (6,6)-(42,42).
Reference: No useful Lucide stick-rocket match; shared diagonal coordinates keep band attachments exact.
Reduction: Two bands reduced to one to preserve spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b755a6df-374d-5892-96f1-9f57a6598a1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/fireworks rocket_b755a6df-374d-5892-96f1-9f57a6598a1d.svg'
AUTHOR = 'gpt-6'


class Batch26Icon(Solo48):
    icon_id = 'striped-stick-firework-rocket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/celebrations"
    aliases = ()
    keywords = ('striped', 'celebration', 'firework', 'rocket')

    def build(self):

        self.add_polyline('body',(14,26),(20,20),(26,14),(34,22),(28,28),(22,34),(18,30),closed=True)
        self.add_line('stripe',(20,20),(28,28))
        self.relate('connect','stripe','body')
        self.add_line('stick',(18,30),(6,42));self.relate('connect','body','stick')
        self.add_polyline('cap',(30,6),(42,6),(42,18))
