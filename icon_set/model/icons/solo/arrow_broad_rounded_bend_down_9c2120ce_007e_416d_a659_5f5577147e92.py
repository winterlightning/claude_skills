"A broad outlined arrow bends right and then down. Square 6..42 fits bend and broad triangular tip. One open contour, concentric-style elbow with roomy inner turn. Source supplies open left tail, outlined bend and point; Lucide arrow-big-down supplies shoulder-to-tip contour principle. Omit no identity features.\n\nEditorial reference brief:\n# Arrow Broad Rounded Bend Down\n\n- source: `pictographic-primitives/_uncategorized_14/diagram arrow bend down_9c2120ce-007e-416d-a659-5f5577147e92.svg`\n- render: `png/diagram arrow bend down_9c2120ce-007e-416d-a659-5f5577147e92.png` (look at this first)\n- native 48px: `png/diagram arrow bend down_9c2120ce-007e-416d-a659-5f5577147e92@48.png`\n- tags: arrow, down, bend, curve, outline, direction, pointer\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `arrow-broad-rounded-bend-down`\n\n- source UUID: `9c2120ce-007e-416d-a659-5f5577147e92`\n\n## Description\n\nA broad outlined arrow travels right from an open left end, curves smoothly downward, and ends in a triangular head. Parallel inner and outer curves define the rounded elbow.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '9c2120ce-007e-416d-a659-5f5577147e92'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram arrow bend down_9c2120ce-007e-416d-a659-5f5577147e92.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-broad-rounded-bend-down'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Downward Bending Arrow']
    keywords = ['arrow', 'broad', 'rounded', 'bend', 'down']

    def build(self):
        self.add_line("outer-top",(6,6),(24,6))
        self.add_arc("outer-elbow",(24,6),(36,18),radius_x=12)
        nodes=[(36,18),(36,28),(42,28),(30,42),(18,28),(24,28),(24,22)]
        for j,(a,b) in enumerate(zip(nodes,nodes[1:]),1):
            self.add_line(f"point-{j}",a,b)
        self.add_arc("inner-elbow",(24,22),(16,14),radius_x=8,sweep=False)
        self.add_line("inner-top",(16,14),(6,14))
        self.add_contour("bent-arrow","outer-top","outer-elbow",*[f"point-{j}" for j in range(1,7)],"inner-elbow","inner-top")
