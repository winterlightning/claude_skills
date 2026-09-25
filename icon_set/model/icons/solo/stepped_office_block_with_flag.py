'Stepped office: aligned floors and a broad flag band, with straight shared walls.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3c101274-9d7e-5fd8-9939-907b34ebbabe'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/embassy building_3c101274-9d7e-5fd8-9939-907b34ebbabe.svg'
AUTHOR = 'gpt-6'

class SteppedOfficeBlockWithFlag(Solo48):
    icon_id = 'stepped-office-block-with-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('embassy', 'office', 'building', 'government', 'flag', 'civic', 'tower', 'architecture')

    def build(self):
        # Stepped office: aligned floors and a broad flag band, with straight shared walls.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('steps',(6,42),(6,34),(20,34),(20,26),(34,26),(34,42),(6,42))
        l('first-wall',(20,34),(20,42))
        link('connect','first-wall','steps')
        p('flag',(26,26),(26,6),(42,6),(42,14),(26,14))
        link('connect','flag','steps')
