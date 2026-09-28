"""Fresh SOLO48 revision of howling-wolf from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '02bbed8d-19bf-42c9-9539-d93fbda86791'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__howling-wolf/20260927T061852Z-thuan-mac-1/reference/wolf body howl_02bbed8d-19bf-42c9-9539-d93fbda86791.svg'
AUTHOR = "gpt-6"

class HowlingWolf(Solo48):
    icon_id = 'howling-wolf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('wolf', 'howl', 'standing', 'moon', 'wild', 'canine', 'night', 'wilderness')

    def build(self) -> None:

        poly(self,'body',(8,42),(12,32),(20,28),(23,17),(29,14),(32,8),
             (37,6),(42,8),(39,12),(36,12),(39,17),(36,25),(39,34),
             (39,42),(31,42),(31,32),(24,32),(24,42),(16,42),closed=True)
        line(self,'tail',(12,32),(6,39))
        contacts(self)
