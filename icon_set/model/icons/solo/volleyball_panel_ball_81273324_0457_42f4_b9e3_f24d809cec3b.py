'A volleyball with curved panel seams.\nConstruction: Radial centerline radius20 about (24,24). Reduce paired panel lines to three curved seams.\nLucide: volleyball: sweeping seams meet at a central three-way junction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81273324-0457-42f4-b9e3-f24d809cec3b'
SOURCE_PATH = 'pictographic-primitives/sports/volleyball ball_81273324-0457-42f4-b9e3-f24d809cec3b.svg'
AUTHOR = 'gpt-6'

class VolleyballPanelBall(Solo48):
    icon_id = 'volleyball-panel-ball'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('volleyball', 'panel', 'ball', 'sport')

    def build(self):
        self.add_arc('ball-a', (24, 6), (42, 24), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('ball-b', (42, 24), (12, 40), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('ball-c', (12, 40), (24, 6), radius_x=20, radius_y=20, sweep=True)
        self.add_contour('ball', 'ball-a', 'ball-b', 'ball-c', closed=True)
        self.add_arc('seam-top', (24, 6), (24, 24), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('seam-right', (24, 24), (42, 24), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('seam-bottom', (24, 24), (12, 40), radius_x=20, radius_y=20, sweep=False)
        self.relate("connect", 'ball', 'seam-top')
        self.relate("connect", 'ball', 'seam-right')
        self.relate("connect", 'ball', 'seam-bottom')
        self.relate("connect", 'seam-top', 'seam-right')
        self.relate("connect", 'seam-top', 'seam-bottom')
        self.relate("connect", 'seam-right', 'seam-bottom')
