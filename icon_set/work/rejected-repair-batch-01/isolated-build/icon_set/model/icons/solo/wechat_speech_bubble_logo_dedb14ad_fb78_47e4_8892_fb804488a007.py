"""Wide oval bubble with a lower-left tail and two staggered text lines. Use smooth coherent curves and two shared text baselines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dedb14ad-fb78-47e4-8892-fb804488a007'
SOURCE_PATH = 'pictographic-primitives/logos/wechat logo_dedb14ad-fb78-47e4-8892-fb804488a007.svg'
AUTHOR = 'gpt-6'

class WechatSpeechBubbleLogo(Solo48):
    icon_id = 'wechat-speech-bubble-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('wechat', 'chat', 'message', 'speech-bubble', 'logo', 'brand', 'text')

    def build(self):
        # Plan: Wide oval bubble with a lower-left tail and two staggered text lines. Use smooth coherent curves and two shared text baselines.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_bezier('bubble',(10,30),((6,27),(4,24),(4,22)),((4,14),(12,8),(24,8)),((36,8),(44,14),(44,22)),((44,30),(36,36),(24,36)),((21,36),(18,35),(16,34)))
        self.add_polyline('tail',(16,34),(8,40),(10,30));self.relate('connect','bubble','tail')
        self.add_line('text-top',(16,18),(32,18));self.add_line('text-bottom',(20,27),(28,27))

