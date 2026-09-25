'A jumping volleyball player raises an arm beside the ball.\nConstruction: Square centerlines (6,6)-(42,42). Bent striking arm, lifted knee and trailing leg retain asymmetric motion; remove clothing and ball seams.\nLucide: accessibility: circular head and coherent bent limb runs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b0142e1-c8b6-427c-bbfc-3a6724c647d8'
SOURCE_PATH = 'pictographic-primitives/sports/volleyball smash_6b0142e1-c8b6-427c-bbfc-3a6724c647d8.svg'
AUTHOR = 'gpt-6'

class VolleyballSpikingPlayer(Solo48):
    icon_id = 'volleyball-spiking-player'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('volleyball', 'spiking', 'player', 'sport')

    def build(self):
        self.add_arc('ball-top', (6, 10), (14, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('ball-bottom', (14, 10), (6, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('ball', 'ball-top', 'ball-bottom', closed=True)
        self.add_arc('head-top', (24, 11), (30, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (30, 11), (24, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('arms', (16, 25), (27, 23), (40, 18), (40, 6), closed=False)
        self.add_polyline('body', (27, 23), (27, 32), (31, 42), closed=False)
        self.relate("connect", 'arms', 'body')
        self.add_polyline('knee', (27, 32), (42, 34), (38, 24), closed=False)
        self.relate("connect", 'knee', 'body')
