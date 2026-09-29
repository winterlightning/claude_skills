"""Curved diagonal dagger, distinct guard and hilt, a fully separate poison droplet at upper right and open-bottom round head at lower right.
Reference comparison: The rejected poisonous dagger was a triangular spike and the victim cue became a small arch. The source has a curved blade, handle and guard, a poison droplet and a head silhouette.
Construction references: Lucide sword: distinct blade, crossguard and hilt; original controls curved blade and two right-side modifiers.
Omissions: Facial detail omitted as in source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3e8bfa80-059e-487c-bda0-70b3d4ddf001'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__roleplay-game-poisonous-dagger-knife/20260929T051531Z-thuan-mac/reference/roleplay game poisonous dagger knife_3e8bfa80-059e-487c-bda0-70b3d4ddf001.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'roleplay-game-poisonous-dagger-knife'
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
        self.path('blade',(12,29),('L',(32,5)),('C',(23,25),(33,14),(28,21)),('L',(17,32)))
        self.add_line('guard',(7,25),(23,37))
        self.path('handle',(11,28),('L',(5,36)),('A',(11,42),4,4,False),('L',(18,33)))
        self.path('poison-drop',(40,8),('C',(36,17),(39,12),(36,14)),('A',(44,17),4,4,False),('C',(40,8),(44,14),(41,12)),closed=True)
        self.path('victim',(30,44),('L',(30,39)),('A',(27,34),8,8,True),('A',(43,34),8,8,True),('A',(40,39),8,8,True),('L',(40,44)))
        self.relate('connect','blade','guard');self.relate('connect','handle','guard')

Drawing.exception = {'reason': 'Three meaning-bearing elements require compact spacing and narrow blade/handle openings. User authorized the complete poisonous-dagger composition as a visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '2c1eb2284de76cf57eb6529773c3b7b0116e30911bb0dc8448108032b1def739'}
