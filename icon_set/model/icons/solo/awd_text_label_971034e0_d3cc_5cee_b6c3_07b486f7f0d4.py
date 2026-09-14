'AWD lettering: uniform vertical stems, a smooth D and a legible compact W.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '971034e0-d3cc-5cee-b6c3-07b486f7f0d4'
SOURCE_PATH = 'pictographic-primitives/transportation/all wheel drive_971034e0-d3cc-5cee-b6c3-07b486f7f0d4.svg'
AUTHOR = 'gpt-6'

class AwdTextLabel(Solo48):
    icon_id = 'awd-text-label'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('awd', 'all wheel drive', 'drivetrain', 'car', 'dashboard', 'text', 'label', '4x4')

    def build(self):
        # AWD wordmark: a naturally wide W shares its top endpoints with A and D instead of being squeezed.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        # Shared top endpoints make an intentional connected wordmark, leaving W its natural width.
        p('a',(4,40),(4,8),(12,8),(12,40))
        l('a-bar',(4,24),(12,24))
        link('connect','a','a-bar')
        p('w',(12,8),(19,40),(24,20),(29,40),(36,8))
        l('d-left',(36,8),(36,40))
        a('d-curve',(36,8),(36,40),8,16)
        link('connect','a','w')
        link('connect','w','d-left')
        link('connect','w','d-curve')
        link('connect','d-left','d-curve')
