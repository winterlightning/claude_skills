"""Straight lead pipe, flared bell, oval tubing loop and two valve stems. Omit one valve and tiny mouthpiece collar. Extremes (4,8)-(44,40). Lucide megaphone flare construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='32a8bbb9-878f-46c6-b55a-43f7976b99d3'
SOURCE_PATH='pictographic-primitives/music/trumpet_32a8bbb9-878f-46c6-b55a-43f7976b99d3.svg'
AUTHOR='gpt-6'

class Trumpet(Solo48):
    icon_id='trumpet'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/music"
    aliases=()
    keywords=('trumpet', 'brass', 'instrument', 'horn', 'jazz', 'band', 'fanfare', 'music')

    def build(self):
        self.add_polyline('lead',(4,20),(10,20),(16,20),(20,20),(24,20),(32,20))
        self.add_polyline('bell',(32,20),(44,8),(44,32),closed=True)
        self.relate('connect','lead','bell')
        self.add_arc('tube-left',(10,20),(10,40),radius_x=6,radius_y=10,sweep=False)
        self.add_line('tube-bottom',(10,40),(20,40))
        self.add_arc('tube-right',(20,40),(20,20),radius_x=6,radius_y=10,sweep=False)
        self.add_contour('tube','tube-left','tube-bottom','tube-right')
        self.relate('connect','lead','tube')
        for n,x in enumerate((16,24)):
            self.add_line(f'valve-{n}',(x,12),(x,20))
            self.relate('connect',f'valve-{n}','lead')
