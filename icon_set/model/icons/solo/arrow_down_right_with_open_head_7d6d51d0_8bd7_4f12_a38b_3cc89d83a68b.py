"A straight arrow points diagonally down right. Square 6..42 follows the directional diagonal. Open head shares one endpoint with shaft; balanced horizontal and vertical arms derive from a common length. Source supplies long shaft and short head; Lucide arrow-down-right supplies the shared endpoint construction. No omitted details.\n\nEditorial reference brief:\n# Arrow Down Right with Open Head\n\n- source: `pictographic-primitives/_uncategorized_14/diagram arrow dash corner right down_7d6d51d0-8bd7-4f12-a38b-3cc89d83a68b.svg`\n- render: `png/diagram arrow dash corner right down_7d6d51d0-8bd7-4f12-a38b-3cc89d83a68b.png` (look at this first)\n- native 48px: `png/diagram arrow dash corner right down_7d6d51d0-8bd7-4f12-a38b-3cc89d83a68b@48.png`\n- tags: arrow, down, right, diagonal, direction, pointer, line\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `arrow-down-right-with-open-head`\n\n- source UUID: `7d6d51d0-8bd7-4f12-a38b-3cc89d83a68b`\n\n## Description\n\nA straight diagonal shaft descends from the upper left toward the lower right. Two perpendicular arms meet at its endpoint, forming an open arrowhead with a horizontal base and upright right edge.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '7d6d51d0-8bd7-4f12-a38b-3cc89d83a68b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram arrow dash corner right down_7d6d51d0-8bd7-4f12-a38b-3cc89d83a68b.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-down-right-with-open-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ['Arrow Pointing Down Right']
    keywords = ['arrow', 'down', 'right', 'with', 'open', 'head']

    def build(self):
        tip=(42,42)
        arm=18
        self.add_line("shaft",(6,6),tip)
        self.add_polyline("head",(42,42-arm),tip,(42-arm,42))
        self.relate("connect","shaft","head")
