'MediaConnect: a regular isometric cube inside two clean outer bracket strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e19348b9-bdcd-4de4-84e3-e69ce4b9d8b8'
SOURCE_PATH = 'icons-json/apps/elemental mediaconnect_e19348b9-bdcd-4de4-84e3-e69ce4b9d8b8.json'
AUTHOR = 'gpt-6'

class ElementalMediaconnect(Solo48):
    icon_id = 'elemental-mediaconnect'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('elemental', 'mediaconnect', 'apps')

    def build(self):
        # MediaConnect: spacious regular cube faces and open outer brackets, avoiding forced compression.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('cube',(24,14),(34,20),(34,30),(24,36),(14,30),(14,20),(24,14))
        p('edges',(14,20),(24,26),(34,20))
        l('vertical',(24,26),(24,36))
        link('connect','cube','edges')
        link('connect','cube','vertical')
        link('connect','edges','vertical')
        p('outer-left',(12,40),(6,36),(6,14),(18,6))
        p('outer-right',(42,14),(42,36),(30,42))
