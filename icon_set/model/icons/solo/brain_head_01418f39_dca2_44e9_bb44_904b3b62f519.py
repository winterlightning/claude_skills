"""brain-head — re-authored in place for smooth SOLO48 geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01418f39-dca2-44e9-bb44-904b3b62f519'
SOURCE_PATH = 'pictographic-primitives/health/brain head_01418f39-dca2-44e9-bb44-904b3b62f519.svg'
AUTHOR = 'gpt-6'

class BrainHead(Solo48):
    icon_id = 'brain-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    categories = ('health', 'state')
    aliases = ()
    keywords = ('brain', 'head', 'health')

    def build(self):
        # Profile head with a circular cranium and one smooth nape transition.
        # Shared human_ref/user.svg informs the circular head vocabulary;
        # this continuous anatomical neck has no detached head/body gap.
        # VRECT_L extremes: (8,4)-(40,44). Face intentionally faces left.
        self.add_line('neck-back', (36, 44), (36, 32))
        self.add_bezier('nape', (36, 32), ((36, 27), (40, 25), (40, 18)))
        self.add_arc('cranium', (40, 18), (12, 18), radius_x=14, sweep=False)
        self.add_line('nose-slope', (12, 18), (8, 28))
        self.add_line('nose-base', (8, 28), (12, 28))
        self.add_line('face', (12, 28), (12, 34))
        self.add_arc('chin', (12, 34), (16, 38), radius_x=4, sweep=False)
        self.add_line('jaw', (16, 38), (20, 38))
        self.add_line('neck-front', (20, 38), (20, 44))
        self.add_contour('outline', 'neck-back', 'nape', 'cranium', 'nose-slope', 'nose-base', 'face', 'chin', 'jaw', 'neck-front')
