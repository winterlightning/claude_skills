"""An outlined pound sterling currency glyph.

Symbol plan: pound-sterling: hooked upper stem, crossbar and baseline; outlined treatment retained from input.
Envelope: VRECT_M. The narrow upright glyph uses the 28-by-40 centerline envelope, (10,4)–(38,44).
Reduction: No defining features omitted.
"""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = '4b4714a5-9ccb-46f5-aa7c-3672e3f9cac9'
SOURCE_PATH = 'icon_set/work/todo-references/pound_4b4714a5-9ccb-46f5-aa7c-3672e3f9cac9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pound'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('pound',)
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_bezier('outer-hook',(38,14),((38,7),(34,4),(27,4)),((16,4),(14,11),(17,22)))
        self.add_line('bar-left-1',(17,22),(10,22))
        self.add_line('bar-left-2',(10,22),(10,30))
        self.add_line('bar-left-3',(10,30),(18,30))
        self.add_bezier('lower-stem',(18,30),((19,36),(15,39),(12,40)))
        self.add_line('foot-1',(12,40),(12,44))
        self.add_line('foot-2',(12,44),(38,44))
        self.add_line('foot-3',(38,44),(38,36))
        self.add_line('foot-4',(38,36),(24,36))
        self.add_bezier('inner-stem',(24,36),((27,32),(26,30),(26,30)))
        self.add_line('bar-right-1',(26,30),(32,30))
        self.add_line('bar-right-2',(32,30),(32,22))
        self.add_line('bar-right-3',(32,22),(25,22))
        self.add_bezier('inner-hook',(25,22),((23,15),(22,12),(27,12)),((29,12),(30,12),(30,14)))
        self.add_line('mouth',(30,14),(38,14))
        self.add_contour('pound','outer-hook','bar-left-1','bar-left-2','bar-left-3','lower-stem','foot-1','foot-2','foot-3','foot-4','inner-stem','bar-right-1','bar-right-2','bar-right-3','inner-hook','mouth',closed=True)

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
