"""An outlined pound sterling glyph.
Plan: VRECT_M supplies the narrow upright (10,4)-(38,44) centerline envelope.
Reduction: No defining glyph component removed; hook, crossbar and foot bands rebalanced.
Construction: Supplied reference owns outlined lettering; Lucide pound-sterling reviewed for hook, bar and baseline hierarchy.
Layout: Directional glyph asymmetry preserved; outlined treatment retained."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48

SOURCE_ICON_ID = '4b4714a5-9ccb-46f5-aa7c-3672e3f9cac9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_31/pound_4b4714a5-9ccb-46f5-aa7c-3672e3f9cac9.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'pound'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('pound',)
    ink_extremes = keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_bezier('outer-hook',(38,12),((38,7),(34,4),(27,4)),((17,4),(16,11),(18,20)))
        self.add_line('bar-left-1',(18,20),(10,20))
        self.add_line('bar-left-2',(10,20),(10,28))
        self.add_line('bar-left-3',(10,28),(18,28))
        self.add_bezier('lower-stem',(18,28),((18,33),(14,36),(12,36)))
        self.add_line('foot-1',(12,36),(12,44))
        self.add_line('foot-2',(12,44),(38,44))
        self.add_line('foot-3',(38,44),(38,36))
        self.add_line('foot-4',(38,36),(28,36))
        self.add_bezier('inner-stem',(28,36),((29,33),(28,30),(28,28)))
        self.add_line('bar-right-1',(28,28),(32,28))
        self.add_line('bar-right-2',(32,28),(32,20))
        self.add_line('bar-right-3',(32,20),(27,20))
        self.add_bezier('inner-hook',(27,20),((26,16),(25,12),(28,12)),((29,12),(30,12),(30,12)))
        self.add_line('mouth',(30,12),(38,12))
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
