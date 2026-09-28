"""Threaded sewing needle with smooth eye and a flowing loose thread.
Plan: Threaded sewing needle with smooth eye and a flowing loose thread.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: Fine filament tail extension omitted; eye, taper and trailing thread retained."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '132f47bc-4c0e-4882-9b9d-93439d0723ca'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__threaded-sewing-needle/20260927T140026Z-thuan-mac-1/reference/needle_132f47bc-4c0e-4882-9b9d-93439d0723ca.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='threaded-sewing-needle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives-generate', 'other')
    aliases=()
    keywords=('threaded', 'sewing', 'needle')

    def build(self):
        # Long steel shaft joins a small eye; a loose thread exits to the right.
        self.add_arc('eye-upper',(30,11),(40,11),radius_x=5)
        self.add_arc('eye-lower',(40,11),(30,11),radius_x=5)
        self.add_contour('eye','eye-upper','eye-lower',closed=True)
        self.add_line('shaft',(6,42),(30,11))
        self.relate('connect','shaft','eye')
        self.add_bezier('thread-upper',(40,11),((42,18),(42,25),(37,29)))
        self.add_bezier('thread-tail',(37,29),((32,33),(30,38),(34,42)))
        self.add_contour('thread','thread-upper','thread-tail')
        self.relate('connect','eye','thread')
