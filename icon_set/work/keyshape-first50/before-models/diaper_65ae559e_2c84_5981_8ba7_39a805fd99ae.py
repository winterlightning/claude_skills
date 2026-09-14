from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65ae559e-2c84-5981-8ba7-39a805fd99ae'
SOURCE_PATH = 'pictographic-primitives/babies/baby care diaper_65ae559e-2c84-5981-8ba7-39a805fd99ae.svg'
AUTHOR = 'gpt-6'

class Diaper(Solo48):
    icon_id = 'diaper'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/baby-care"
    aliases = ()
    keywords = ('diaper', 'nappy', 'baby', 'infant', 'changing', 'childcare', 'hygiene', 'toddler')

    # Designed to centerline extremes (6, 8)–(42, 40).
    def build(self) -> None:
        self.add_line('shell-1', (6, 8), (42, 8))
        self.add_line('shell-2', (42, 8), (42, 18))
        self.add_arc('shell-3', (42, 18), (24, 40), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('shell-4', (24, 40), (6, 18), radius_x=22, radius_y=22, sweep=True)
        self.add_line('shell-5', (6, 18), (6, 8))
        self.add_contour('shell', 'shell-1', 'shell-2', 'shell-3', 'shell-4', 'shell-5', closed=True)
        self.add_line('tab-left-1', (6, 18), (11, 18))
        self.add_contour('tab-left', 'tab-left-1', closed=False)
        self.add_line('tab-right-1', (42, 18), (37, 18))
        self.add_contour('tab-right', 'tab-right-1', closed=False)
        self.relate("connect", "shell", "tab-left")
        self.relate("connect", "shell", "tab-right")
