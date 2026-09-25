"""Eight equal-direction asterisk arms around a square opening. Reduce the thick outer ribbon to eight strokes and enlarge the central square to preserve legal spacing between arms."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'beb8aa7d-dfb3-4a43-af57-8d9d82279923'
SOURCE_PATH = 'pictographic-primitives/logos/zapier logo_beb8aa7d-dfb3-4a43-af57-8d9d82279923.svg'
AUTHOR = 'gpt-6'

class ZapierLogo(Solo48):
    icon_id = 'zapier-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('zapier', 'automation', 'asterisk', 'workflow', 'logo', 'brand', 'integration')

    def build(self):
        # Plan: Eight equal-direction asterisk arms around a square opening. Reduce the thick outer ribbon to eight strokes and enlarge the central square to preserve legal spacing between arms.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        nodes=[(16,16),(24,16),(32,16),(32,24),(32,32),(24,32),(16,32),(16,24)]
        ends=[(6,6),(24,6),(42,6),(42,24),(42,42),(24,42),(6,42),(6,24)]
        for j,a in enumerate(nodes):self.add_line('hub-'+str(j),a,nodes[(j+1)%8])
        self.add_contour('hub',*[f'hub-{j}' for j in range(8)],closed=True)
        for j,(a,b) in enumerate(zip(nodes,ends)):
            self.add_line('arm-'+str(j),a,b);self.relate('connect','hub','arm-'+str(j))

