"""Festive Donkey Pinata.
Plan: Left-facing suspended donkey; body and two broad legs share one silhouette, cord attaches to back. Centerline extremes (6,6)-(42,42).
Reference: Lucide dog inspected; no useful full-body match. Source establishes left-facing silhouette and cord.
Reduction: Tail omitted to preserve leg and cord clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0943b52-9890-59dd-ab15-b88694bb732e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/pinata_b0943b52-9890-59dd-ab15-b88694bb732e.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'suspended-donkey-pinata'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    categories = ("primitives", "events")
    aliases = ()
    keywords = ('festive', 'donkey', 'pinata')

    def build(self):

        self.add_polyline('outline',(6,18),(16,12),(18,6),(22,16),(22,24),(30,24),(38,24),(42,42),(32,42),(28,32),(20,32),(16,42),(6,42),(12,26),(6,26),closed=True)
        self.add_line('suspension',(30,24),(30,6))
        self.relate('connect','suspension','outline')
