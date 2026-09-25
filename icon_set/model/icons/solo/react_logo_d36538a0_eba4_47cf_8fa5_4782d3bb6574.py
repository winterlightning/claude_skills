# Repair: Rebalance all three React orbits together to enlarge the six outer counters without changing the atom topology.
"""Three repeated elliptical orbits rotated by 60 degrees, sharing every true crossing node, around a central dot. Lucide atom informs smooth cubic loops. Parameters own all repeated geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd36538a0-eba4-47cf-8fa5-4782d3bb6574'
SOURCE_PATH = 'pictographic-primitives/logos/react native logo_d36538a0-eba4-47cf-8fa5-4782d3bb6574.svg'
AUTHOR = 'gpt-6'

class ReactLogo(Solo48):
    icon_id = 'react-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('react', 'react-native', 'atom', 'javascript', 'logo', 'brand', 'developer')

    def build(self):
        from ._symmetry_curves import path, poly, contacts
        poly(self,'inner',(14,18),(24,13),(34,18),(34,30),(24,35),(14,30),closed=True)
        path(self,'upper-left',(14,18),('C',(8,4),(20,4),(24,13)))
        path(self,'upper-right',(24,13),('C',(28,4),(40,4),(34,18)))
        path(self,'right',(34,18),('C',(47.3333333333,18),(47.3333333333,30),(34,30)))
        path(self,'lower-right',(34,30),('C',(40,44),(28,44),(24,35)))
        path(self,'lower-left',(24,35),('C',(20,44),(8,44),(14,30)))
        path(self,'left',(14,30),('C',(0.6666666667,30),(0.6666666667,18),(14,18)))
        self.add_dot('nucleus',(24,24))
        contacts(self)
