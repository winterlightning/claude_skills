"""A clipped-corner dollar invoice with a currency mark and two payment rules.
Construction reference: file, dollar-sign: rounded document corners and a coherent S stroke.
Reduction: Dropped the shorter ancillary payment rule to preserve room around the dollar sign and longer rule.
Keyshape: VRECT_L; geometry authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce8e18cb-9215-42b4-8bc1-1f1fc2a0437d'
SOURCE_PATH = 'icon_set/work/todo-references/dollar bill_ce8e18cb-9215-42b4-8bc1-1f1fc2a0437d.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'dollar-bill'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
    aliases = ()
    keywords = ('dollar', 'bill')

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
        # Plan: clipped document; currency symbol above two rules.
        self.path('paper',(12,4),[(30,4),(40,14),(40,40),((36,44),4,4,True),(12,44),((8,40),4,4,True),(8,8),((12,4),4,4,True)],True)
        self.path('dollar',(28,14),[(24,14),((24,20),3,3,False),((24,26),3,3,True),(20,26)])
        self.add_line('dollar-top',(24,13),(24,14))
        self.add_line('dollar-bottom',(24,26),(24,27))
        self.relate('connect','dollar-top','dollar')
        self.relate('connect','dollar-bottom','dollar')
        self.add_line('rule-long',(17,35),(31,35))
