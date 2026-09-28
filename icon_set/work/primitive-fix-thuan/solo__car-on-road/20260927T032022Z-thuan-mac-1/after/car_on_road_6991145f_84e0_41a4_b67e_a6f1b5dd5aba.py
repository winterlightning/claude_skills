"""car-on-road: reconstructed on SOLO48 from the supplied transportation reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6991145f-84e0-41a4-b67e-a6f1b5dd5aba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-on-road/20260927T032022Z-thuan-mac-1/reference/traveling on road_6991145f-84e0-41a4-b67e-a6f1b5dd5aba.svg'
AUTHOR = 'gpt-6'


class CarOnRoad(Solo48):
    icon_id = 'car-on-road'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('car', 'road', 'driving', 'travel', 'road trip', 'highway', 'journey', 'vehicle')

    def build(self) -> None:

        # Broad windscreen and two visible tyres make the front-facing car clear.
        self.add_polyline('windscreen',(11,16),(16,6),(32,6),(37,16))
        self.add_polyline('body',(6,16),(42,16),(42,24),(6,24),closed=True)
        for i,x in enumerate((13,35)):
            self.add_line(f'tyre-{i}',(x,24),(x,30))
        # The receding road is kept separate from the vehicle silhouette.
        self.add_line('road-left',(10,38),(6,42))
        self.add_line('road-right',(38,38),(42,42))
        self.add_dot('centre-lane',(24,42))
        # Record only actual shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
