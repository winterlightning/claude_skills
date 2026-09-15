"""Round the three jellyfish bells to full semicircles and align their tentacle lengths, replacing the flattened caps with fuller domes.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c9bdc48d-a72f-41ce-9b7a-6a465d1111ed'
SOURCE_PATH = 'pictographic-primitives/animals/jellyfish group_c9bdc48d-a72f-41ce-9b7a-6a465d1111ed.svg'
AUTHOR = 'gpt-6'

class JellyfishGroup(Solo48):
    icon_id = 'jellyfish-group-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('jellyfish', 'group', 'three', 'swarm', 'sea', 'ocean', 'marine', 'bloom')

    def build(self) -> None:
        """Opening repair: Rebuilt three deeper bells and reduced each to two evenly spaced tentacles to avoid new crowding."""
        for index, (left, rim_y, ends) in enumerate(((6, 14, (6, 14)), (26, 27, (34, 42)), (6, 38, (6, 14)))):
            right = left + 16
            dome = f'bell-{index}-dome'
            rim = f'bell-{index}-rim'
            contour = f'bell-{index}'
            self.add_arc(dome, (left, rim_y), (right, rim_y), radius_x=8, radius_y=8)
            nodes = sorted(set((left, right) + ends), reverse=True)
            for j in range(1, len(nodes)):
                self.add_line(f'{rim}-{j}', (nodes[j - 1], rim_y), (nodes[j], rim_y))
            self.add_contour(contour, dome, *[f'{rim}-{j}' for j in range(1, len(nodes))], closed=True)
            end_y = (18, 31, 42)[index]
            for j, x in enumerate(ends):
                name = f'tentacle-{index}-{j}'
                self.add_line(name, (x, rim_y), (x, end_y))
                self.relate('connect', name, contour)
    variant_of = 'jellyfish-group'
    variant_label = 'Batch 01 centerline repair'
