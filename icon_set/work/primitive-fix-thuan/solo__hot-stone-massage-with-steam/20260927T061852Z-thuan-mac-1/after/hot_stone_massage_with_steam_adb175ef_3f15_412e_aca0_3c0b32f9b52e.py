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

        # Open stones above the resting body eliminate two tiny enclosed pockets.
        line(self,'body',(4,40),(27,40))
        ellipse(self,'head',40,36,4)
        path(self,'stone-left',(4,30),('A',4,4,True,(12,30)))
        path(self,'stone-right',(20,30),('A',4,4,True,(28,30)))
        for i,x in enumerate((8,22)):
            self.add_bezier(f'steam-{i}',(x,8),((x-5,11),(x+5,14),(x,17)))
        contacts(self)
