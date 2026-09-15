"""An upright document with a folded top right corner holds four horizontal text lines, the lower two shorter.

Plan: Folded page owns its fold endpoints; two text lines share left alignment and 9-unit row spacing.
Keyshape: VRECT_L; exact SOLO48 envelope from the contract.
Construction reference: file-text: rounded page and shared fold junctions.
Simplification: Four text lines reduce to two.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6dbe125c-f5f3-4d74-b6f7-e95b9d655a71'
SOURCE_PATH = 'pictographic-primitives/logos/google docs logo_6dbe125c-f5f3-4d74-b6f7-e95b9d655a71.svg'
AUTHOR = 'gpt-6'


class GoogleDocsLogo(Solo48):
    icon_id = 'google-docs-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-docs', 'google', 'document', 'text', 'logo', 'brand', 'office')

    def build(self):
        self.add_line('top',(12,4),(28,4))
        self.add_line('fold-slope',(28,4),(40,16))
        self.add_line('right',(40,16),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,8))
        self.add_arc('tl',(8,8),(12,4),radius_x=4)
        self.add_contour('page','top','fold-slope','right','br','bottom','bl','left','tl',closed=True)
        self.add_polyline('fold',(28,4),(28,16),(40,16))
        self.relate('connect','page','fold')
        for i,(y,end) in enumerate(((26,31),(35,26))):
            self.add_line(f'text-{i}',(17,y),(end,y))
