'Seated squirrel facing right with upright bushy tail, rounded ear, muzzle and forepaw. SQUARE retains full silhouette. One outer contour owns tail and body, with a single open haunch curve. Lucide squirrel informs smooth connected silhouette rather than detached animal parts; reference supplies right-facing pose. Eye and fine fur omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a51deaea-200e-4079-8de8-824f2bcd9803'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/chipmunk_a51deaea-200e-4079-8de8-824f2bcd9803.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'squirrel-with-upright-bushy-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Squirrel with Upright Bushy Tail',)
    keywords = ('squirrel', 'rodent', 'tail', 'seated', 'animal', 'wildlife', 'mammal')
    def build(self):
        self.add_bezier('tail-back',(18,42),((6,42),(6,34),(6,24)))
        self.add_line('tail-rise',(6,24),(6,18))
        self.add_arc('tail-cap',(6,18),(18,18),radius_x=6,sweep=True)
        self.add_line('tail-inner',(18,18),(18,28))
        self.add_bezier('back',(18,28),((18,22),(26,22),(26,14)))
        self.add_line('ear-rise',(26,14),(26,10))
        self.add_arc('ear',(26,10),(34,10),radius_x=4,sweep=True)
        self.add_bezier('head',(34,10),((38,10),(42,14),(42,18)),((42,20),(38,20),(34,20)))
        self.add_line('neck',(34,20),(34,29))
        self.add_line('paw-top',(34,29),(38,29))
        self.add_arc('paw',(38,29),(38,37),radius_x=4,sweep=True)
        self.add_line('paw-bottom',(38,37),(34,37))
        self.add_line('belly',(34,37),(34,42))
        self.add_line('base',(34,42),(18,42))
        self.add_contour('silhouette','tail-back','tail-rise','tail-cap','tail-inner','back','ear-rise','ear','head','neck','paw-top','paw','paw-bottom','belly','base',closed=True)
