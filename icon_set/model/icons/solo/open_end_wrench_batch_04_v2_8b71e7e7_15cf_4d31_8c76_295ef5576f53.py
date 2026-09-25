"""Independent full icon-solo drawing from the original batch-04 brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b71e7e7-15cf-4d31-8c76-295ef5576f53'
SOURCE_PATH = 'pictographic-primitives/other/flash wrench_8b71e7e7-15cf-4d31-8c76-295ef5576f53.svg'
AUTHOR = 'gpt-6'


class IndependentSolo(Solo48):
    icon_id = 'open-end-wrench-batch-04-v2'
    variant_of = 'open-end-wrench-batch-04'
    variant_label = 'Independent icon-solo; original reference only'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('open', 'end', 'wrench', 'batch', '04')

    def build(self):
        # Plan: single closed wrench silhouette on a rising diagonal; no modifier.
        # SQUARE centerline extremes (6,6)-(42,42). Lucide wrench: open jaw + round heel.
        self.add_bezier('head-left',(20,22),((17,12),(23,6),(30,6)))
        for i,(a,b) in enumerate(zip([(30,6),(24,14),(32,22)],[(24,14),(32,22),(42,12)]),1):
            self.add_line(f'jaw-{i}',a,b)
        self.add_bezier('head-right',(42,12),((42,21),(39,28),(28,28)))
        self.add_line('handle-right',(28,28),(14,41))
        self.add_arc('heel',(14,41),(8,33),radius_x=5)
        self.add_line('handle-left',(8,33),(20,22))
        self.add_contour('wrench','head-left',*[f'jaw-{i}' for i in range(1,4)],'head-right','handle-right','heel','handle-left',closed=True)
