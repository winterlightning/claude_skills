'Hot Steaming Coffee Cup.\n\nSymbol plan: Rounded coffee bowl, open-loop handle and one steam wisp; omit thin elliptical drink rim.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: coffee.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '043154b0-0611-4b18-8bcc-ee10abcadb6d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/latte_043154b0-0611-4b18-8bcc-ee10abcadb6d.svg'
AUTHOR = 'gpt-6'

class SteamingLatteCup(Solo48):
    icon_id = 'steaming-latte-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('steaming', 'latte', 'cup')

    def build(self):
        # Rounded coffee bowl, open-loop handle and one steam wisp; omit thin elliptical drink rim.
        axis_x = 24
        p_6_20 = (6, 20)
        p_6_29 = (6, 29)
        p_6_37 = (6, 37)
        p_10_42 = (10, 42)
        p_16_9 = (16, 9)
        p_19_42 = (19, 42)
        p_20_6 = (20, 6)
        p_20_12 = (20, 12)
        p_23_10 = (23, 10)
        p_28_42 = (28, 42)
        p_32_20 = (32, 20)
        p_32_29 = (32, 29)
        p_32_32 = (32, 32)
        p_32_37 = (32, 37)
        p_36_20 = (36, 20)
        p_36_32 = (36, 32)
        p_44_20 = (44, 20)
        p_44_32 = (44, 32)
        self.add_line('bowl-1', p_6_20, p_32_20)
        self.add_line('bowl-2', p_32_20, p_32_29)
        self.add_bezier('bowl-3', p_32_29, (p_32_37, p_28_42, p_19_42))
        self.add_bezier('bowl-4', p_19_42, (p_10_42, p_6_37, p_6_29))
        self.add_line('bowl-5', p_6_29, p_6_20)
        self.add_contour('bowl', 'bowl-1', 'bowl-2', 'bowl-3', 'bowl-4', 'bowl-5', closed=True)
        self.add_line('handle-1', p_32_20, p_36_20)
        self.add_bezier('handle-2', p_36_20, (p_44_20, p_44_32, p_36_32))
        self.add_line('handle-3', p_36_32, p_32_32)
        self.add_contour('handle', 'handle-1', 'handle-2', 'handle-3', closed=False)
        self.relate("connect", 'bowl', 'handle')
        self.add_bezier('steam-1', p_20_6, (p_16_9, p_23_10, p_20_12))
        self.add_contour('steam', 'steam-1', closed=False)
