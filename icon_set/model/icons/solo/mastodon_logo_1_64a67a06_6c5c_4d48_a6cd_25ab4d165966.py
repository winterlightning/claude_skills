'Mastodon mark: smooth tangent corners and a generous return, preserving the familiar silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64a67a06-6c5c-4d48-a6cd-25ab4d165966'
SOURCE_PATH = 'pictographic-primitives/logos/mastodon logo 1_64a67a06-6c5c-4d48-a6cd-25ab4d165966.svg'
AUTHOR = 'gpt-6'

class MastodonLogo1(Solo48):
    icon_id = 'mastodon-logo-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('mastodon', 'logo', 'logos')

    def build(self):
        # Mastodon mark: smooth tangent corners and a generous return, preserving the familiar silhouette.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('top',(16,6),(32,6))
        a('tr',(32,6),(42,16),10)
        l('right',(42,16),(42,24))
        a('br',(42,24),(32,34),10)
        l('return',(32,34),(18,34))
        a('tail',(18,34),(26,42),8,sweep=False)
        l('bottom',(26,42),(20,42))
        a('bl',(20,42),(6,28),14)
        l('left',(6,28),(6,16))
        a('tl',(6,16),(16,6),10)
        self.add_contour('mark','top','tr','right','br','return','tail','bottom','bl','left','tl',closed=True)
