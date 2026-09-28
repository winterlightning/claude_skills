'Broad scraper blade narrows into a short rounded handle. Preserve full scraping edge and blade-to-handle transition.\nPlan: reference-backed typed contours; repeated shapes share parameters. Keyshape VRECT_L uses exact SOLO48 contract bounds. No useful exact Lucide reference unless noted.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '7f4d1570-9de8-4a19-90c3-57287c2ac40b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__putty-knife-with-broad-blade/20260927T170540Z-thuan-mac-1/reference/putty knife_7f4d1570-9de8-4a19-90c3-57287c2ac40b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'putty-knife-with-broad-blade'
    keyshape = Keyshape.VRECT_L
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    def build(self):
        # One broad straight blade narrows into a rounded grip.
        self.add_line('top',(8,4),(40,4))
        self.add_line('blade-right',(40,4),(34,22))
        self.add_line('shoulder-right',(34,22),(30,28))
        self.add_line('handle-right',(30,28),(30,38))
        self.add_arc('handle-end',(30,38),(18,38),radius_x=6,sweep=True)
        self.add_line('handle-left',(18,38),(18,28))
        self.add_line('shoulder-left',(18,28),(14,22))
        self.add_line('blade-left',(14,22),(8,4))
        self.add_contour('knife','top','blade-right','shoulder-right','handle-right','handle-end','handle-left','shoulder-left','blade-left',closed=True)
        self.add_line('neck',(18,28),(30,28))
        self.relate('connect','neck','knife')
