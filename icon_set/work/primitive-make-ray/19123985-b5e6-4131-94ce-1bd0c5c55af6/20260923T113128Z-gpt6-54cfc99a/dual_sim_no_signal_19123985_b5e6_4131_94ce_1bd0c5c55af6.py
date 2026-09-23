"""A SIM card beside two short signal bars.
Construction reference: card-sim: clipped corner, rounded outer shell and inset chip.
Reduction: No defining features omitted.
Keyshape: HRECT_L; geometry authored directly on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '19123985-b5e6-4131-94ce-1bd0c5c55af6'
SOURCE_PATH = 'icon_set/work/todo-references/dual sim no signal_19123985-b5e6-4131-94ce-1bd0c5c55af6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'dual-sim-no-signal'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('dual', 'sim', 'no', 'signal')

    def path(self, name, start, segments, closed=False):
        members = []
        for i, spec in enumerate(segments):
            part = f"{name}-{i+1}"
            if len(spec) == 2:
                end = spec
                self.add_line(part, start, end)
            else:
                end, rx, ry, sweep = spec
                self.add_arc(part, start, end, radius_x=rx, radius_y=ry, sweep=sweep)
            members.append(part)
            start = end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, x, y, r):
        self.path(name, (x-r,y), [((x+r,y),r,r,True),((x-r,y),r,r,True)], True)

    def rect(self, name, x, y, w, h, r=3):
        self.path(name, (x+r,y), [(x+w-r,y),((x+w,y+r),r,r,True),(x+w,y+h-r),((x+w-r,y+h),r,r,True),(x+r,y+h),((x,y+h-r),r,r,True),(x,y+r),((x+r,y),r,r,True)], True)

    def build(self):
        # Plan: clipped card left; rectangular chip inside; two separate signal runs right.
        self.path('card',(8,8),[(22,8),(30,16),(30,36),((26,40),4,4,True),(8,40),((4,36),4,4,True),(4,12),((8,8),4,4,True)],True)
        self.rect('chip',13,22,8,9,2)
        self.add_line('signal-long',(38,26),(44,26))
        self.add_line('signal-short',(38,36),(40,36))
