"""VRECT_XL (8,6)-(40,42) centerlines. Preserve three pointed onion domes, taller central tower and broad base. Replace tight upright shoulder notches with open diagonal shoulders. Mirrored radii and coordinates about x=24.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'aadc2bb4-c5a5-468e-ad1c-a8d76afc257f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__saint-basils-cathedral/20260927T084430Z-thuan-mac-1/reference/saint basils cathderal_aadc2bb4-c5a5-468e-ad1c-a8d76afc257f.svg'
AUTHOR = 'gpt-6'

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
        self.add_line('left-wall',(10,44),(10,30))
        self.add_bezier('left-shoulder',(10,30),((10,27),(8,27),(8,24)))
        self.add_bezier('left-dome-up',(8,24),((8,21),(11,20),(12,16)))
        self.add_bezier('left-dome-down',(12,16),((14,20),(17,26),(18,31)))
        self.add_bezier('center-up',(18,31),((18,20),(22,10),(24,4)))
        self.add_bezier('center-down',(24,4),((26,10),(30,20),(30,31)))
        self.add_bezier('right-dome-up',(30,31),((31,26),(34,20),(36,16)))
        self.add_bezier('right-dome-down',(36,16),((37,20),(40,21),(40,24)))
        self.add_bezier('right-shoulder',(40,24),((40,27),(38,27),(38,30)))
        self.add_line('right-wall',(38,30),(38,44))
        self.add_line('base',(38,44),(10,44))
        self.add_contour('cathedral','left-wall','left-shoulder','left-dome-up','left-dome-down','center-up','center-down','right-dome-up','right-dome-down','right-shoulder','right-wall','base',closed=True)
