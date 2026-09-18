"""Left-facing dog muzzle, pointed ear and open neck; asymmetric profile silhouette.
Keyshape ink bounds: (6, 2, 42, 46).
Construction reference: Lucide dog; source render establishes subject.
Reduction: No eye or nostril, matching sparse reference.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a085944f-53b4-4a2c-a24d-d67fff30f609'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/dog head 1_a085944f-53b4-4a2c-a24d-d67fff30f609.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-025/references/dog head 1_a085944f-53b4-4a2c-a24d-d67fff30f609.svg'
AUTHOR = 'gpt-6'

class Batch025Icon(Solo48):
    icon_id = 'dog-head-profile-solo-batch-025-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ()
    keywords = ('dog', 'head', 'profile', 'solo')

    def build(self):
        self.add_polyline('ear-back',(22,16),(28,4),(40,44))
        self.add_bezier('muzzle-top',(22,16),((18,18),(8,16),(8,26)))
        self.add_bezier('muzzle-bottom',(8,26),((8,34),(15,34),(22,34)))
        self.add_line('neck',(22,34),(24,44))
        self.relate('connect','ear-back','muzzle-top')
        self.add_contour('muzzle','muzzle-top','muzzle-bottom','neck')
