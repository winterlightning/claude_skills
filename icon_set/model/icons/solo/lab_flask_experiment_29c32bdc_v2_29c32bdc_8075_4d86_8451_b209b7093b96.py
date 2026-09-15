'lab-flask-experiment-29c32bdc: distinct review variant.\n\nConstruction: Empty broad-neck laboratory flask with a neck collar and a flatter, round-cornered base.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nConstruction reference: flask-conical from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '29c32bdc-8075-4d86-8451-b209b7093b96'
SOURCE_PATH = 'pictographic-primitives/science/lab flask experiment_29c32bdc-8075-4d86-8451-b209b7093b96.svg'
AUTHOR = 'gpt-6'


class LabFlaskExperiment29c32bdcVariant2(Solo48):
    icon_id = 'lab-flask-experiment-29c32bdc-v2'
    variant_of = 'lab-flask-experiment-29c32bdc'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'flask', 'experiment', 'science')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'flask',(16,4),('L',(32,4)),('L',(32,12)),('C',(34,18),(40,34),(40,38)),('L',(40,40)),('A',4,4,True,(36,44)),('L',(12,44)),('A',4,4,True,(8,40)),('L',(8,38)),('C',(8,34),(14,18),(16,12)),('L',(16,4)),closed=True)
        line(self,'collar',(16,12),(32,12))
        contacts(self)
