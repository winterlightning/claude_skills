"""Jigsaw piece two sockets.

Construction reference: puzzle.
Tab and sockets are opposing circular sweeps; right edge stays plain.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '5ed610a0-561c-4394-96d1-35f43a6a1e6b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/puzzle_5ed610a0-561c-4394-96d1-35f43a6a1e6b.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'jigsaw-piece-two-sockets-solo-5ed610a0'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ('jigsaw-piece-two-sockets',)
    keywords = ('jigsaw', 'piece', 'two', 'sockets')

    def build(self):
        # One top tab, left and bottom sockets; coherent silhouette without detached loops.
        path(self,'piece',(12,14),[('L',(19,14)),('L',(19,9)),('A',(29,9),5,5,True),('L',(29,14)),('L',(36,14)),('A',(40,18),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(28,44)),('A',(20,44),5,5,False,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,32)),('A',(8,24),5,5,False,True),('L',(8,18)),('A',(12,14),4,4,True)],True)
