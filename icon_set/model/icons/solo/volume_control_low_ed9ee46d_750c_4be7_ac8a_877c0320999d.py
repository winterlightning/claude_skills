'volume-control-low: independent smooth-curve repair.\n\nConstruction: Speaker profile with a rounded rear box and a flared cone; upper and lower sides mirror exactly.\nKeyshape: VRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/volume-2.svg and atomic-debug/volume-2.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'ed9ee46d-750c-4be7-ac8a-877c0320999d'
SOURCE_PATH = 'pictographic-primitives/audio/volume control low_ed9ee46d-750c-4be7-ac8a-877c0320999d.svg'
AUTHOR = 'gpt-6'


class VolumeControlLow(Solo48):
    icon_id = 'volume-control-low'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'low', 'audio')
    keyshape = Keyshape.VRECT_L

    def build(self):
        path(self,'speaker',(8,18),('L',(18,18)),('L',(35,5)),('C',(36,4),(36,4),(37,4)),('A',3,3,True,(40,7)),('L',(40,41)),('A',3,3,True,(37,44)),('C',(36,44),(36,44),(35,43)),('L',(18,30)),('L',(8,30)),('L',(8,18)),closed=True)
        line(self,'division',(18,18),(18,30))
        contacts(self)
