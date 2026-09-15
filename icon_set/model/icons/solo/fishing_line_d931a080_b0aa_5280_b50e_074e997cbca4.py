'Fishing hook: clean broad eye, actual shaft contacts, and a continuous rounded hook bend.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd931a080-b0aa-5280-b50e-074e997cbca4'
SOURCE_PATH = 'pictographic-primitives/outdoors/fishing line_d931a080-b0aa-5280-b50e-074e997cbca4.svg'
AUTHOR = 'gpt-6'

class FishingLine(Solo48):
    icon_id = 'fishing-line'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('fishing', 'line', 'outdoors')

    def build(self) -> None:
        # Tall hook with a broad eye and smoothly curved lower bend.
        self.add_line('line',(33,4),(33,12))
        self.add_arc('eye-a',(26,16),(40,16),radius_x=7,radius_y=4)
        self.add_arc('eye-b',(40,16),(26,16),radius_x=7,radius_y=4)
        self.add_contour('eye','eye-a','eye-b',closed=True)
        self.add_line('shaft',(33,20),(33,32))
        self.add_bezier('bend',(33,32),((33,40),(27,44),(20,44)),((13,44),(8,40),(8,34)))
        self.add_polyline('barb',(8,34),(8,29),(14,34))
        self.add_contour('hook','shaft','bend')
        self.relate('connect','hook','barb');self.relate('connect','hook','eye');self.relate('connect','line','eye')
