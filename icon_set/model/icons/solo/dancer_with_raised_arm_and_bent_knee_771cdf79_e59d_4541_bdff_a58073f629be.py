"A dancer balances with one raised arm and a lifted bent knee. Square extremes 6..42. Head radius 5, vertical upper torso, exact 8 centerline neck gap. Natural asymmetric pose. Human full_body_ref supplies circular head and round limbs; Lucide person-standing supplies branched shared joints. Source supplies raised right arm and lifted right knee. Omit outlined body bulk.\n\nEditorial reference brief:\n# Dancer with Raised Arm and Bent Knee\n\n- source: `pictographic-primitives/_uncategorized_14/dancer_771cdf79-e59d-4541-bdff-a58073f629be.svg`\n- render: `png/dancer_771cdf79-e59d-4541-bdff-a58073f629be.png` (look at this first)\n- native 48px: `png/dancer_771cdf79-e59d-4541-bdff-a58073f629be@48.png`\n- tags: dancer, dancing, person, pose, movement, arm, knee\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `dancer-with-raised-arm-and-bent-knee`\n\n- source UUID: `771cdf79-e59d-4541-bdff-a58073f629be`\n\n## Description\n\nA round headed figure balances on one extended leg while lifting the other knee. One arm reaches sideways to the left, and the opposite arm curves upward over the shoulder.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '771cdf79-e59d-4541-bdff-a58073f629be'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/dancer_771cdf79-e59d-4541-bdff-a58073f629be.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'dancer-with-raised-arm-and-bent-knee'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ['Dancing Person Figure']
    keywords = ['dancer', 'with', 'raised', 'arm', 'and', 'bent', 'knee']

    def build(self):
        self.add_arc("head-top", (19,11), (29,11), radius_x=5)
        self.add_arc("head-bottom", (29,11), (19,11), radius_x=5)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        neck=(24,24)
        hip=(24,32)
        self.add_line("torso", neck, hip)
        self.add_line("left-arm", (6,26), neck)
        self.add_line("raised-arm-start", neck, (34,24))
        self.add_bezier("raised-arm-end", (34,24), ((40,24),(42,18),(42,6)))
        self.add_contour("raised-arm", "raised-arm-start", "raised-arm-end")
        self.add_line("standing-leg", hip, (16,42))
        self.add_polyline("lifted-leg", hip, (36,34), (32,42))
        self.relate("connect", "torso", "left-arm", "raised-arm")
        self.relate("connect", "torso", "standing-leg", "lifted-leg")
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
