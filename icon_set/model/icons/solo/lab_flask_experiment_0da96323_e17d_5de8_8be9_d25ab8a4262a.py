'lab-flask-experiment: independent smooth-curve repair.\n\nConstruction: Conical flask: shared neck width, symmetric shoulders, rounded base and a wide liquid band.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/flask-conical.svg and atomic-debug/flask-conical.svg (geometric construction).\nOriginal source and parent geometry preserved.'
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
        path(self,'flask',(18,4),('L',(30,4)),('L',(30,17)),('L',(36,28)),('C',(38,31.666666667),(40,33),(40,36)),('A',8,8,True,(32,44)),('L',(16,44)),('A',8,8,True,(8,36)),('C',(8,33),(10,31.666666667),(12,28)),('L',(18,17)),('L',(18,4)),closed=True)
        line(self,'liquid',(12,28),(36,28))
        contacts(self)
