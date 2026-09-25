'Embassy with dome, right-facing flag and low wings. SQUARE centerlines (6,6)-(42,42). Paired wings, shared dome radius. Arched entrance retained; internal wing divisions and cornices omitted. Lucide landmark informs architectural rhythm.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9753b8d6-83c7-5ff0-8f5f-0f692f64e751'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/embassy building_9753b8d6-83c7-5ff0-8f5f-0f692f64e751.svg'
AUTHOR = 'gpt-6'

class DomedCivicBuildingWithFlag(Solo48):
    icon_id = 'domed-civic-building-with-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('embassy', 'government', 'dome', 'civic', 'flag', 'building', 'official', 'architecture')

    def build(self) -> None:
        axis, left, right, bottom = 24, 6, 42, 42
        self.add_polyline('flag',(axis,14),(34,14),(34,6),(axis,6),(axis,14),(axis,22))
        self.add_arc('dome-left',(14,32),(axis,22),radius_x=10)
        self.add_arc('dome-right',(axis,22),(34,32),radius_x=10)
        self.add_contour('dome','dome-left','dome-right')
        self.add_polyline('body',(14,32),(6,32),(6,42),(20,42),(28,42),(42,42),(42,32),(34,32))
        self.add_line('door-left',(20,42),(20,36))
        self.add_arc('door-arch',(20,36),(28,36),radius_x=4)
        self.add_line('door-right',(28,36),(28,42))
        self.add_contour('door','door-left','door-arch','door-right')
        self.relate('connect','door','body')
        self.relate('connect','dome','body')
        self.relate('connect','flag','dome')
