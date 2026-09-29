"""Rounded muzzle and head casing, capsule torso, two clear bent support legs with horizontal feet and an upturned tail; remove crowded duplicate leg outlines.
Reference comparison: The rejected robot dog had angular stick legs, a triangular face and a diagonal tail. The source has a rounded mechanical head, capsule body, articulated feet and a curved tail.
Construction references: Lucide dog provides rounded animal contour principles; supplied robot-dog reference defines mechanical side silhouette.
Omissions: Leg outlines reduced to coherent single strokes so both feet remain clear at48px; small body seams omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c20481c7-9ec2-4d00-987f-2953dfb49c5c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__robot-dog/20260929T051531Z-thuan-mac/reference/robot pet dog_c20481c7-9ec2-4d00-987f-2953dfb49c5c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'robot-dog'
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
            elif step[0]=='C': self.add_bezier(key,p,(step[2],step[3],end))
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.path('head',(4,7),('L',(15,7)),('A',(21,13),6,6,True),('L',(21,23)),('A',(15,18),6,6,True),('L',(15,7)))
        self.add_arc('muzzle',(4,7),(15,16),radius_x=11,radius_y=9,sweep=False)
        self.path('body',(19,23),('L',(34,23)),('A',(41,30),7,7,True),('L',(40,34)),('L',(36,34)),('L',(31,34)),('L',(23,34)),('L',(18,34)),('A',(12,29),6,6,True),('A',(19,23),7,6,True),closed=True)
        self.path('tail',(35,23),('A',(44,18),10,10,False),('C',(40,29),(44,24),(44,27)))
        self.path('front-leg',(23,34),('L',(18,43)),('L',(9,43)))
        self.path('rear-leg',(31,34),('L',(35,39)),('L',(31,44)),('L',(25,44)))
        self.relate('connect','body','head');self.relate('connect','body','tail');self.relate('connect','body','front-leg');self.relate('connect','body','rear-leg');self.relate('connect','head','muzzle')

Drawing.exception = {'reason': 'Mechanical body joins and articulated feet require compact interior openings. Retain the complete robotic dog under user-authorized visual exception with uniform4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '92d353adb9989f192de7101c2f5ff395dfa2ae184633d3dd22401b92ba9a21c4'}
