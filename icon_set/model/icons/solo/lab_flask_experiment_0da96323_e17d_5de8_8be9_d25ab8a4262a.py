"""lab-flask-experiment: approved original model.

Construction: Round-bottom boiling flask with a circular bulb and a straight liquid surface through its widest points.
Keyshape: VRECT_L; exact SOLO48 envelope.
Construction reference: flask-conical from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '0da96323-e17d-5de8-8be9-d25ab8a4262a'
SOURCE_PATH = 'pictographic-primitives/science/lab flask experiment_0da96323-e17d-5de8-8be9-d25ab8a4262a.svg'
AUTHOR = 'gpt-6'

class LabFlaskExperiment(Solo48):
    icon_id = 'lab-flask-experiment'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'flask', 'experiment', 'science')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self, 'flask', (18, 4), ('L', (30, 4)), ('L', (30, 14)), ('C', (36, 17), (40, 21), (40, 28)), ('A', 16, 16, True, (24, 44)), ('A', 16, 16, True, (8, 28)), ('C', (8, 21), (12, 17), (18, 14)), ('L', (18, 4)), closed=True)
        line(self, 'liquid', (8, 28), (40, 28))
        contacts(self)
