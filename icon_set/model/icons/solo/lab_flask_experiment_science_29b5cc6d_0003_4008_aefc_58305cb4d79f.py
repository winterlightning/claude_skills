"""lab-flask-experiment-science: approved original model.

Construction: Pear-shaped science flask with a narrow neck and an undulating liquid surface.
Keyshape: VRECT_L; exact SOLO48 envelope.
Construction reference: flask-conical from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '29b5cc6d-0003-4008-aefc-58305cb4d79f'
SOURCE_PATH = 'pictographic-primitives/science/lab flask experiment_29b5cc6d-0003-4008-aefc-58305cb4d79f.svg'
AUTHOR = 'gpt-6'

class LabFlaskExperimentScience(Solo48):
    icon_id = 'lab-flask-experiment-science'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'flask', 'experiment', 'science')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self, 'flask', (18, 4), ('L', (30, 4)), ('L', (30, 20)), ('C', (30, 22), (40, 22), (40, 32)), ('A', 12, 12, True, (28, 44)), ('L', (20, 44)), ('A', 12, 12, True, (8, 32)), ('C', (8, 22), (18, 22), (18, 20)), ('L', (18, 4)), closed=True)
        path(self, 'liquid', (8, 32), ('C', (16, 26), (16, 38), (24, 32)), ('C', (32, 26), (32, 38), (40, 32)))
        contacts(self)
