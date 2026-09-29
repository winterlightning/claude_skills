"""Three concentric-looking upper bands separated from two mirrored cloud ends; preserve all three bands and airy source composition.
Reference comparison: The rejected rainbow had two bands and heavy cloud junctions. Feedback asks to restore its intended meaning.
Construction references: Lucide rainbow: nested semicircular bands; reference defines opposing open cloud ends.
Omissions: Cloud ends remain open as in source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '41049662-f336-4650-9604-e8d4818347cc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rainbow-between-clouds/20260929T042221Z-thuan-mac/reference/weather clouds rainbow_41049662-f336-4650-9604-e8d4818347cc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rainbow-between-clouds'
    keyshape = Keyshape.HRECT_L
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
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.add_arc('outer',(4,26),(44,26),radius_x=20,radius_y=18,sweep=True)
        self.add_arc('middle',(11,27),(37,27),radius_x=13,radius_y=12,sweep=True)
        self.add_arc('inner',(18,28),(30,28),radius_x=6,radius_y=6,sweep=True)
        self.path('left-cloud',(4,33),('A',(12,35),8,8,True),('A',(12,43),4,4,True),('L',(4,43)))
        self.path('right-cloud',(44,33),('A',(36,35),8,8,False),('A',(36,43),4,4,False),('L',(44,43)))

Drawing.exception = {'reason': 'Three bands keep at least approximately 2px visible gaps while retaining 4px strokes. Natural cloud placement slightly exceeds the selected vertical envelope but stays inside 48px; authorized visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'b75876b7d5fce5a8672235520a5a7e52fd3381b9bd8934e86f58c5f6e1232928'}
