"""A folded document page with three legible lines of text.

The open inner fold avoids a tiny closed triangle at native size while the
shorter last line follows the source page's descending text rhythm.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6dbe125c-f5f3-4d74-b6f7-e95b9d655a71'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__google-docs-logo/20260927T055616Z-thuan-mac-1/reference/google docs logo_6dbe125c-f5f3-4d74-b6f7-e95b9d655a71.svg'
AUTHOR = "gpt-6"


class GoogleDocsLogo(Solo48):
    icon_id = 'google-docs-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-docs', 'google', 'document', 'text', 'logo', 'brand', 'office')

    def build(self):
        self.add_line('top',(12,4),(32,4))
        self.add_line('fold-slope',(32,4),(40,12))
        self.add_line('right',(40,12),(40,40))
        self.add_arc('br',(40,40),(36,44),radius_x=4)
        self.add_line('bottom',(36,44),(12,44))
        self.add_arc('bl',(12,44),(8,40),radius_x=4)
        self.add_line('left',(8,40),(8,8))
        self.add_arc('tl',(8,8),(12,4),radius_x=4)
        self.add_contour('page','top','fold-slope','right','br','bottom','bl','left','tl',closed=True)
        self.add_line('fold',(32,4),(32,12))
        self.relate('connect','page','fold')
        # Three native-size text rows retain more of the source document.
        for i,(y,end) in enumerate(((19,26),(27,30),(35,24))):
            self.add_line(f'text-{i}',(17,y),(end,y))
