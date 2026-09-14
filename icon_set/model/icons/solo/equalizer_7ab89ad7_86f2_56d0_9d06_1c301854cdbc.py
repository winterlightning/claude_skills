'Equalizer: equal-size control knobs with exact stem attachments and balanced column spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ab89ad7-86f2-56d0-9d06-1c301854cdbc'
SOURCE_PATH = 'icons-json/audio/equalizer_7ab89ad7-86f2-56d0-9d06-1c301854cdbc.json'
AUTHOR = 'gpt-6'

class EqualizerAudio(Solo48):
    icon_id = 'equalizer-audio'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('equalizer', 'audio')

    def build(self) -> None:
        # Equal controls on three parallel stems; nodes and stem endpoints share coordinates.
        for name,x,y in (('left',9,22),('middle',24,31),('right',39,16)):
            self.add_arc(name+'-a',(x-5,y),(x+5,y),radius_x=5,radius_y=4)
            self.add_arc(name+'-b',(x+5,y),(x-5,y),radius_x=5,radius_y=4)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
            self.add_line(name+'-upper',(x,8),(x,y-4))
            self.add_line(name+'-lower',(x,y+4),(x,40))
            self.relate('connect',name,name+'-upper');self.relate('connect',name,name+'-lower')
