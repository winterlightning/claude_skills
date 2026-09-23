"""A blank standing board with a horizontal tray and two legs.
Plan: Symmetric rounded top; continuous sides split at the tray junction; shared y30 tray.
Construction reference: rectangle-horizontal: matching top corner arcs and straight sides.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3ac51a01-49f8-4fab-833e-bfbdf004114a'
SOURCE_PATH = 'icon_set/work/todo-references/board 1_3ac51a01-49f8-4fab-833e-bfbdf004114a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'board-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('board', '1')
    # Bounds are supplied by the contract; geometry below is authored to them.
    planned_visible_bounds = Keyshape.HRECT_L.bounds_for(Profile.SOLO48)

    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, left, top, right, bottom, radius=4):
        r = radius
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members = []
        for i, start in enumerate(points):
            end = points[(i+1)%8]
            part = f'{name}-{i}'
            if i%2:
                self.add_arc(part,start,end,radius_x=r)
            else:
                self.add_line(part,start,end)
            members.append(part)
        self.add_contour(name,*members,closed=True)

    def build(self):
        self.add_line('left-leg',(8,40),(8,30))
        self.add_line('left-wall',(8,30),(8,12))
        self.add_arc('tl',(8,12),(12,8),radius_x=4)
        self.add_line('top',(12,8),(36,8))
        self.add_arc('tr',(36,8),(40,12),radius_x=4)
        self.add_line('right-wall',(40,12),(40,30))
        self.add_line('right-leg',(40,30),(40,40))
        self.add_contour('board','left-leg','left-wall','tl','top','tr','right-wall','right-leg')
        for i,(a,b) in enumerate([(4,8),(8,40),(40,44)]):
            self.add_line(f'tray-{i}',(a,30),(b,30))
        for side,ids in [('left',(0,1)),('right',(1,2))]:
            for part in ('wall','leg'):
                for i in ids:
                    self.relate('connect',f'{side}-{part}',f'tray-{i}')
