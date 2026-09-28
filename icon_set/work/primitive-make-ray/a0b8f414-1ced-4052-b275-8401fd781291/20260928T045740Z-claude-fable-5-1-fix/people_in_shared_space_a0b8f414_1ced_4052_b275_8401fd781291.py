"""Three people standing together under a shared dome (a shared spatial experience).

Plan: HRECT_L (4,8)-(44,40). A half-ellipse dome (rx20, ry8) spans the top from (4,16) to (44,16). Three busts stand under it, the middle one taller and forward: each is a dot head 9 above a rounded-shoulder body (r4 shoulder arc, straight sides, flat base at y=40) 8 wide, with 8 between neighbouring bodies. Body edges are standalone members joined by connect so the 8-unit gaps certify.
Review of the rejected drawing: the people were three dots with short stubs under an arch, which read as a face or an alien; the original shows three rounded figures with bodies under a dome.
Omissions: arms and the figures' leg split.
Human reference: icon_set/references/human_ref/user.svg (round head over rounded shoulders), reduced to dot heads at this scale.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a0b8f414-1ced-4052-b275-8401fd781291'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__people-in-shared-space/20260928T042731Z-thuan-mac-1/reference/share play spatial experience_a0b8f414-1ced-4052-b275-8401fd781291.svg'
AUTHOR = 'thuan-mac-1/claude-fable-5-1'


class PeopleInSharedSpace(Solo48):
    icon_id = 'people-in-shared-space'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    categories = ('other', 'primitives')
    aliases = ('shared-space', 'group-under-dome')
    keywords = ('people', 'shared', 'space', 'group', 'spatial', 'experience', 'dome', 'share', 'play')

    def build(self) -> None:
        self.add_arc('dome', (4, 16), (44, 16), radius_x=20, radius_y=8, sweep=True)
        for name, cx, top in (('left', 8, 33), ('middle', 24, 26), ('right', 40, 33)):
            self.add_dot(f'{name}-head', (cx, top - 9))
            # shoulders as two cardinal quarter arcs in their own contour; sides and base standalone
            self.add_arc(f'{name}-shoulder-left', (cx - 4, top + 4), (cx, top), radius_x=4, sweep=True)
            self.add_arc(f'{name}-shoulder-right', (cx, top), (cx + 4, top + 4), radius_x=4, sweep=True)
            self.add_contour(f'{name}-shoulders', f'{name}-shoulder-left', f'{name}-shoulder-right')
            self.add_line(f'{name}-side-left', (cx - 4, 40), (cx - 4, top + 4))
            self.add_line(f'{name}-side-right', (cx + 4, top + 4), (cx + 4, 40))
            self.add_line(f'{name}-base', (cx + 4, 40), (cx - 4, 40))
            members = [f'{name}-side-left', f'{name}-shoulders', f'{name}-side-right', f'{name}-base']
            for a, b in zip(members, members[1:] + members[:1]):
                self.relate('connect', a, b)
