"""Lidded urn with broad handles and spreading foot. Extremes (5,2)-(43,46). Lucide amphora mirrored vessel and handles; collar and shoulder seam merged."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '013843b0-cb2a-568a-8813-88833200bb81'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/urn_013843b0-cb2a-568a-8813-88833200bb81.svg'

class LiddedCeremonialUrn(Solo48):
    icon_id = 'lidded-ceremonial-urn'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('urn', 'vessel', 'pottery', 'funerary', 'ceramic', 'antique', 'museum', 'ashes')

    def build(self) -> None:
        self.add_line('lid',(15,2),(33,2))
        self.add_line('neck-1', (18, 2), (18, 10))
        self.add_line('neck-2', (18, 10), (15, 10))
        self.add_arc('shoulder-left',(15,10),(12,19),radius_x=10)
        self.add_arc('bowl-left',(12,19),(20,38),radius_x=25,sweep=False)
        self.add_line('bowl-bottom',(20,38),(28,38))
        self.add_arc('bowl-right',(28,38),(36,19),radius_x=25,sweep=False)
        self.add_arc('shoulder-right',(36,19),(33,10),radius_x=10)
        self.add_line('neck-right-1', (33, 10), (30, 10))
        self.add_line('neck-right-2', (30, 10), (30, 2))
        self.add_contour('vessel','neck-1','neck-2','shoulder-left','bowl-left','bowl-bottom','bowl-right','shoulder-right','neck-right-1','neck-right-2')
        self.relate('connect','lid','vessel')
        self.add_arc('handle-left',(12,19),(12,31),radius_x=7,radius_y=6,sweep=False)
        self.add_arc('handle-right',(36,31),(36,19),radius_x=7,radius_y=6,sweep=False)
        self.relate('connect','vessel','handle-left')
        self.relate('connect','vessel','handle-right')
        self.add_polyline('foot',(20,38),(15,46),(33,46),(28,38))
        self.relate('connect','vessel','foot')
