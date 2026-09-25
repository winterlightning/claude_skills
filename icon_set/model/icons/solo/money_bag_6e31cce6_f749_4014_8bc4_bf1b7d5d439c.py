"""A dollar-marked sack with a flared top. VRECT_L extremes (8,4)-(40,44). No useful exact Lucide sack match; coherent circular shoulders and rounded base retain the source silhouette. Open the neck crossbar and use short dollar terminal strokes instead of a full crossing stem to avoid undersized holes. Retain the money-bag identity and flared rim."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e31cce6-f749-4014-8bc4-bf1b7d5d439c'
SOURCE_PATH = 'pictographic-primitives/symbol/money bag_6e31cce6-f749-4014-8bc4-bf1b7d5d439c.svg'
AUTHOR = 'gpt-6'


class MoneyBag(Solo48):
    icon_id = 'money-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('money-bag', 'money', 'dollar', 'savings', 'wealth', 'cash', 'finance', 'bank')

    def build(self) -> None:
        self.add_arc('left-shoulder',(16,8),(8,24),radius_x=20,sweep=False)
        self.add_line('left',(8,24),(8,34))
        self.add_arc('bl',(8,34),(18,44),radius_x=10,sweep=False)
        self.add_line('base',(18,44),(30,44))
        self.add_arc('br',(30,44),(40,34),radius_x=10,sweep=False)
        self.add_line('right',(40,34),(40,24))
        self.add_arc('right-shoulder',(40,24),(32,8),radius_x=20,sweep=False)
        self.add_contour('sack','left-shoulder','left','bl','base','br','right','right-shoulder')
        self.add_polyline('top',(16,8),(12,4),(36,4),(32,8))
        self.relate('connect','sack','top')
        self.add_line('s-top-right',(26,18),(24,18))
        self.add_line('s-top-left',(24,18),(22,18))
        self.add_arc('s-upper',(22,18),(22,26),radius_x=4,sweep=False)
        self.add_line('s-middle',(22,26),(26,26))
        self.add_arc('s-lower',(26,26),(26,34),radius_x=4)
        self.add_line('s-bottom-right',(26,34),(24,34))
        self.add_line('s-bottom-left',(24,34),(22,34))
        self.add_contour('s','s-top-right','s-top-left','s-upper','s-middle','s-lower','s-bottom-right','s-bottom-left')
        self.add_line('dollar-top',(24,17),(24,18))
        self.add_line('dollar-bottom',(24,34),(24,35))
        self.relate('connect','s','dollar-top')
        self.relate('connect','s','dollar-bottom')
