"""A framed album with paired musical notes.

Symbol plan: music: circular noteheads and a single bent stem/beam contour.
Envelope: SQUARE. The complete composition has a square overall envelope and uses the (6,6)–(42,42) centerline extremes.
Reduction: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0c038416-c2a9-4ae0-ab80-a793e4a0b0c7'
SOURCE_PATH = 'icon_set/work/todo-references/playlist album_0c038416-c2a9-4ae0-ab80-a793e4a0b0c7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'playlist-album'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('playlist', 'album')
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.rounded('album',6,6,42,42,4)
        for name,cx,cy in [('note-left',17,31),('note-right',31,29)]:
            self.circle(name,cx,cy,2)
        self.add_polyline('music-stems',(19,31),(19,18),(33,15),(33,29))
        for note in ('note-left','note-right'): self.relate('connect',note,'music-stems')

    def circle(self, name, cx, cy, r):
        points = [(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members = []
        for i, (a,b) in enumerate(zip(points, points[1:])):
            member = f"{name}-{i}"
            self.add_arc(member, a, b, radius_x=r)
            members.append(member)
        self.add_contour(name, *members, closed=True)

    def rounded(self, name, left, top, right, bottom, r):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r),(left+r,top)]
        members = []
        for i,(a,b) in enumerate(zip(points,points[1:])):
            member = f"{name}-{i}"
            if i % 2: self.add_arc(member,a,b,radius_x=r)
            else: self.add_line(member,a,b)
            members.append(member)
        self.add_contour(name,*members,closed=True)

    def plug(self, cx=24, top=21, bottom=32):
        # Shared bowl width and mirrored prongs; cable joins bottom apex.
        r=8
        self.add_polyline('plug-top',(cx-r,top),(cx-4,top),(cx+4,top),(cx+r,top))
        self.add_line('plug-right',(cx+r,top),(cx+r,bottom-r))
        self.add_arc('plug-right-curve',(cx+r,bottom-r),(cx,bottom),radius_x=r)
        self.add_arc('plug-left-curve',(cx,bottom),(cx-r,bottom-r),radius_x=r)
        self.add_line('plug-left',(cx-r,bottom-r),(cx-r,top))
        self.add_contour('plug-bowl','plug-right','plug-right-curve','plug-left-curve','plug-left')
        self.relate('connect','plug-top','plug-bowl')
        for i,x in enumerate((cx-4,cx+4)):
            self.add_line(f'prong-{i}',(x,top-8),(x,top))
            self.relate('connect',f'prong-{i}','plug-top')
