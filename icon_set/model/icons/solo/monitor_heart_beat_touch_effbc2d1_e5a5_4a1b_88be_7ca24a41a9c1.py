"""A finger touching a pulse sensor.
Symbol plan and construction: hand: coherent pointing-finger contour; heart-pulse: waveform; human references checked for hand-only anatomy.
Keyshape: VRECT_L reserves the upper sensor and lower pointing hand bands.
Omissions: Fine thumb contour steps; pulse amplitude reduced.
Review: Finger width is eight, the sensor walls share actual finger nodes, and the palm is ten units below the sensor bottom. Rounded thumb and finger read as a hand. No detached head/body gap applies."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'effbc2d1-e5a5-4a1b-88be-7ca24a41a9c1'
SOURCE_PATH = 'pictographic-primitives/health/monitor heart beat touch_effbc2d1-e5a5-4a1b-88be-7ca24a41a9c1.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'monitor-heart-beat-touch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('monitor heart beat touch',)





    def build(self):
        # Sensor and pointing hand share the two finger-wall nodes at y28.
        # Hand-only subject: detached head/body requirements do not apply.
        self.add_line('sensor-left',(10,24),(10,14))
        self.add_arc('sensor-top',(10,14),(34,14),radius_x=12,radius_y=10)
        self.add_line('sensor-right',(34,14),(34,24))
        self.add_arc('sensor-br',(34,24),(30,28),radius_x=4)
        self.add_line('sensor-bottom-right',(30,28),(24,28))
        self.add_line('sensor-bottom-left',(16,28),(14,28))
        self.add_arc('sensor-bl',(14,28),(10,24),radius_x=4)
        self.add_contour('sensor','sensor-bottom-left','sensor-bl','sensor-left','sensor-top','sensor-right','sensor-br','sensor-bottom-right')
        self.add_polyline('pulse',(10,14),(17,14),(21,12),(25,17),(28,14),(34,14))
        self.relate('connect','sensor','pulse')
        self.add_line('thumb-outer',(14,44),(8,40))
        self.add_arc('thumb-cap',(8,40),(16,40),radius_x=4)
        self.add_line('finger-left',(16,40),(16,28))
        self.add_arc('finger-tip',(16,28),(24,28),radius_x=4)
        self.add_line('finger-right',(24,28),(24,38))
        self.add_line('palm-top',(24,38),(34,38))
        self.add_arc('palm-corner',(34,38),(40,44),radius_x=6)
        self.add_contour('hand','thumb-outer','thumb-cap','finger-left','finger-tip','finger-right','palm-top','palm-corner')
        self.relate('connect','sensor','hand')
