'Microphone: symmetric capsule and curved cradle with one clean stem junction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88610259-450b-43f2-85da-95879335b5f2'
SOURCE_PATH = 'icons-json/audio/microphone_88610259-450b-43f2-85da-95879335b5f2.json'
AUTHOR = 'gpt-6'

class Microphone88610259(Solo48):
    icon_id = 'microphone-88610259'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self) -> None:
        # Capsule and cradle share an axis; only the cradle joins the stand.
        self.add_arc('cap-top',(17,11),(31,11),radius_x=7)
        self.add_line('cap-right',(31,11),(31,17))
        self.add_arc('cap-bottom',(31,17),(17,17),radius_x=7)
        self.add_line('cap-left',(17,17),(17,11))
        self.add_contour('capsule','cap-top','cap-right','cap-bottom','cap-left',closed=True)
        self.add_arc('cradle-left',(8,20),(24,35),radius_x=16,radius_y=15,sweep=False)
        self.add_arc('cradle-right',(24,35),(40,20),radius_x=16,radius_y=15,sweep=False)
        self.add_contour('cradle','cradle-left','cradle-right')
        self.add_line('stand',(24,35),(24,44))
        self.relate('connect','cradle','stand')
