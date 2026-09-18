"""Flying Blimp Airship — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '94ee19fa-6c64-4340-9c2b-4d23bc7e3842'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/airship_94ee19fa-6c64-4340-9c2b-4d23bc7e3842.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'flying-blimp-airship-batch-033'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('flying-blimp-airship',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: Blimp envelope with left fins and hanging gondola; right-facing rounded nose; extrema (4,8)-(44,40).

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x0,y0,x1,y1,r=4):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            ids=[]
            for i,p in enumerate(pts):
                q=pts[(i+1)%8];eid=f'{name}-{i}';ids.append(eid)
                if i%2:self.add_arc(eid,p,q,radius_x=r)
                else:self.add_line(eid,p,q)
            self.add_contour(name,*ids,closed=True)

        self.add_polyline('upper-tail',(4,22),(10,17),(16,12),(32,12))
        self.add_arc('nose-top',(32,12),(44,22),radius_x=12,radius_y=10)
        self.add_arc('nose-bottom',(44,22),(32,32),radius_x=12,radius_y=10)
        self.add_polyline('lower-tail',(32,32),(20,32),(16,32),(10,27),(4,22))
        self.contours.clear()
        self.add_contour('envelope',*[f'upper-tail-{i}' for i in range(1,4)],'nose-top','nose-bottom',*[f'lower-tail-{i}' for i in range(1,5)],closed=True)
        self.add_polyline('fin-top',(10,17),(4,8),(16,12))
        self.add_polyline('fin-bottom',(10,27),(4,36),(16,32))
        self.add_polyline('gondola',(20,32),(22,40),(30,40),(32,32))
        for name in ('fin-top','fin-bottom','gondola'):self.relate('connect','envelope',name)
