"""Raised symmetrical arms, circular head, central medal and a front-facing racing chair with three wheel axes and horizontal axle. Head bottom12 to torso20 gives exact 4px ink gap.
Reference comparison: The rejected racer replaced the central front wheel with running legs and omitted the medal and chair axle. The original shows a celebrating seated racer.
Construction references: human_ref/full_body_ref.png circular head and round-ended limbs; original controls raised-arm pose and chair.
Omissions: Outlined arms reduced to single strokes; retain medal and all three wheels.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ccdd0a46-c667-4e7a-8d4d-7666a4ba3ccd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__racer-raised-arms/20260929T042221Z-thuan-mac/reference/race_ccdd0a46-c667-4e7a-8d4d-7666a4ba3ccd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'racer-raised-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.circle('head',24,8,4)
        self.path('arms',(6,4),('L',(11,17)),('L',(24,22)),('L',(37,17)),('L',(42,4)))
        self.add_line('torso',(24,20),(24,23))
        self.circle('medal',24,27,3)
        # Front-facing racing chair: three wheel axes, not running legs.
        self.path('central-wheel',(21,36),('A',(27,36),3,3,True),('L',(27,42)),('A',(21,42),3,3,True),('L',(21,36)),closed=True)
        self.add_line('left-wheel',(12,33),(7,44));self.add_line('right-wheel',(36,33),(41,44))
        self.add_line('axle-left',(11,38),(21,38));self.add_line('axle-right',(27,38),(37,38))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

Drawing.exception = {'reason': 'Medal, chair wheels and axle need compact true overlaps and narrow wheel openings. User authorized meaning-preserving exception; head/torso spacing is retained exactly.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'a529b7b081cf693d1e04c3d7fe683503b885d61413fc9d760a73d6851cc041c0'}
