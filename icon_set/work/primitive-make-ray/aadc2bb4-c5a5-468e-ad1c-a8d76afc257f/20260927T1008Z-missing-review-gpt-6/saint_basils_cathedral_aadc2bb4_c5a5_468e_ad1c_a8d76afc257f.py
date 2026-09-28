"""Saint Basil’s Cathedral reduced to one mirrored skyline of three pointed onion domes and a broad base.
A continuous contour avoids the overlapping tower outlines in the rejected version. The source determines the towers; Lucide church informs the simple base.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'aadc2bb4-c5a5-468e-ad1c-a8d76afc257f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__saint-basils-cathedral/20260927T084430Z-thuan-mac-1/reference/saint basils cathderal_aadc2bb4-c5a5-468e-ad1c-a8d76afc257f.svg'
AUTHOR = "gpt-6"

class Landmark(Solo48):
    icon_id = 'saint-basils-cathedral'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    categories = ('landmarks', 'primitives')
    aliases = ()
    keywords = ('saint basil', 'moscow', 'russia', 'cathedral', 'onion dome', 'landmark', 'church', 'religion')

    def build(self):
        # A single mirrored skyline retains the three onion domes without
        # overlapping separate tower contours. Lucide church guides the base.
        self.add_line('left-wall',(8,44),(8,24))
        self.add_bezier('left-dome-up',(8,24),((8,21),(11,20),(12,16)))
        self.add_bezier('left-dome-down',(12,16),((14,20),(17,26),(18,31)))
        self.add_bezier('center-up',(18,31),((18,20),(22,10),(24,4)))
        self.add_bezier('center-down',(24,4),((26,10),(30,20),(30,31)))
        self.add_bezier('right-dome-up',(30,31),((31,26),(34,20),(36,16)))
        self.add_bezier('right-dome-down',(36,16),((37,20),(40,21),(40,24)))
        self.add_line('right-wall',(40,24),(40,44))
        self.add_line('base',(40,44),(8,44))
        self.add_contour('cathedral','left-wall','left-dome-up','left-dome-down','center-up','center-down','right-dome-up','right-dome-down','right-wall','base',closed=True)
