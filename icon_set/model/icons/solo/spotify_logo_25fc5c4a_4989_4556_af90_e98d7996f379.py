"""Circular badge with three smoothly arched waves of decreasing width. Keep all three waves with a slight downward-right slope and controlled vertical steps; reduce outlined bars to uniform strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25fc5c4a-4989-4556-af90-e98d7996f379'
SOURCE_PATH = 'pictographic-primitives/logos/spotify logo_25fc5c4a-4989-4556-af90-e98d7996f379.svg'
AUTHOR = 'gpt-6'

class SpotifyLogo(Solo48):
    icon_id = 'spotify-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('spotify', 'music', 'streaming', 'sound-waves', 'logo', 'brand', 'audio')

    def build(self):
        # Plan: Circular badge with three smoothly arched waves of decreasing width. Keep all three waves with a slight downward-right slope and controlled vertical steps; reduce outlined bars to uniform strokes.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        circle('badge',24,24,20)
        for j,(left,right,y,c) in enumerate([(15,33,17,15),(17,31,26,24),(20,28,34,33)]):
            self.add_bezier('wave-'+str(j),(left,y),((left+(right-left)/3,c),(right-(right-left)/3,c),(right,y+1)))

