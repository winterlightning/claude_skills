# Variant of lidded-ceremonial-urn; parent file remains unchanged.
'Simplified lidded urn with smooth mirrored bowl, stem and foot. VRECT_M fits the handle-free vessel. Lucide amphora informs the mirrored vessel construction; handles and stepped foot omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '013843b0-cb2a-568a-8813-88833200bb81'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/urn_013843b0-cb2a-568a-8813-88833200bb81.svg'
AUTHOR = 'gpt-6'

class LiddedCeremonialUrnVariant2(Solo48):
    icon_id = 'lidded-ceremonial-urn-v2'
    variant_of = 'lidded-ceremonial-urn'
    variant_label = 'Simplified lidded silhouette'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('urn', 'vessel', 'pottery', 'funerary', 'ceramic', 'antique', 'museum', 'ashes')

    def build(self) -> None:
        # VRECT_M extremes (11,2)-(37,46); matching circular shoulders.
        self.add_line('lid',(15,2),(33,2))
        self.add_line('neck-left',(18,2),(18,10))
        self.add_arc('shoulder-left',(18,10),(11,17),radius_x=7,sweep=False)
        self.add_arc('bowl-left',(11,17),(24,38),radius_x=13,radius_y=21,sweep=False)
        self.add_arc('bowl-right',(24,38),(37,17),radius_x=13,radius_y=21,sweep=False)
        self.add_arc('shoulder-right',(37,17),(30,10),radius_x=7,sweep=False)
        self.add_line('neck-right',(30,10),(30,2))
        self.add_contour('vessel','neck-left','shoulder-left','bowl-left','bowl-right','shoulder-right','neck-right')
        self.relate('connect','vessel','lid')
        self.add_line('stem',(24,38),(24,46))
        self.add_polyline('foot',(14,46),(24,46),(34,46))
        self.relate('connect','stem','vessel')
        self.relate('connect','stem','foot')
