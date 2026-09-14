'Open quotation marks: reflected equal curved bowls from the matching close-quote construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85ffc214-8dd9-5360-9fc5-4074fb6d8b16'
SOURCE_PATH = 'icons-json/interface-essential/open quote_85ffc214-8dd9-5360-9fc5-4074fb6d8b16.json'
AUTHOR = 'gpt-6'

class OpenQuote(Solo48):
    icon_id = 'open-quote'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('open', 'quote', 'interface-essential')

    def build(self) -> None:
        def p(x,y): return 48-x,48-y
        for name,x in (('left',4),('right',28)):
            self.add_line(name+'-top',p(x+8,8),p(x+16,8))
            self.add_line(name+'-side',p(x+16,8),p(x+16,24))
            self.add_bezier(name+'-tail',p(x+16,24),(p(x+16,34),p(x+8,40),p(x,40)))
            self.add_arc(name+'-bowl',p(x,16),p(x+8,8),radius_x=8)
            self.add_arc(name+'-return',p(x+8,24),p(x,16),radius_x=8)
            self.add_contour(name,name+'-return',name+'-bowl',name+'-top',name+'-side',name+'-tail')
