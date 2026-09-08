"""Standing llama in left profile. Long neck, pointed ear and rounded rump retained; four legs reduced to two visible legs. No useful exact Lucide match; simple contour construction follows cat."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c296f6df-7f03-557e-90f3-1cb6a7f08661'
SOURCE_PATH = 'pictographic-primitives/animals/lama_c296f6df-7f03-557e-90f3-1cb6a7f08661.svg'
AUTHOR = 'gpt-6'


class Llama(Solo48):
    icon_id = 'llama'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('llama', 'alpaca', 'standing', 'andes', 'animal', 'wool', 'farm', 'south america')

    def build(self) -> None:
        # Exact visible extremes: (0, 0, 48, 48); centerline inset 2.
        self.add_line('ear-rise', (15,12), (15,2))
        self.add_line('ear-tip', (15,2), (20,7))
        self.add_arc('neck-top', (20, 7), (23, 20), radius_x=24, radius_y=24, sweep=True, large_arc=False)
        self.add_line('neck-back', (23, 20), (23, 25))
        self.add_line('back', (23, 25), (34, 25))
        self.add_arc('rump', (34, 25), (46, 34), radius_x=12, radius_y=9, sweep=True, large_arc=False)
        self.add_line('rear-leg', (46, 34), (46, 46))
        self.add_line('rear-hoof', (46, 46), (38, 46))
        self.add_line('rear-inner', (38, 46), (38, 38))
        self.add_line('belly', (38, 38), (20, 38))
        self.add_line('front-inner', (20, 38), (20, 46))
        self.add_line('front-hoof', (20, 46), (12, 46))
        self.add_line('front-leg', (12, 46), (12, 23))
        self.add_line('muzzle-bottom', (12, 23), (6, 23))
        self.add_arc('muzzle', (6, 23), (6, 15), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('muzzle-top', (6, 15), (15, 12))
        self.add_contour('outline', 'ear-rise', 'ear-tip', 'neck-top', 'neck-back', 'back', 'rump', 'rear-leg', 'rear-hoof', 'rear-inner', 'belly', 'front-inner', 'front-hoof', 'front-leg', 'muzzle-bottom', 'muzzle', 'muzzle-top', closed=True)
