"""Headphone Listener with Cigarette.

Symbol plan: Circular face under a headphone arch, side ear pads and an angled cigarette. Drop facial microdetails.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide headphones: a broad band and side pads; human_ref/user.svg: circular face construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bc938aa3-95bd-4a96-b283-3c27b08596d6'
SOURCE_PATH = 'pictographic-primitives/audio/music genre smoke_bc938aa3-95bd-4a96-b283-3c27b08596d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'headphone-listener-with-cigarette'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('person', 'cigarette', 'headphones', 'audio', 'listening', 'music', 'earcup', 'headband', 'sound', 'equipment')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        # Circular jaw and headband share the side pad junctions.
        arc('band',(6,24),(42,24),18)
        arc('face-r',(34,24),(30,32),10)
        arc('face-l',(30,32),(14,24),10)
        join('face','face-r','face-l')
        line('pad-left',(6,24),(14,24));connect('pad-left','band');connect('pad-left','face')
        line('pad-right',(34,24),(42,24));connect('pad-right','band');connect('pad-right','face')
        line('left-pad-depth',(6,24),(6,32));connect('left-pad-depth','pad-left');connect('left-pad-depth','band')
        line('right-pad-depth',(42,24),(42,32));connect('right-pad-depth','pad-right');connect('right-pad-depth','band')
        line('cigarette',(30,32),(40,42))
        connect('face','cigarette')
