"""Revision of the claimed reference after comparing original and rejected drawing."""
"""laptop skull, complete SOLO48 composition.
Symbol plan is recorded in build(). Visible keyshape extremes: (2, 6, 46, 42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '44a8272b-04c4-4a7c-b200-ee122a35ef32'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__laptop-skull/20260927T142529Z-thuan-mac-1/reference/laptop skull_44a8272b-04c4-4a7c-b200-ee122a35ef32.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'laptop-skull'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("combination", "other", "primitives-generate")
    aliases = ()
    keywords = ('laptop skull',)

    def rounded(self,n,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for i in range(8):
            a,b=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(n+str(i),a,b,radius_x=r)
            else:self.add_line(n+str(i),a,b)
        self.add_contour(n,*(n+str(i) for i in range(8)),closed=True)

    def laptop(self):
        # Screen and base own shared hinge endpoints; repeated corner radius 4.
        self.add_line('screen-left',(8,32),(8,12))
        self.add_arc('screen-tl',(8,12),(12,8),radius_x=4)
        self.add_line('screen-top',(12,8),(36,8))
        self.add_arc('screen-tr',(36,8),(40,12),radius_x=4)
        self.add_line('screen-right',(40,12),(40,32))
        self.add_line('hinge',(40,32),(8,32))
        self.add_contour('screen','screen-left','screen-tl','screen-top','screen-tr','screen-right','hinge',closed=True)
        self.add_polyline('base',(8,32),(4,40),(44,40),(40,32))
        self.relate('connect','screen','base')

    def build(self):
        # A wider skull sits above an open laptop base, preserving room for eye sockets.
        self.add_arc('cranium',(8,24),(40,24),radius_x=16,radius_y=16)
        self.add_polyline('jaw',(8,24),(16,31),(32,31),(40,24))
        self.relate('connect','cranium','jaw')
        for x in (19,29): self.add_dot('eye-'+str(x),(x,22))
        self.add_polyline('screen-left',(8,24),(8,32),(4,40))
        self.add_polyline('screen-right',(40,24),(40,32),(44,40))
        self.relate('connect','cranium','screen-left'); self.relate('connect','cranium','screen-right')
        self.relate('connect','jaw','screen-left'); self.relate('connect','jaw','screen-right')
        self.add_line('laptop-base',(4,40),(44,40))
        self.relate('connect','screen-left','laptop-base'); self.relate('connect','screen-right','laptop-base')


# Explicit user approval for this exact SVG; changes invalidate the exception.
