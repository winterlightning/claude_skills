"A capped courier rides a scooter carrying a rear box. Square 6..42 preserves equipment proportions. Head and wheels share radius 3; exact head gap 8. Cap visor attaches at head rightmost endpoint. Human full_body_ref and Lucide bike teach circular head and minimal bent limbs. Source supplies right-facing scooter, cap and rear parcel. Omit body panels and internal cap seam; retain projecting visor.\n\nEditorial reference brief:\n# Capped Delivery Rider on Scooter\n\n- source: `pictographic-primitives/_uncategorized_14/delivery person motorcycle_54079a5b-25ea-4346-8fc4-d2b5f8239da0.svg`\n- render: `png/delivery person motorcycle_54079a5b-25ea-4346-8fc4-d2b5f8239da0.png` (look at this first)\n- native 48px: `png/delivery person motorcycle_54079a5b-25ea-4346-8fc4-d2b5f8239da0@48.png`\n- tags: delivery, rider, scooter, cap, box, transport, courier\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `capped-delivery-rider-on-scooter`\n\n- source UUID: `54079a5b-25ea-4346-8fc4-d2b5f8239da0`\n\n## Description\n\nA capped rider sits on a right facing scooter with arms reaching toward the handlebar. A square delivery box rests behind the rider above the rear body, between two large round wheels.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '54079a5b-25ea-4346-8fc4-d2b5f8239da0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/delivery person motorcycle_54079a5b-25ea-4346-8fc4-d2b5f8239da0.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'capped-delivery-rider-on-scooter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ['Delivery Person on Scooter']
    keywords = ['capped', 'delivery', 'rider', 'on', 'scooter']

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
        self.add_line("cap-brim",(27,9),(32,9))
        self.relate("connect","head","cap-brim")
