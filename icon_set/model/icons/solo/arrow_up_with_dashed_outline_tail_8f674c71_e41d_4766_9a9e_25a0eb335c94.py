"A broad upward outline arrow has a broken two-sided tail. VRECT_L x8..40 y4..44 gives room for the dashed progression. All paired marks derive from axis24 and shaft halfwidth6; tails have a short dash and terminal dot, separated by 8 centerline units. Source supplies outlined head and dashed/dotted tail. Lucide arrow-big-down supplies shoulder construction, reflected vertically for up. Reduce many tiny tail marks to one dash and one dot per side.\n\nEditorial reference brief:\n# Arrow Up with Dashed Outline Tail\n\n- source: `pictographic-primitives/_uncategorized_14/diagram arrow dash up 1_8f674c71-e41d-4766-9a9e-25a0eb335c94.svg`\n- render: `png/diagram arrow dash up 1_8f674c71-e41d-4766-9a9e-25a0eb335c94.png` (look at this first)\n- native 48px: `png/diagram arrow dash up 1_8f674c71-e41d-4766-9a9e-25a0eb335c94@48.png`\n- tags: arrow, up, outline, dashed, tail, direction, pointer\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `arrow-up-with-dashed-outline-tail`\n\n- source UUID: `8f674c71-e41d-4766-9a9e-25a0eb335c94`\n\n## Description\n\nA broad outlined arrow points straight upward, with a triangular head and two parallel shaft edges. The lower ends of the shaft break into short dashes and tiny separated dots.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '8f674c71-e41d-4766-9a9e-25a0eb335c94'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram arrow dash up 1_8f674c71-e41d-4766-9a9e-25a0eb335c94.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-up-with-dashed-outline-tail'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ['Dashed Upward Arrow']
    keywords = ['arrow', 'up', 'with', 'dashed', 'outline', 'tail']

    def build(self):
        axis=24
        left=[(18,26),(18,20),(8,20)]
        right=[(2*axis-x,y) for x,y in reversed(left)]
        self.add_polyline("arrow-outline",*left,(axis,4),*right)
        for side,x in [("left",18),("right",2*axis-18)]:
            self.add_line(side+"-dash",(x,34),(x,36))
            self.add_dot(side+"-dot",(x,44))
