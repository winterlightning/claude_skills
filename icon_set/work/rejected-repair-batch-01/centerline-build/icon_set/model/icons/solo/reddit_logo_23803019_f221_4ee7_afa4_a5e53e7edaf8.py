"""Snoo face with paired eyes, a gentle smile and the asymmetric antenna. Omit small ears to preserve facial space. This alien head has no detached human body."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23803019-f221-4ee7-afa4-a5e53e7edaf8'
SOURCE_PATH = 'pictographic-primitives/logos/reddit logo_23803019-f221-4ee7-afa4-a5e53e7edaf8.svg'
AUTHOR = 'gpt-6'

class RedditLogo(Solo48):
    icon_id = 'reddit-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('reddit', 'snoo', 'social', 'alien', 'logo', 'brand', 'community')

    def build(self):
        # Plan: Snoo face with paired eyes, a gentle smile and the asymmetric antenna. Omit small ears to preserve facial space. This alien head has no detached human body.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_arc('face-top',(8,30),(24,16),radius_x=16,radius_y=14)
        self.add_arc('face-right',(24,16),(40,30),radius_x=16,radius_y=14)
        self.add_arc('face-bottom',(40,30),(8,30),radius_x=16,radius_y=14)
        self.add_contour('face','face-top','face-right','face-bottom',closed=True)
        self.add_polyline('antenna',(24,16),(26,4),(34,7))
        circle('tip',37,7,3)
        self.relate('connect','antenna','face')
        self.relate('connect','antenna','tip')
        for x in (19,29):self.add_dot('eye-'+str(x),(x,26))
        self.add_bezier('smile',(20,35),((22,36),(26,36),(28,35)))

