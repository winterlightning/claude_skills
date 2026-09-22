"A broad down arrow begins beneath a separate horizontal bar. Square extremes 6..42 retain broad bar and centered point. Mirror the two shaft sides and shoulders about x=24; separate bar is intrinsic arrow notation. Source supplies open-top shaft with flanges and separate bar; Lucide arrow-big-down supplies continuous shoulder/point contour. No omitted identity features.\n\nEditorial reference brief:\n# Arrow Down Beneath Separate Top Bar\n\n- source: `pictographic-primitives/_uncategorized_14/diagram arrow dash down_97505a77-9794-4383-8806-61bbb128d83e.svg`\n- render: `png/diagram arrow dash down_97505a77-9794-4383-8806-61bbb128d83e.png` (look at this first)\n- native 48px: `png/diagram arrow dash down_97505a77-9794-4383-8806-61bbb128d83e@48.png`\n- tags: arrow, down, bar, outline, direction, shaft, pointer\n- family: solo — author with `$icon-solo`\n- proposed icon_id: `arrow-down-beneath-separate-top-bar`\n\n- source UUID: `97505a77-9794-4383-8806-61bbb128d83e`\n\n## Description\n\nA broad downward arrow has an outlined vertical shaft and a triangular point below. Its upper sides extend outward horizontally, with a separate long horizontal bar positioned above the open top.\n\n## To author\n\nRun `$icon-solo`, which reads `icon_set/skills/icon-design/SKILL.md`, then the reference-backed\nintake. Look at the render before choosing anything: name the subject in\none sentence, keep only what survives at native size, choose the keyshape,\nand design backwards from its four extreme coordinates.\n\nThe reference sets the subject, not the grid, the stroke or the\nproportions. Fit the result to the requested profile.\n\nYou can try modifying a copy of the SVG reference to fit the icon design rules,\nor generate a new icon that matches the icon name. Either approach must follow\nthe requested family's design rules and preserve the named subject's identity.\nKeep the original reference unchanged and produce the family skill's required deliverables.\n\n## Fit the icon design rules\n\nThis reference is drawn at illustration scale — thin strokes and more\ndetail than a 48px canvas can hold. Adapt or regenerate it to fit:\nfewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on\nthe grid. Keep the meaning intact — the silhouette it is recognized by and\nthe parts that make it this subject and not a neighbouring one. Simplify\nthe drawing, never the meaning."
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '97505a77-9794-4383-8806-61bbb128d83e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram arrow dash down_97505a77-9794-4383-8806-61bbb128d83e.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-down-beneath-separate-top-bar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ['Downward Arrow with Top Bar']
    keywords = ['arrow', 'down', 'beneath', 'separate', 'top', 'bar']

    def build(self):
        axis=24
        self.add_line("top-bar",(6,6),(42,6))
        left=[(6,14),(18,14),(18,26),(6,26)]
        tip=(axis,42)
        right=[(2*axis-x,y) for x,y in reversed(left)]
        self.add_polyline("arrow",*left,tip,*right)
