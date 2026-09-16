"""Tree-Like Architectural Columns.

Symbol plan: Two branching architectural supports with unequal heights. Reduce thin double trunk outlines to single structural strokes.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '52498168-5dc9-57cf-a9b6-bfb0fd36773b'
SOURCE_PATH = 'pictographic-primitives/building/modern architecture_52498168-5dc9-57cf-a9b6-bfb0fd36773b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tree-like-architectural-columns'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building', 'architecture', 'structure', 'roof', 'property', 'exterior', 'construction', 'urban')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        path('large-crown',(4,8),(16,20),(28,8))
        line('large-trunk',(16,20),(16,40));connect('large-crown','large-trunk')
        path('small-crown',(28,24),(36,32),(44,24))
        line('small-trunk',(36,32),(36,40));connect('small-crown','small-trunk')
