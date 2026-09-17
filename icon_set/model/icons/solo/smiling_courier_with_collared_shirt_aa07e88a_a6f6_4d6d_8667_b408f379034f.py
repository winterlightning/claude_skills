from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa07e88a-a6f6-4d6d-8667-b408f379034f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/delivery/delivery man_aa07e88a-a6f6-4d6d-8667-b408f379034f.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'smiling-courier-with-collared-shirt'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/people"
    aliases = ()
    keywords = ('courier', 'delivery', 'person', 'smile', 'cap', 'uniform', 'collar', 'worker')
    human_construction = "bust"

    def build(self):
        # Plan: courier cap, circular smiling jaw and touching rounded shoulders; symmetric bust.
        # Centerline extremes: (6,6)-(42,42). Construction: human_ref/user.svg for shoulders and circular head; original cap and smile.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        axis = 24  # Cap, jaw, collar and shoulders share this symmetry axis.
        # Shared human reference: circular jaw r12; bottom 28 and shoulder apex 32 give 0u ink gap.
        path('cap',(-12+axis,16),(-8+axis,6),(8+axis,6),(12+axis,16))
        self.add_arc('jaw',(12+axis,16),(-12+axis,16),radius_x=12);join('cap','jaw')
        self.add_line('brim-left',(-16+axis,16),(-12+axis,16));self.add_line('brim-right',(12+axis,16),(16+axis,16))
        for p in ('brim-left','brim-right'):join('cap',p);join('jaw',p)
        self.add_arc('smile',(3+axis,16),(-3+axis,16),radius_x=3)
        self.add_arc('shoulder-left',(-18+axis,42),(-8+axis,34),radius_x=10,radius_y=8)
        self.add_arc('neckline',(-8+axis,34),(8+axis,34),radius_x=8,radius_y=2)
        self.add_arc('shoulder-right',(8+axis,34),(18+axis,42),radius_x=10,radius_y=8)
        self.add_contour('shoulders','shoulder-left','neckline','shoulder-right')
        join('jaw','shoulders')
        path('collar',(-8+axis,34),(0+axis,42),(8+axis,34));join('collar','shoulders')
