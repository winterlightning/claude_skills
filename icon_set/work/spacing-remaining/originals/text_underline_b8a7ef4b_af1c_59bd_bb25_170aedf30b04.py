'Underlined U: a true semicircular bowl with 8 units above the underline.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8a7ef4b-af1c-59bd-bb25-170aedf30b04'
SOURCE_PATH = 'icons-json/interface-essential/text underline_b8a7ef4b-af1c-59bd-bb25-170aedf30b04.json'
AUTHOR = 'gpt-6'

class TextUnderline(Solo48):
    icon_id = 'text-underline'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'underline', 'interface-essential')

    def build(self):
        # Underlined U: a true semicircular bowl with 8 units above the underline.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('left',(12,6),(12,22))
        a('bowl',(12,22),(36,22),12,sweep=False)
        l('right',(36,22),(36,6))
        self.add_contour('letter','left','bowl','right')
        l('underline',(6,42),(42,42))
