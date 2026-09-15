"""Four long round-ended bars and four short dots on one 12-unit lattice. Preserve the eight-part pinwheel and open center, reducing capsule outlines to solid strokes. Lucide audio-lines informs clean round-ended mark vocabulary."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dff5334a-149f-433d-add2-7604aa35780f'
SOURCE_PATH = 'pictographic-primitives/logos/slack logo_dff5334a-149f-433d-add2-7604aa35780f.svg'
AUTHOR = 'gpt-6'

class SlackLogo(Solo48):
    icon_id = 'slack-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('slack', 'chat', 'workspace', 'hash', 'logo', 'brand', 'collaboration')

    def build(self):
        # Plan: Four long round-ended bars and four short dots on one 12-unit lattice. Preserve the eight-part pinwheel and open center, reducing capsule outlines to solid strokes. Lucide audio-lines informs clean round-ended mark vocabulary.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        for j,(a,b) in enumerate([((30,6),(30,18)),((6,18),(18,18)),((18,30),(18,42)),((30,30),(42,30))]):
            self.add_line('bar-'+str(j),a,b)
        for j,p in enumerate([(18,6),(6,30),(30,42),(42,18)]):self.add_dot('stub-'+str(j),p)

