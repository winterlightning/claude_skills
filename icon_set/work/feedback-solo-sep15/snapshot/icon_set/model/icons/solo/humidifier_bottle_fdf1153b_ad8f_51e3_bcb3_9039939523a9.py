"""Round humidifier with collar, water line, and curled mist. Portrait envelope; no exact Lucide match; mirrored vessel with an asymmetric vapor curl."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fdf1153b-ad8f-51e3-bcb3-9039939523a9'
SOURCE_PATH = 'pictographic-primitives/technology/humidifier_fdf1153b-ad8f-51e3-bcb3-9039939523a9.svg'
AUTHOR = 'gpt-6'

class HumidifierBottle(Solo48):
    icon_id = 'humidifier-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('humidifier', 'mist', 'water', 'vessel', 'air', 'appliance', 'moisture')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_line('neck-1',(18, 17),(30, 17))
        self.add_line('neck-2',(30, 17),(32, 23))
        self.add_arc('shoulder-right',(32, 23),(40, 34),radius_x=14,radius_y=14,large_arc=False,sweep=True)
        self.add_bezier('lower-right',(40, 34),*(((39.03526374, 39.91404021), (34.82760764, 44), (30, 44)),))
        self.add_line('bottom',(30, 44),(18, 44))
        self.add_bezier('lower-left',(18, 44),*(((13.17239236, 44), (8.96473626, 39.91404021), (8, 34)),))
        self.add_arc('shoulder-left',(8, 34),(16, 23),radius_x=14,radius_y=14,large_arc=False,sweep=True)
        self.add_line('neck-left',(16, 23),(18, 17))
        self.add_arc('water-left',(8, 34),(24, 34),radius_x=18,radius_y=18,large_arc=False,sweep=True)
        self.add_bezier('water-right',(24, 34),*(((29.04021316, 37.12580751), (34.95978684, 37.12580751), (40, 34)),))
        self.add_bezier('mist',(24, 4),*(((22.3837142, 4), (20.80131331, 4.72578466), (20, 6)),))
        self.add_contour('vessel',*('neck-1', 'neck-2', 'shoulder-right', 'lower-right', 'bottom', 'lower-left', 'shoulder-left', 'neck-left'),closed=True)
        self.add_contour('water',*('water-left', 'water-right'),closed=False)
        self.relate('connect',*('water', 'vessel'))
