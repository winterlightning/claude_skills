"""Fresh SOLO48 revision of hubot-logo from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7004b716-3a3b-4f2a-8272-02ce97782981'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hubot-logo/20260927T061852Z-thuan-mac-1/reference/hubot logo_7004b716-3a3b-4f2a-8272-02ce97782981.svg'
AUTHOR = "gpt-6"

class HubotLogo(Solo48):
    icon_id = 'hubot-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('hubot', 'github', 'robot', 'chatbot', 'logo', 'brand', 'automation')

    def build(self) -> None:

        # Arched robot head, pulse visor band and trapezoid mouth.
        path(self,'head',(8,44),('L',(8,20)),('A',16,16,True,(24,4)),
             ('A',16,16,True,(40,20)),('L',(40,44)))
        poly(self,'visor',(16,22),(20,22),(23,18),(26,26),(29,22),(32,22),
             (32,30),(16,30),closed=True)
        poly(self,'mouth',(20,40),(21,36),(27,36),(28,40),closed=True)
        contacts(self)
