"""car-on-road: reconstructed on SOLO48 from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6991145f-84e0-41a4-b67e-a6f1b5dd5aba'
SOURCE_PATH = 'pictographic-primitives/transportation/traveling on road_6991145f-84e0-41a4-b67e-a6f1b5dd5aba.svg'
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

        # Shared front-view cabin and body; motion context is detached below.
        self.add_polyline('cabin',(12,14),(16,6),(32,6),(36,14))
        self.add_polyline('body',(6,14),(12,14),(36,14),(42,14),(42,24),(34,24),(14,24),(6,24),closed=True)

        self.add_line('road-left',(12,34),(6,42))
        self.add_line('road-right',(36,34),(42,42))
        self.add_dot('lane-mark-upper',(24,34))
        self.add_dot('lane-mark-lower',(24,42))
        for i,x in enumerate([14,34]): self.add_line(f'tyre-{i}',(x,24),(x,26))
        # Record only actual shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
