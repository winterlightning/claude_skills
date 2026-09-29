"""Restore broad scalloped fan headdress, horizontal headband, round lower face, ears and V-shaped collar with shoulders; paired contours share x24 symmetry.
Reference comparison: The rejected portrait substituted a single side feather for the reference fan headdress and omitted the ears and V collar. Feedback asks to recover the reference portrait.
Construction references: human_ref/user.svg: circular lower face and broad shoulders. Original reference defines fan headdress, headband and collar.
Omissions: Facial features omitted as in the original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f115a501-49ed-4291-9f64-42b1086ca5d2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__red-indian-man-avatar/20260929T051531Z-thuan-mac/reference/red indian man_f115a501-49ed-4291-9f64-42b1086ca5d2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'red-indian-man-avatar'
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
        # Frontal portrait with a broad symmetric fan headdress; no invented single side feather.
        self.path('headdress',(10,21),('C',(7,13),(3,20),(4,14)),('C',(13,8),(7,8),(9,6)),('C',(20,7),(16,3),(19,4)),('C',(28,7),(21,1),(27,1)),('C',(35,8),(29,4),(32,3)),('C',(41,13),(39,6),(41,8)),('C',(38,21),(44,14),(45,20)))
        self.path('head',(15,24),('A',(24,18),9,6,True),('A',(33,24),9,6,True),('L',(33,28)),('A',(15,28),9,9,True),('L',(15,24)),closed=True)
        self.add_line('headband',(15,24),(33,24));self.relate('connect','head','headband')
        self.path('left-ear',(15,25),('A',(11,31),4,4,False),('L',(15,32)))
        self.path('right-ear',(33,25),('A',(37,31),4,4,True),('L',(33,32)))
        self.path('shoulders',(8,44),('C',(18,40),(10,42),(15,40)),('L',(24,45)),('L',(30,40)),('C',(40,44),(33,40),(38,42)))
        self.add_line('headdress-left-rib',(18,14),(21,18));self.add_line('headdress-right-rib',(30,14),(27,18))

Drawing.exception = {'reason': 'Fan headdress, headband and ears need compact local gaps in the complete portrait. User authorized a meaning-preserving visual exception with4px strokes; circular lower jaw and balanced shoulders remain clear.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '2d93d2db511e7517309c9fff04c855273a11a9d5a6c8a9654afbda35477836d9'}
