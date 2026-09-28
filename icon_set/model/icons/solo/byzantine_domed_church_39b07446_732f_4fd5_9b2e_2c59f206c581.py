"""SQUARE (6,6)-(42,42) centerlines. Preserve tall central dome, two side domes and three repeated arches. Omit the facade band and side windows so the arches have space. Mirrored about x=24.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39b07446-732f-4fd5-9b2e-2c59f206c581'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/mystras_39b07446-732f-4fd5-9b2e-2c59f206c581.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'byzantine-domed-church'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    categories = ("landmarks", "primitives")
    aliases = ()
    keywords = ('mystras', 'byzantine', 'church', 'dome', 'greece', 'monastery', 'heritage', 'religion')

    def build(self):
        self.add_arc('central-dome',(12,20),(36,20),radius_x=12,radius_y=14)
        self.add_line('left-wall',(6,42),(6,26))
        self.add_arc('left-dome-outer',(6,26),(12,20),radius_x=6)
        self.add_arc('left-dome-inner',(12,20),(18,26),radius_x=6)
        self.add_line('valley',(18,26),(30,26))
        self.add_arc('right-dome-inner',(30,26),(36,20),radius_x=6)
        self.add_arc('right-dome-outer',(36,20),(42,26),radius_x=6)
        self.add_line('right-wall',(42,26),(42,42))
        self.add_contour('facade','left-wall','left-dome-outer','left-dome-inner','valley','right-dome-inner','right-dome-outer','right-wall')
        self.relate('connect','central-dome','facade')
        for i in range(3):
            self.add_arc(f'arch-{i}',(42-i*12,42),(30-i*12,42),radius_x=6,sweep=False)
        self.add_contour('arcade','arch-0','arch-1','arch-2')
        self.relate('connect','facade','arcade')
