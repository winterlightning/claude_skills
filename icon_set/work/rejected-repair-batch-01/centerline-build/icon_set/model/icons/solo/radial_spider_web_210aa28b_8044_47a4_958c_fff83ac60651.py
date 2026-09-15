"""Radial Spider Web; re-authored from the supplied visual reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '210aa28b-8044-47a4-958c-fff83ac60651'
SOURCE_PATH = 'pictographic-primitives/websites/web_210aa28b-8044-47a4-958c-fff83ac60651.svg'
SOURCE_REFERENCES = ({'source_icon_id': '210aa28b-8044-47a4-958c-fff83ac60651', 'source_path': 'pictographic-primitives/websites/web_210aa28b-8044-47a4-958c-fff83ac60651.svg'},)
AUTHOR = 'gpt-6'

class RadialSpiderWeb(Solo48):
    icon_id = 'radial-spider-web'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/invertebrates"
    aliases = ()
    keywords = ('web', 'spider', 'radial', 'strands', 'cobweb', 'nature', 'network')

    def build(self) -> None:
        # The eight spokes share one central junction. Axial tips reach radius 20.
        center=(24,24)
        points=[(24,6),(38,10),(42,24),(38,38),(24,42),(10,38),(6,24),(10,10)]
        for n,p in enumerate(points):
            self.add_arc(f'rim-{n}',p,points[(n+1)%8],radius_x=22,sweep=False)
        self.add_contour('rim',*(f'rim-{n}' for n in range(8)),closed=True)
        for n,p in enumerate(points):
            self.add_line(f'spoke-{n}',center,p)
            self.relate('connect',f'spoke-{n}','rim')
            for earlier in range(n):self.relate('connect',f'spoke-{n}',f'spoke-{earlier}')
