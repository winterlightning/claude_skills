"A two-rooted molar stands beside a hooked dental pick. Square 6..42 accommodates tool diagonal and upright tooth. Tooth owns a continuous broad crown and two roots; pick is separate physical equipment. Source supplies overlapping dental scene; no useful Lucide tooth match. Separate rather than overlap the pick and tooth; omit tool handle outline to retain spacing.\n\nEditorial reference brief:\n# Tooth Beside Bent Dental Stick\n\n- source: `pictographic-primitives/_uncategorized_14/dental stick tooth_5fba6994-83b3-4c8e-872d-6f2fc2d663b7.svg`\n- render: `png/dental stick tooth_5fba6994-83b3-4c8e-872d-6f2fc2d663b7.png` (look at this first)\n- native 48px: `png/dental stick tooth_5fba6994-83b3-4c8e-872d-6f2fc2d663b7@48.png`\n- tags: tooth, dental, stick, pick, teeth, hygiene, tool\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `tooth-beside-bent-dental-stick`\n\n- source UUID: `5fba6994-83b3-4c8e-872d-6f2fc2d663b7`\n\n## Description\n\nA broad two rooted tooth stands behind a long diagonal dental stick. The stick has a rounded lower end and a short hooked upper tip that bends back toward the tooth.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '5fba6994-83b3-4c8e-872d-6f2fc2d663b7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/dental stick tooth_5fba6994-83b3-4c8e-872d-6f2fc2d663b7.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'tooth-beside-bent-dental-stick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ['Tooth and Dental Pick']
    keywords = ['tooth', 'beside', 'bent', 'dental', 'stick']

    def build(self):
        self.add_bezier("crown-left",(30,8),((27,8),(27,6),(24,6)),((20,6),(18,10),(18,14)),((18,19),(21,21),(21,25)))
        self.add_bezier("roots",(21,25),((21,29),(21,34),(24,34)),((27,34),(27,24),(30,24)),((33,24),(33,34),(36,34)),((39,34),(39,29),(39,25)))
        self.add_bezier("crown-right",(39,25),((39,21),(42,19),(42,14)),((42,10),(40,6),(36,6)),((33,6),(33,8),(30,8)))
        self.add_contour("tooth","crown-left","roots","crown-right",closed=True)
        self.add_polyline("dental-pick",(10,12),(6,16),(6,26),(16,42))
