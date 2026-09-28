"""Fresh SOLO48 revision of hot-stone-massage-with-steam from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'adb175ef-3f15-412e-aca0-3c0b32f9b52e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hot-stone-massage-with-steam/20260927T061852Z-thuan-mac-1/reference/hot stone massage person_adb175ef-3f15-412e-aca0-3c0b32f9b52e.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'hot-stone-massage-with-steam'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('hot', 'stone', 'massage', 'with', 'steam')

    def build(self) -> None:

        # Low resting body, round head, stones and rising steam.
        line(self,'bed',(4,40),(32,40))
        ellipse(self,'head',40,36,4)
        path(self,'stone-left',(8,32),('A',5,4,True,(18,32)))
        path(self,'stone-right',(22,32),('A',5,4,True,(32,32)))
        for i,x in enumerate((13,27)):
            self.add_bezier(f'steam-{i}',(x,8),((x-5,14),(x+5,18),(x,24)))
        contacts(self)
