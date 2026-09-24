"A bareheaded courier rides a scooter with a rear parcel. Square extremes 6..42. Shared radius 3 circles for head and wheels; neck exactly 8 below head outline. Source supplies seated rider, rear box and scooter. Human full_body_ref supplies circular head and bent limbs; Lucide bike supplies simplified two-wheel scene. Omit headlamp and body panels. Parcel stays physical cargo, not a badge.\n\nEditorial reference brief:\n# Bareheaded Delivery Rider on Scooter\n\n- source: `pictographic-primitives/_uncategorized_14/delivery person motorcycle 1_9046ec78-1a6b-4029-a2e9-be0d10843436.svg`\n- render: `png/delivery person motorcycle 1_9046ec78-1a6b-4029-a2e9-be0d10843436.png` (look at this first)\n- native 48px: `png/delivery person motorcycle 1_9046ec78-1a6b-4029-a2e9-be0d10843436@48.png`\n- tags: delivery, rider, scooter, parcel, courier, transport, vehicle\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `bareheaded-delivery-rider-on-scooter`\n\n- source UUID: `9046ec78-1a6b-4029-a2e9-be0d10843436`\n\n## Description\n\nA round headed rider sits upright on a right facing scooter, with a bent leg reaching toward the footboard. A square parcel sits behind, and a small front fitting projects above the wheel.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '9046ec78-1a6b-4029-a2e9-be0d10843436'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/delivery person motorcycle 1_9046ec78-1a6b-4029-a2e9-be0d10843436.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'bareheaded-delivery-rider-on-scooter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ['Delivery Rider on Scooter']
    keywords = ['bareheaded', 'delivery', 'rider', 'on', 'scooter']

    def build(self):
        for name,cx,cy in [("head",24,9),("rear-wheel",9,39),("front-wheel",39,39)]:
            self.add_arc(name+"-a",(cx-3,cy),(cx+3,cy),radius_x=3)
            self.add_arc(name+"-b",(cx+3,cy),(cx-3,cy),radius_x=3)
            self.add_contour(name,name+"-a",name+"-b",closed=True)
        self.add_polyline("parcel", (6,16),(14,16),(14,24),(6,24),closed=True)
        neck=(24,20)
        hip=(24,28)
        self.add_line("torso",neck,hip)
        self.add_polyline("arm",neck,(32,20),(38,20))
        self.add_polyline("leg",hip,(30,28),(30,31))
        self.add_polyline("chassis",(12,39),(24,39),(36,39))
        self.add_polyline("front-fork",(39,36),(39,28),(38,20))
        self.relate("connect","torso","arm")
        self.relate("connect","torso","leg")
        self.relate("connect","chassis","rear-wheel")
        self.relate("connect","chassis","front-wheel")
        self.relate("connect","front-fork","front-wheel")
        self.relate("connect","front-fork","arm")
        self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")
