"""Tree-Like Architectural Columns.

Symbol plan: Two branching architectural supports with unequal heights. Reduce thin double trunk outlines to single structural strokes.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: No useful exact Lucide subject match; reconstruct the supplied silhouette with coherent lines and arcs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '52498168-5dc9-57cf-a9b6-bfb0fd36773b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tree-like-architectural-columns/20260927T101610Z-thuan-mac-1/reference/modern architecture_52498168-5dc9-57cf-a9b6-bfb0fd36773b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tree-like-architectural-columns'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('building', 'architecture', 'structure', 'roof', 'property', 'exterior', 'construction', 'urban')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        self.add_bezier('large-left',(4,8),((8,12),(16,16),(16,20)))
        self.add_bezier('large-right',(16,20),((16,16),(22,12),(28,8)))
        self.add_contour('large-crown','large-left','large-right')
        self.add_bezier('large-trunk',(16,20),((16,28),(15,35),(14,40)))
        connect('large-crown','large-trunk')
        self.add_bezier('small-left',(28,24),((32,26),(36,29),(36,32)))
        self.add_bezier('small-right',(36,32),((36,29),(40,26),(44,24)))
        self.add_contour('small-crown','small-left','small-right')
        line('small-trunk',(36,32),(36,40));connect('small-crown','small-trunk')
