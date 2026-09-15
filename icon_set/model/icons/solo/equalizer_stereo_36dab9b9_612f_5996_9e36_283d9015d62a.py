'Equalizer: equal-size control knobs with exact stem attachments and balanced column spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36dab9b9-612f-5996-9e36-283d9015d62a'
SOURCE_PATH = 'pictographic-primitives/audio/equalizer stereo_36dab9b9-612f-5996-9e36-283d9015d62a.svg'
AUTHOR = 'gpt-6'

class EqualizerStereo(Solo48):
    icon_id = 'equalizer-stereo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('equalizer', 'stereo', 'audio')

    def build(self) -> None:
        # Equal controls on three parallel stems; nodes and stem endpoints share coordinates.
        for name,x,y in (('left',9,22),('middle',24,31),('right',39,16)):
            self.add_arc(name+'-a',(x-5,y),(x+5,y),radius_x=5,radius_y=4)
            self.add_arc(name+'-b',(x+5,y),(x-5,y),radius_x=5,radius_y=4)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
            self.add_line(name+'-upper',(x,8),(x,y-4))
            self.add_line(name+'-lower',(x,y+4),(x,40))
            self.relate('connect',name,name+'-upper');self.relate('connect',name,name+'-lower')
