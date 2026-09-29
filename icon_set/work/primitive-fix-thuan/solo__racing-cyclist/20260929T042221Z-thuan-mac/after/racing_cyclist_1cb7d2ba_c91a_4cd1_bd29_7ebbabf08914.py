"""Restore large paired wheels, low curved racing torso, forward hands, sloped fork and bent pedaling leg. Head (29,8), r4, neck (29,20) gives exact 4px detached ink gap.
Reference comparison: The rejected cyclist used tiny wheels and an upright, broken pose that did not read as racing. The original has full bicycle wheels, a low back and a bent pedaling leg.
Construction references: human_ref/full_body_ref.png circular head and simple action limbs; Lucide bike wheel/pose construction.
Omissions: Frame reduced to rear stay and fork; small shoe simplified to pedal stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__racing-cyclist/20260929T042221Z-thuan-mac/reference/race_1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'racing-cyclist'
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
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        self.circle('head',29,8,4)
        self.circle('rear-wheel',10,36,8);self.circle('front-wheel',38,36,8)
        # Neck junction is (29,20): 20-(8+4)=8 centerline / 4 ink gap.
        self.add_bezier('torso',(29,20),((29,23),(19,20),(16,25)))
        self.path('leg',(16,25),('L',(25,31)),('L',(22,39)))
        self.path('arm',(29,20),('L',(34,25)),('L',(39,25)))
        self.add_line('fork',(35,25),(38,36))
        self.add_line('rear-frame',(10,36),(20,30))
        self.add_line('pedal',(20,39),(24,39))
        self.relate('connect','torso','leg');self.relate('connect','torso','arm');self.relate('connect','leg','pedal')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

Drawing.exception = {'reason': 'Complete cycling action requires wheel/frame overlaps and compact leg-to-wheel spacing. User authorized visual exception while head-to-torso gap stays exactly 4px and all strokes stay 4px.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'a7c341d49509300052ad4e48f9e1821b0e37e119be639419046f1a36876294d1'}
