"""A lobed royal crown with an orb on a short post and a rounded lower band.

VRECT_L live visible extremes (6,2)-(42,46); centerlines (8,4)-(40,44).
Lucide crown informs the central axis and lower-band hierarchy. The supplied
reference sets the rounded lobes, arched panel and circular orb. Paired curves
share radii and mirrored integer nodes. No gems or extra detail are introduced.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f006ba07-bc53-40a1-9fda-41f04b82bb5a'
SOURCE_PATH = 'pictographic-primitives/rewards/vip crown_f006ba07-bc53-40a1-9fda-41f04b82bb5a.svg'
AUTHOR = 'gpt-6'


class RoyalCrownWithOrb(Solo48):
    icon_id = 'royal-crown-with-orb'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/award'
    aliases = ('orb-crown',)
    keywords = ('crown', 'royal', 'orb', 'monarch', 'vip', 'king', 'headwear')

    def build(self) -> None:
        self.add_arc('orb-right', (24,4), (24,12), radius_x=4)
        self.add_arc('orb-left', (24,12), (24,4), radius_x=4)
        self.add_contour('orb', 'orb-right', 'orb-left', closed=True)
        self.add_line('post', (24,12), (24,16))
        self.relate('connect', 'orb', 'post')
        for side, sign in [('left',-1), ('right',1)]:
            def p(x,y): return (24+sign*x,y)
            self.add_arc(side+'-upper', p(0,16), p(16,24), radius_x=10, sweep=sign==1)
            self.add_arc(side+'-lower', p(16,24), p(12,32), radius_x=10, sweep=sign==1)
            self.add_line(side+'-base', p(12,32), p(10,36))
            self.add_contour(side+'-lobe', side+'-upper', side+'-lower', side+'-base')
            self.relate('connect', 'post', side+'-lobe')
        self.relate('connect', 'left-lobe', 'right-lobe')
        self.add_arc('panel-left', (18,28), (24,16), radius_x=6, radius_y=12)
        self.add_arc('panel-right', (24,16), (30,28), radius_x=6, radius_y=12)
        self.add_contour('panel', 'panel-left', 'panel-right')
        self.relate('connect', 'panel', 'post')
        self.relate('connect', 'panel', 'left-lobe')
        self.relate('connect', 'panel', 'right-lobe')
        self.add_line('band-top', (14,36), (34,36))
        self.add_arc('band-right', (34,36), (34,44), radius_x=4)
        self.add_line('band-bottom', (34,44), (14,44))
        self.add_arc('band-left', (14,44), (14,36), radius_x=4)
        self.add_contour('band', 'band-top', 'band-right', 'band-bottom', 'band-left', closed=True)
        self.relate('connect', 'band', 'left-lobe')
        self.relate('connect', 'band', 'right-lobe')
