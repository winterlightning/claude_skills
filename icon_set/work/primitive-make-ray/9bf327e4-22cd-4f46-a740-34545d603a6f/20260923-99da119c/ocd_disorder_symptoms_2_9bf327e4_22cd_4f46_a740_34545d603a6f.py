from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9bf327e4-22cd-4f46-a740-34545d603a6f'
SOURCE_PATH = 'icon_set/work/todo-references/ocd disorder symptoms 2_9bf327e4-22cd-4f46-a740-34545d603a6f.svg'
AUTHOR = 'gpt-6'
# Construction plan: Left-facing head silhouette with repeated checklist symbols inside; intentional facial asymmetry preserves profile.
# Keyshape visible extremes are supplied by Keyshape.VRECT_L.bounds_for(SOLO48).
# Lucide construction reference: No useful subject match; shared human reference for portraits.
class Drawing(Solo48):
    icon_id = 'ocd-disorder-symptoms-2'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('ocd', 'disorder', 'symptoms', '2')
    def build(self):
        self.add_bezier('cranium',(8,19),((8,9),(14,4),(24,4)),((34,4),(40,12),(40,20)),((40,27),(35,29),(35,36)))
        self.add_polyline('face',(35,36),(35,44),(18,44),(18,36),(10,36),(10,27),(8,27),(8,19))
        self.contours.pop()
        self.add_contour('head','cranium',*[f'face-{i}' for i in range(1,8)],closed=True)
        for i,y in enumerate((14,24)):
            self.add_polyline(f'check-{i}',(16,y),(18,y+2),(21,y-2))
            self.add_line(f'text-{i}',(29,y),(32,y))
        self.add_polyline('empty-box',(24,33),(29,33),(29,38),(24,38),closed=True)

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, x, y, right, bottom, r=3):
        points=[(x+r,y),(right-r,y),(right,y+r),(right,bottom-r),(right-r,bottom),(x+r,bottom),(x,bottom-r),(x,y+r),(x+r,y)]
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            part=f'{name}-{i}'
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)

    def cross(self,name,cx,cy,r):
        for suffix,p in [('left',(cx-r,cy)),('right',(cx+r,cy)),('top',(cx,cy-r)),('bottom',(cx,cy+r))]:
            self.add_line(name+'-'+suffix,p,(cx,cy))
        self.relate('connect',*[name+'-'+s for s in ('left','right','top','bottom')])

    def clipboard(self):
        self.box('clip',17,4,31,12,4)
        self.add_polyline('board',(17,8),(8,8),(8,44),(40,44),(40,8),(31,8))
        self.relate('connect','clip','board')


# Visible keyshape extremes: (6, 2, 42, 46).
# Visual review: Head profile and two checks read clearly, but the empty checkbox closes at native size and crowds the neck; requires revision.
