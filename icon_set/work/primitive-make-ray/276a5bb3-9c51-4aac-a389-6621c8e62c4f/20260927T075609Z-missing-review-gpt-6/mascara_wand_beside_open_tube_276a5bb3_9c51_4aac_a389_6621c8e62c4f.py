"""Revision of mascara-wand-beside-open-tube. The rejected wand looked like a screwdriver. Redrew the applicator with three separated bristle rows and a shorter rounded handle beside the open tube.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""Mascara Wand beside Open Tube.

Symbol plan: Left wand with two repeated bristle bars, capsule handle; right removable tube. Drop the third bristle and seam for clearance.
VRECT_L centerline extremes (8,4)-(40,44); envelope follows the subject's proportions.
Construction reference: Lucide paint-roller: simple capsule ends and shared handle attachment.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '276a5bb3-9c51-4aac-a389-6621c8e62c4f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__mascara-wand-beside-open-tube/20260927T074149Z-thuan-mac-1/reference/mascara_276a5bb3-9c51-4aac-a389-6621c8e62c4f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'mascara-wand-beside-open-tube'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('mascara', 'wand', 'beside', 'open', 'tube')

    def build(self):
        def box(n,x,y,w,h,r):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            names=[]
            for i,(a,b) in enumerate(zip(pts,pts[1:]+pts[:1])):
                name=f'{n}-{i}'
                if i%2:self.add_arc(name,a,b,radius_x=r)
                else:self.add_line(name,a,b)
                names.append(name)
            self.add_contour(n,*names,closed=True)
        box('handle',8,31,12,13,5)
        self.add_line('shaft',(14,4),(14,31))
        self.relate('connect','shaft','handle')
        for i,y in enumerate((4,13,22)):
            self.add_line(f'bristle-{i}',(9,y),(19,y))
            self.relate('connect','shaft',f'bristle-{i}')
        box('tube',30,20,10,24,5)
