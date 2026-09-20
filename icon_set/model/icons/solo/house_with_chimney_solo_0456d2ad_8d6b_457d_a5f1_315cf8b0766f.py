"""House with chimney.

Construction reference: house.
Deliberately asymmetric chimney; empty house interior.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '0456d2ad-8d6b-457d-a5f1-315cf8b0766f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/empty house_0456d2ad-8d6b-457d-a5f1-315cf8b0766f.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'house-with-chimney-solo-0456d2ad'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('house-with-chimney',)
    keywords = ('house', 'with', 'chimney')

    def build(self):
        # Roof keeps its overhang and an upright right chimney.
        self.add_polyline('roof',(6,24),(10,20),(24,6),(34,16),(42,24))
        path(self,'walls',(10,20),[('L',(10,38)),('A',(14,42),4,4,False),('L',(34,42)),('A',(38,38),4,4,False),('L',(38,20))])
        self.add_line('chimney',(34,16),(34,6))
        self.relate('connect','roof','walls')
        self.relate('connect','roof','chimney')
