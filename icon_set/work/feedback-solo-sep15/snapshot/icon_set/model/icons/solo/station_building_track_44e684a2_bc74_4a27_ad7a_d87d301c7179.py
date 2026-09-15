"""station-building-track: reconstructed on SOLO48 from its reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44e684a2-bc74-4a27-ad7a-d87d301c7179'
SOURCE_PATH = 'pictographic-primitives/transportation/ticket office 1_44e684a2-bc74-4a27-ad7a-d87d301c7179.svg'
AUTHOR = 'gpt-6'


class StationBuildingTrack(Solo48):
    icon_id = 'station-building-track'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('ticket office', 'station', 'railway station', 'building', 'track', 'depot', 'terminal', 'train')

    def build(self) -> None:

        # Gable and low wings share one facade; arched doorway and sparse sleepers remain.
        self.add_polyline('facade',(6,30),(6,18),(14,18),(24,6),(34,18),(42,18),(42,30),(30,30),(18,30),(6,30))
        self.add_line('door-left',(18,30),(18,24))
        self.add_arc('door-arch',(18,24),(30,24),radius_x=6)
        self.add_line('door-right',(30,24),(30,30))
        self.add_contour('door','door-left','door-arch','door-right')
        self.add_polyline('rail',(6,40),(12,40),(24,40),(36,40),(42,40))
        for i,x in enumerate([12,24,36]): self.add_polyline(f'sleeper-{i}',(x,38),(x,40),(x,42))
        # Declare only real junctions with exactly matching endpoints.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
