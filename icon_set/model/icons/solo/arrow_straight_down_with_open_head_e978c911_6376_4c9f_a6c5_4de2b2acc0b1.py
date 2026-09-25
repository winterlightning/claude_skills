"A vertical arrow points straight down with an open head. VRECT_M 10..38 x 4..44 emphasizes long shaft. Mirror head arms around x=24 and share the tip with the shaft. Source supplies long vertical stem; Lucide arrow-down supplies the common endpoint and mirrored diagonals. No omitted details.\n\nEditorial reference brief:\n# Arrow Straight Down with Open Head\n\n- source: `pictographic-primitives/_uncategorized_14/diagram arrow dash down 1_e978c911-6376-4c9f-a6c5-4de2b2acc0b1.svg`\n- render: `png/diagram arrow dash down 1_e978c911-6376-4c9f-a6c5-4de2b2acc0b1.png` (look at this first)\n- native 48px: `png/diagram arrow dash down 1_e978c911-6376-4c9f-a6c5-4de2b2acc0b1@48.png`\n- tags: arrow, down, vertical, line, direction, pointer, head\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `arrow-straight-down-with-open-head`\n\n- source UUID: `e978c911-6376-4c9f-a6c5-4de2b2acc0b1`\n\n## Description\n\nA single straight vertical shaft descends into a broad open arrowhead. Two diagonal arms extend upward from the bottom tip, creating a balanced downward pointer with no enclosing outline.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'e978c911-6376-4c9f-a6c5-4de2b2acc0b1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram arrow dash down 1_e978c911-6376-4c9f-a6c5-4de2b2acc0b1.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-straight-down-with-open-head'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ['Downward Pointing Arrow']
    keywords = ['arrow', 'straight', 'down', 'with', 'open', 'head']

    def build(self):
        axis=24
        tip=(axis,44)
        self.add_line("shaft",(axis,4),tip)
        self.add_polyline("head",(10,30),tip,(2*axis-10,30))
        self.relate("connect","shaft","head")
