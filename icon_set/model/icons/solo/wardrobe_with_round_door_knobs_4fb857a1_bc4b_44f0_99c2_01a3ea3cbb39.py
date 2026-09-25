'Tall symmetric two-door wardrobe with paired knobs and feet. SQUARE supplies a broad cabinet body and 36-unit body width for two knobs with exact eight-unit separations. Shared x=24 axis, four-unit corner radii and eight-unit feet. Source supplies paired doors, knobs and feet; Lucide panels-top-left supplies joined frame/seam principle. Knobs reduced to round dots.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fb857a1-bc4b-44f0-99c2-01a3ea3cbb39'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/closet_4fb857a1-bc4b-44f0-99c2-01a3ea3cbb39.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'wardrobe-with-round-door-knobs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Wardrobe with Round Door Knobs',)
    keywords = ('wardrobe', 'cabinet', 'doors', 'knobs', 'furniture', 'storage', 'legs')
    def build(self):
        pts=[(10,6),(24,6),(38,6),(42,10),(42,30),(38,34),(24,34),(10,34),(6,30),(6,10)]
        corners={2,4,7,9}
        members=[]
        for i,p in enumerate(pts):
            name=f'frame-{i}'; q=pts[(i+1)%len(pts)]
            if i in corners: self.add_arc(name,p,q,radius_x=4,sweep=True)
            else: self.add_line(name,p,q)
            members.append(name)
        self.add_contour('body',*members,closed=True)
        self.add_line('seam',(24,6),(24,34))
        self.relate('connect','body','seam')
        for x in (10,38):
            name=f'foot-{x}'
            self.add_line(name,(x,34),(x,42))
            self.relate('connect',name,'body')
        for x in (16,32): self.add_dot(f'knob-{x}',(x,20))
