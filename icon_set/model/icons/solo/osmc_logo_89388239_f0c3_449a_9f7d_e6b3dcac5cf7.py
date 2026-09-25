"""Concentric badge; mirrored bowtie triangles share their central vertex. Preserve the intrinsic brand emblem."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89388239-f0c3-449a-9f7d-e6b3dcac5cf7'
SOURCE_PATH = 'pictographic-primitives/logos/osmc logo_89388239-f0c3-449a-9f7d-e6b3dcac5cf7.svg'
AUTHOR = 'gpt-6'

class OsmcLogo(Solo48):
    icon_id = 'osmc-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('osmc', 'media-center', 'bowtie', 'logo', 'brand', 'kodi', 'open-source')

    def build(self):
        # Plan: Concentric badge; mirrored bowtie triangles share their central vertex. Preserve the intrinsic brand emblem.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        circle('badge',24,24,20)
        for side,x in [('left',15),('right',33)]:
            self.add_polyline(side,(24,24),(x,18),(x,30),closed=True)
        self.relate('connect','left','right')

