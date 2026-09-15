'speaker: independent smooth-curve repair.\n\nConstruction: Speaker driver with a circular ring and four compact mounting tabs; smooth circular cone.\nKeyshape: SQUARE; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/speaker.svg and atomic-debug/speaker.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '81d4c431-5d96-51d5-9f0d-22d192c29508'
SOURCE_PATH = 'pictographic-primitives/audio/speaker_81d4c431-5d96-51d5-9f0d-22d192c29508.svg'
AUTHOR = 'gpt-6'


class Speaker(Solo48):
    icon_id = 'speaker'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('speaker', 'audio')
    keyshape = Keyshape.SQUARE

    def build(self):
        def rotate(p,turn):
            x,y=p
            for _ in range(turn): x,y=48-y,x
            return x,y
        quarter=[('C',(27,10),(29,10),(31,11)),('L',(36,6)),('A',6,6,True,(42,12)),('L',(37,17)),('C',(38,19),(38,21),(38,24))]
        commands=[]
        for turn in range(4):
            for cmd in quarter:
                commands.append(tuple([cmd[0]]+[rotate(p,turn) if isinstance(p,tuple) else p for p in cmd[1:]]))
        path(self,'outer',(24,10),*commands,closed=True)
        ellipse(self,'cone',24,24,5)
        contacts(self)
