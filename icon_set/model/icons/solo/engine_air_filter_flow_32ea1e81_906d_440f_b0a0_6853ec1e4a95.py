"""Engine Air Filter Flow, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '32ea1e81-906d-440f-b0a0-6853ec1e4a95'
SOURCE_PATH = 'pictographic-primitives/transportation/engine air filter_32ea1e81-906d-440f-b0a0-6853ec1e4a95.svg'
AUTHOR = 'gpt-6'

class EngineAirFilterFlow(Solo48):
    icon_id = 'engine-air-filter-flow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('air filter', 'engine', 'filter', 'airflow', 'maintenance', 'car', 'dashboard', 'service')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        # Two shared wave profiles between the cartridge caps.
        for i,x in enumerate((18,30)):
            self.add_arc(f'pleat-{i}-a',(x,8),(x-2,16),radius_x=2,radius_y=8)
            self.add_arc(f'pleat-{i}-b',(x-2,16),(x,24),radius_x=2,radius_y=8,sweep=False)
            self.add_arc(f'pleat-{i}-c',(x,24),(x+2,32),radius_x=2,radius_y=8,sweep=False)
            self.add_arc(f'pleat-{i}-d',(x+2,32),(x,40),radius_x=2,radius_y=8)
            self.add_contour(f'pleat-{i}',*[f'pleat-{i}-{s}' for s in 'abcd'])
        for y in (8,40):
            self.add_polyline(f'cap-{y}',(16,y),(18,y),(30,y),(32,y))
            for i in range(2): self.relate('connect',f'cap-{y}',f'pleat-{i}')
        for i in range(3):
            y=14+i*10
            self.add_line(f'inlet-{i}',(4,y),(6,y))
        self.add_line('outlet',(40,24),(44,24))
        self.add_polyline('outlet-head',(40,20),(44,24),(40,28))
        self.relate('connect','outlet','outlet-head')
