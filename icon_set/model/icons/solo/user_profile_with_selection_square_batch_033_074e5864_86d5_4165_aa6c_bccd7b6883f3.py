"""User Profile with Selection Square — new batch-033 result."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '074e5864-86d5-4165-aa6c-bccd7b6883f3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/person with square_074e5864-86d5-4165-aa6c-bccd7b6883f3.svg'
AUTHOR = 'gpt-6'

class Batch033Icon(Solo48):
    icon_id = 'user-profile-with-selection-square-batch-033'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/other"
    aliases = ('user-profile-with-selection-square',)
    keywords = ('batch-033',)

    def build(self):
        # Symbol plan: User bust beside selection square; head radius8, shoulders radius10 and exact detached gap8; extrema (6,6)-(42,42).

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

        self.add_polyline('selection',(6,6),(14,6),(14,14),(6,14),closed=True)
        circle('head',32,16,8)
        self.add_arc('shoulder-left',(22,42),(32,32),radius_x=10)
        self.add_arc('shoulder-right',(32,32),(42,42),radius_x=10)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
