"""Donkey Shaped Piñata.
Plan: Right-facing donkey outline with broad separated legs; band attaches to side walls. Centerline extremes (6,6)-(42,42).
Reference: Lucide dog inspected; no useful full-body match. Retained source donkey profile with geometric legs.
Reduction: Second overlapping ear and tail reduced; band retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0d1f866-a25b-58b5-b0e5-584d69347eff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/pinata_e0d1f866-a25b-58b5-b0e5-584d69347eff.svg'
AUTHOR = 'gpt-6'


class Batch25Icon(Solo48):
    icon_id = 'donkey-pinata-banded-body'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "events"
    aliases = ()
    keywords = ('donkey', 'shaped', 'piñata')

    def build(self):
        self.add_polyline('outline',(6,26),(6,18),(24,18),(28,6),(34,14),(42,18),(42,26),(34,26),(34,34),(34,42),(26,42),(24,34),(16,34),(14,42),(6,42),closed=True)
        self.add_line('band',(6,26),(34,26))
        self.relate('connect','band','outline')
