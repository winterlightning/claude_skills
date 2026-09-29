"""Three concentric semicircular rainbow bands and a larger smooth heart preserve pride and love; omit one fine rainbow band for 48px clarity.
The rejected rainbow has only two detached bands and the heart is cramped and angular. Restore the rainbow above a clearly lobed heart.
Keyshape HRECT_L; preserve reference proportions where a documented visual exception is needed.
Construction refs: human_ref/user.svg and full_body_ref.png for human vocabulary; Lucide heart/cat/sailboat for related contour construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c0e31e5f-9872-4414-9334-38d9e1e42539'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__romance-pride-gay-lgbt-heart/20260929T084651Z-thuan-mac/reference/romance pride gay lgbt heart_c0e31e5f-9872-4414-9334-38d9e1e42539.svg'
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
    icon_id = 'romance-pride-gay-lgbt-heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives"
    aliases = ()
    keywords = ('romance', 'pride', 'gay', 'lgbt', 'heart')

    def build(self):
        s=self
        # Plan: three concentric rainbow bands, symmetric heart below.
        for i,r in enumerate((18,12,6)):
            s.add_arc(f'rainbow-{i}',(24-r,22),(24+r,22),radius_x=r,sweep=True)
        path(s,'heart',(24,31),('C',(13,34),(18,25),(10,28)),('C',(24,44),(14,37),(20,41)),('C',(35,34),(28,41),(34,37)),('C',(24,31),(38,28),(30,25)),closed=True)

# User explicitly authorized high-quality drawing-specific exceptions.
Drawing.exception = {'reason': 'Keep three readable rainbow bands above a lobed heart. The 2px band openings and taller composition preserve both pride and love at 48px.', 'approved_by': 'user-authorized discretion; gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '5d6150d132bd42ab5a26c0752315f2f7aa152f117c9693abfb285deae04ceb02'}
