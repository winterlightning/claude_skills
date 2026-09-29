"""Added a tapered snout, eye, open angular mouth and rear crest to a smooth S-shaped neck.
The rejected head is a blocky question mark with no eye, mouth or crest. Restore the sea-dragon face and curved neck.
Keyshape SQUARE; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd6e9efaa-5911-4b52-b4b0-7f1573743591'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sea-serpent-head/20260929T084651Z-thuan-mac/reference/fantasy leviathan sea snake_d6e9efaa-5911-4b52-b4b0-7f1573743591.svg'
AUTHOR = 'gpt-6'

def path(s, name, start, *steps, closed=False):
    members=[]; here=start
    for i, step in enumerate(steps):
        kind, end, *p = step
        ident=f'{name}-{i}'
        if kind == 'L': s.add_line(ident, here, end)
        elif kind == 'A': s.add_arc(ident, here, end, radius_x=p[0], radius_y=p[1], sweep=p[2])
        elif kind == 'C': s.add_bezier(ident, here, (p[0], p[1], end))
        members.append(ident); here=end
    s.add_contour(name, *members, closed=closed)

def circle(s, name, x, y, r):
    path(s,name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

class Drawing(Solo48):
    icon_id = 'sea-serpent-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('fantasy', 'leviathan', 'sea', 'snake')

    def build(self):
        s=self
        # Plan: dragon snout, eye and zigzag mouth; clean crest without crowded subdivisions.
        path(s,'profile',(16,44),('C',(28,29),(16,36),(21,33)),('C',(28,20),(34,25),(32,20)),('L',(24,20)),('C',(18,26),(24,25),(22,26)),('L',(7,26)),('A',(4,23),3,3,True),('L',(4,16)),('A',(8,12),4,4,True),('L',(14,12)),('C',(25,9),(18,7),(20,9)),('C',(40,22),(34,8),(40,15)),('C',(33,36),(42,29),(37,33)),('C',(27,44),(29,39),(27,41)))
        s.add_polyline('mouth',(4,22),(9,19),(14,22));s.relate('connect','mouth','profile')
        s.add_dot('eye',(19,15))
        path(s,'crest',(25,9),('C',(42,9),(30,0),(37,3)),('L',(44,18)),('L',(40,20)));s.relate('connect','crest','profile')

# User explicitly authorized high-quality drawing-specific exceptions.
Drawing.exception = {'reason': 'Keep the dragon eye, angular mouth and crest on a smooth sea-serpent neck. Compact face and crest spacing preserves identity at native size.', 'approved_by': 'user-authorized discretion; gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '1999e9493e5e2f8221f320478162d609d34d412fbb559eac8fc1cbc72574187e'}
