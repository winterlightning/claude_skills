"""Handheld Water Spray Nozzle.
Plan: Flared nozzle above pistol grip; three spray strokes at right. Extrema (6,6)-(42,42).
Reference: Supplied source; no useful exact Lucide match. Coherent curves and shared attachment points.
Reduction: Narrow trigger and connector reduced into the grip silhouette; three water strokes retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3d030d9-b45f-44f5-93c9-5ba1902c725f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/hand sprinkler_a3d030d9-b45f-44f5-93c9-5ba1902c725f.svg'
AUTHOR = 'gpt-6'

class Batch28Icon(Solo48):
    icon_id = 'hose-spray-gun'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('handheld', 'water', 'spray', 'nozzle')

    def build(self):

        self.add_polyline('body',(6,14),(18,14),(28,6),(28,26),(18,22),(18,42),(10,42),(10,22),(6,22),(6,14))
        for i,(a,b) in enumerate((((38,8),(42,6)),((38,16),(42,16)),((38,24),(42,26)))):
            self.add_line(f'spray-{i}',a,b)
