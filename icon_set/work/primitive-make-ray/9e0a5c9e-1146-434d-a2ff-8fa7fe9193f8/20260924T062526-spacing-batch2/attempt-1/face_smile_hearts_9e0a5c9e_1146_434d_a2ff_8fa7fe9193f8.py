"""face smile hearts.
Plan: Heart silhouette containing two heart eyes and smile. Shared mirrored heart lobes; human facial vocabulary. No useful exact local Lucide match.
Keyshape SQUARE: visible bounds (4, 4, 44, 44); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8'
SOURCE_PATH='pictographic-primitives/_uncategorized_18/face smile hearts_9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='face-smile-hearts'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('face', 'smile', 'hearts')
    def build(self):
        self.add_bezier('heart-left',(24,42),((16,36),(6,28),(6,18)),((6,10),(9,6),(15,6)),((19,6),(22,8),(24,12)))
        self.add_bezier('heart-right',(24,12),((26,8),(29,6),(33,6)),((39,6),(42,10),(42,18)),((42,28),(32,36),(24,42)))
        self.add_contour('heart','heart-left','heart-right',closed=True)
        for i,x in enumerate((16,32)):
            self.add_bezier(f'eye-{i}',(x,25),((x-8,20),(x-4,13),(x,18)),((x+4,13),(x+8,20),(x,25)))
        self.add_arc('smile',(20,31),(28,31),radius_x=5,sweep=False)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)
