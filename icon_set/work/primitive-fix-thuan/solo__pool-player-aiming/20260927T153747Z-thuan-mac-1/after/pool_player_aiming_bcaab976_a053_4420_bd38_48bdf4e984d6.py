"""Pool player aiming, authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bcaab976-a053-4420-bd38-48bdf4e984d6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pool-player-aiming/20260927T153747Z-thuan-mac-1/reference/pool player_bcaab976-a053-4420-bd38-48bdf4e984d6.svg'
AUTHOR = 'gpt-6'

class PoolPlayerAiming(Solo48):
    icon_id='pool-player-aiming'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('pool', 'player', 'aiming')
    def build(self):
        # A bent player steadies a cue across the picture plane.
        self.add_arc('head-top', (26, 10), (34, 10), radius_x=4)
        self.add_arc('head-bottom', (34, 10), (26, 10), radius_x=4)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('torso', (30, 22), (18, 22), (18, 30))
        self.add_line('arm', (30, 22), (38, 30))
        self.add_polyline('cue', (6, 30), (18, 30), (38, 30), (42, 30))
        self.add_line('leg-left', (18, 30), (12, 42))
        self.add_line('leg-right', (18, 30), (28, 42))
        for a,b in (('torso','arm'),('torso','cue'),('arm','cue'),('torso','leg-left'),('torso','leg-right')):
            self.relate('connect',a,b)
        self.mark_human_figure('player',head='head',torso='torso-1',torso_junction='start')
