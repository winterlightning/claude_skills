"A diagonal sports dart points lower left with two tail flights upper right. Square 6..42 fits the diagonal equipment. Flights mirror about x+y=48; shared diagonal seam and shaft own real attachment nodes. Source supplies orientation and two fins. No useful Lucide dart match. Omit barrel grip texture and outline thickness to retain clean shaft and two flights.\n\nEditorial reference brief:\n# Dart with Two Visible Tail Flights\n\n- source: `pictographic-primitives/_uncategorized_14/dart_f95af12b-a19b-4e5a-a6ec-10d5dae17560.svg`\n- render: `png/dart_f95af12b-a19b-4e5a-a6ec-10d5dae17560.png` (look at this first)\n- native 48px: `png/dart_f95af12b-a19b-4e5a-a6ec-10d5dae17560@48.png`\n- tags: dart, flights, barrel, tip, sport, game, equipment\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `dart-with-two-visible-tail-flights`\n\n- source UUID: `f95af12b-a19b-4e5a-a6ec-10d5dae17560`\n\n## Description\n\nA dart lies diagonally with its pointed tip at the lower left and broad tail flights at the upper right. A short thick barrel joins the tip to the slender shaft.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'f95af12b-a19b-4e5a-a6ec-10d5dae17560'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/dart_f95af12b-a19b-4e5a-a6ec-10d5dae17560.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'dart-with-two-visible-tail-flights'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ['Diagonal Sports Dart Arrow']
    keywords = ['dart', 'with', 'two', 'visible', 'tail', 'flights']

    def build(self):
        tip=(6,42)
        root=(22,26)
        seam=(36,12)
        self.add_line("shaft", tip, root)
        self.add_polyline("upper-flight", root, (22,14), (30,6), seam)
        self.add_polyline("lower-flight", seam, (42,18), (34,26), root)
        self.add_line("flight-seam", root, seam)
        self.relate("connect", "shaft", "upper-flight", "lower-flight", "flight-seam")
