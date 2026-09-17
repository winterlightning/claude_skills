"""Braided Yarn Skein.

Plan: Three rounded braided bundles reoriented horizontally. Shared shallow end scallops and two sweeping strand seams. Bounds (4,10)-(44,38); reduce fine thread lines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ab9f3b5-03e7-4655-9d6a-e84a5583b790'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hobbies/yarn_5ab9f3b5-03e7-4655-9d6a-e84a5583b790.svg'
AUTHOR = 'gpt-6'


class BraidedYarnSkein(Solo48):
    icon_id = 'braided-yarn-skein'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hobbies'
    aliases = ()
    keywords = ('braided', 'yarn', 'skein')

    def build(self):
        self.add_arc('top-left',(12,10),(24,10),radius_x=6,radius_y=3,sweep=False)
        self.add_arc('top-right',(24,10),(36,10),radius_x=6,radius_y=3,sweep=False)
        self.add_arc('end-right',(36,10),(36,38),radius_x=8,radius_y=14)
        self.add_arc('bottom-right',(36,38),(24,38),radius_x=6,radius_y=3,sweep=False)
        self.add_arc('bottom-left',(24,38),(12,38),radius_x=6,radius_y=3,sweep=False)
        self.add_arc('end-left',(12,38),(12,10),radius_x=8,radius_y=14)
        self.add_contour('skein','top-left','top-right','end-right','bottom-right','bottom-left','end-left',closed=True)
        for i in range(2):
            x=24+12*i
            self.add_arc(f'strand-{i}',(x,10),(x-12,38),radius_x=12,radius_y=28)
            self.relate('connect','skein',f'strand-{i}')
