'Closing quotation marks: matched round bowls and flowing tails, separated by a clear gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2921ecef-6779-4e0d-9ac0-683c2ff1cada'
SOURCE_PATH = 'icons-json/interface-essential/close quote_2921ecef-6779-4e0d-9ac0-683c2ff1cada.json'
AUTHOR = 'gpt-6'

class CloseQuote(Solo48):
    icon_id = 'close-quote'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('close', 'quote', 'interface-essential')

    def build(self) -> None:
        # Two equal quotation marks; smooth comma tails and shared dimensions.
        for name,x in (('left',4),('right',28)):
            self.add_line(name+'-top',(x+8,8),(x+16,8))
            self.add_line(name+'-side',(x+16,8),(x+16,24))
            self.add_bezier(name+'-tail',(x+16,24),((x+16,34),(x+8,40),(x,40)))
            self.add_arc(name+'-bowl',(x,16),(x+8,8),radius_x=8)
            self.add_arc(name+'-return',(x+8,24),(x,16),radius_x=8)
            self.add_contour(name,name+'-return',name+'-bowl',name+'-top',name+'-side',name+'-tail')
