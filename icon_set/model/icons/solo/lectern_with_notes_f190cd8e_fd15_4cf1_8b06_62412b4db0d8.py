"""A lectern holds marked notes beside a curved microphone."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='f190cd8e-fd15-4cf1-8b06-62412b4db0d8'
SOURCE_PATH='pictographic-primitives/office/presentation desk notes_f190cd8e-fd15-4cf1-8b06-62412b4db0d8.svg'
AUTHOR='gpt-6'

class LecternWithNotes(Solo48):
    icon_id='lectern-with-notes'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('lectern', 'notes', 'microphone', 'presentation', 'podium', 'office')

    def build(self):
        # Centerline extremes (4,8)-(44,40).
        # Reduction: Raise the note sheet for legibility; two text lines become one mark, and the microphone head becomes its rounded tip.
        # Reference: Lucide mic: coherent microphone stem; presentation: board and pedestal.
        # All contacts below are physical joints sharing exact endpoints.
        endpoints = {}
        def line(name, a, b):
            self.add_line(name, a, b)
            endpoints[name] = (a, b)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
            endpoints[name] = tuple(points)
        def arc(name, a, b, r, ry=None, sweep=True):
            self.add_arc(name, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)
            endpoints[name] = (a, b)
        def join_contacts():
            names = list(endpoints)
            for i, a in enumerate(names):
                for b in names[i+1:]:
                    if set(endpoints[a]) & set(endpoints[b]):
                        self.relate("connect", a, b)
        def circle(name,cx,cy,r):
            arc(name+'-top',(cx-r,cy),(cx,cy-r),r)
            arc(name+'-right',(cx,cy-r),(cx+r,cy),r)
            arc(name+'-bottom',(cx+r,cy),(cx,cy+r),r)
            arc(name+'-left',(cx,cy+r),(cx-r,cy),r)
            self.add_contour(name,*(name+s for s in ['-top','-right','-bottom','-left']),closed=True)
        # Plan: sloped tabletop, upright note sheet, tangent microphone and center pedestal.
        axis=24
        path('surface',(8,24),(axis,24),(40,24),(44,32),(axis,32),(4,32),closed=True)
        path('notes',(axis,24),(axis,8),(40,8),(40,24))
        self.add_dot('note-mark',(32,16))
        line('mic-stem',(8,24),(8,16))
        arc('mic-neck',(8,16),(16,8),8)
        line('pedestal',(axis,32),(axis,40))
        join_contacts()
