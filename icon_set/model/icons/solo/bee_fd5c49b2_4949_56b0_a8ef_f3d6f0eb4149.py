"""Top-view bee; paired wings and two abdominal bands. Lucide bug informs capsule construction; antenna curls reduced to sweeping arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd5c49b2-4949-56b0-a8ef-f3d6f0eb4149'
SOURCE_PATH = 'pictographic-primitives/animals/bee_fd5c49b2-4949-56b0-a8ef-f3d6f0eb4149.svg'
AUTHOR = 'gpt-6'


class BeeWithSweptWings(Solo48):
    icon_id = 'bee-with-swept-wings'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('bee', 'honeybee', 'insect', 'wings', 'stripes', 'honey', 'pollinate', 'bug')

    def build(self) -> None:
        # SQUARE centerline extremes recorded in batch-02-review.md.
        self.add_arc('crown-left', (16, 18), (24, 10), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('crown-right', (24, 10), (32, 18), radius_x=8, radius_y=8, sweep=True)
        self.add_line('side-right', (32, 18), (32, 34))
        self.add_arc('base-right', (32, 34), (24, 42), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('base-left', (24, 42), (16, 34), radius_x=8, radius_y=8, sweep=True)
        self.add_line('side-left', (16, 34), (16, 18))
        self.add_contour('body', 'crown-left', 'crown-right', 'side-right', 'base-right', 'base-left', 'side-left', closed=True)
        self.add_line('stripe-18', (16, 18), (32, 18))
        self.relate("connect", 'body', 'stripe-18')
        self.add_line('stripe-26', (16, 26), (32, 26))
        self.relate("connect", 'body', 'stripe-26')
        self.add_line('stripe-34', (16, 34), (32, 34))
        self.relate("connect", 'body', 'stripe-34')
        self.add_line('stinger', (24, 42), (24, 46))
        self.relate("connect", 'body', 'stinger')
        self.add_arc('left-wing-upper', (16, 18), (2, 34), radius_x=30, radius_y=30, sweep=True)
        self.add_arc('left-wing-lower', (2, 34), (16, 34), radius_x=7, radius_y=6, sweep=False)
        self.add_contour('left-wing', 'left-wing-upper', 'left-wing-lower', closed=False)
        self.relate("connect", 'body', 'left-wing')
        self.add_line('left-antenna-stem', (16, 18), (16, 8))
        self.add_arc('left-antenna-curl', (16, 8), (10, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('left-antenna', 'left-antenna-stem', 'left-antenna-curl', closed=False)
        self.relate("connect", 'body', 'left-antenna')
        self.relate("connect", 'left-wing', 'left-antenna')
        self.add_arc('right-wing-upper', (32, 18), (46, 34), radius_x=30, radius_y=30, sweep=False)
        self.add_arc('right-wing-lower', (46, 34), (32, 34), radius_x=7, radius_y=6, sweep=True)
        self.add_contour('right-wing', 'right-wing-upper', 'right-wing-lower', closed=False)
        self.relate("connect", 'body', 'right-wing')
        self.add_line('right-antenna-stem', (32, 18), (32, 8))
        self.add_arc('right-antenna-curl', (32, 8), (38, 2), radius_x=6, radius_y=6, sweep=False)
        self.add_contour('right-antenna', 'right-antenna-stem', 'right-antenna-curl', closed=False)
        self.relate("connect", 'body', 'right-antenna')
        self.relate("connect", 'right-wing', 'right-antenna')
