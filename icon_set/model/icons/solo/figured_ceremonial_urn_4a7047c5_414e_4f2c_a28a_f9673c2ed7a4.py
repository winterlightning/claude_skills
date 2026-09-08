"""A handled ceremonial urn bearing a small human figure. SQUARE extremes (2,2)-(46,46). Lucide amphora informs paired handles and a narrow neck; scrolls and foot tiers are omitted."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a7047c5-414e-4f2c-a28a-f9673c2ed7a4'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/chinese urn_4a7047c5-414e-4f2c-a28a-f9673c2ed7a4.svg'


class FiguredCeremonialUrn(Solo48):
    icon_id = 'figured-ceremonial-urn'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('urn', 'vase', 'chinese', 'pottery', 'ceramic', 'antique', 'vessel', 'museum')

    def build(self) -> None:
        self.add_line('neck-1',(16,12),(16,2))
        self.add_line('neck-2',(16,2),(32,2))
        self.add_line('neck-3',(32,2),(32,12))
        self.add_arc('shoulder-right',(32,12),(38,24),radius_x=15)
        self.add_arc('belly-right',(38,24),(30,40),radius_x=20)
        self.add_line('foot-1',(30,40),(34,46))
        self.add_line('foot-2',(34,46),(14,46))
        self.add_line('foot-3',(14,46),(18,40))
        self.add_arc('belly-left',(18,40),(10,24),radius_x=20)
        self.add_arc('shoulder-left',(10,24),(16,12),radius_x=15)
        self.add_contour('urn','neck-1','neck-2','neck-3','shoulder-right','belly-right','foot-1','foot-2','foot-3','belly-left','shoulder-left',closed=True)
        for label,x,outer in (('left',16,2),('right',32,46)):
            self.add_arc(label+'-curl',(x,12),(outer,12),radius_x=7,sweep=label=='right')
            self.add_line(label+'-side',(outer,12),(outer,24))
            self.add_line(label+'-join',(outer,24),(10 if label=='left' else 38,24))
            self.add_contour(label+'-handle',label+'-curl',label+'-side',label+'-join')
            self.relate('connect','urn',label+'-handle')
        self.add_dot('figure-head',(24,21))
        self.add_line('figure-body',(24,27),(24,32))
        self.add_line('figure-arms',(19,28),(29,28))
        self.add_polyline('figure-legs',(21,34),(24,32),(27,34))
        self.relate('connect','figure-body','figure-arms')
        self.relate('connect','figure-body','figure-legs')
