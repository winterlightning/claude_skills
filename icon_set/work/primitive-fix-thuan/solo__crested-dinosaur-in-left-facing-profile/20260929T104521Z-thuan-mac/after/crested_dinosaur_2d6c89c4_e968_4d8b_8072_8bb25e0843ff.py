"""A left-facing crested dinosaur with a rounded muzzle and bent hind leg.

Plan: SQUARE centerline extremes (6,6)-(42,42). One coherent animal
outline owns muzzle, neck, back, tail and hind leg; a swept crest and short
forelimb attach at explicit shared nodes. Left-facing asymmetry is intentional.
Lucide rabbit informs smooth animal contours; the original supplies anatomy.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2d6c89c4-e968-4d8b-8072-8bb25e0843ff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crested-dinosaur-in-left-facing-profile/20260929T104521Z-thuan-mac/reference/dinosaur raptor 2_2d6c89c4-e968-4d8b-8072-8bb25e0843ff.svg'
AUTHOR = 'gpt-6'


class CrestedDinosaur(Solo48):
    icon_id = 'crested-dinosaur-in-left-facing-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ('crested-dinosaur',)
    keywords = ('dinosaur', 'crest', 'prehistoric', 'tail', 'profile')

    def build(self):
        self.add_bezier('muzzle-top', (6,18), ((6,16),(12,14),(16,13)))
        self.add_bezier('neck-back', (16,13), ((22,14),(20,23),(24,23)))
        self.add_bezier('back-tail', (24,23), ((30,19),(35,24),(37,28)), ((39,31),(40,31),(42,31)))
        self.add_bezier('tail-under', (42,31), ((40,35),(36,35),(33,33)))
        self.add_line('shin', (33,33), (33,36))
        self.add_bezier('foot', (33,36), ((39,41),(33,42),(27,42)))
        self.add_bezier('knee', (27,42), ((23,42),(22,40),(26,35)))
        self.add_bezier('belly', (26,35), ((21,35),(18,32),(16,29)))
        self.add_bezier('throat', (16,29), ((14,26),(14,24),(14,23)))
        self.add_line('muzzle-bottom', (14,23), (10,23))
        self.add_bezier('nose', (10,23), ((7,23),(6,21),(6,18)))
        self.add_contour('animal', 'muzzle-top','neck-back','back-tail','tail-under','shin','foot','knee','belly','throat','muzzle-bottom','nose',closed=True)
        self.add_bezier('crest', (16,13), ((20,8),(22,6),(26,6)))
        self.relate('connect','crest','animal')
        self.add_bezier('forelimb', (16,29), ((12,35),(10,30),(8,34)))
        self.relate('connect','forelimb','animal')
