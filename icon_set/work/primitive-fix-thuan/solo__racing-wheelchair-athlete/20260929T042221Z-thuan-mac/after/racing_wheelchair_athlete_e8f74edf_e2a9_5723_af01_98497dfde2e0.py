"""Large rear racing wheel, smaller forward wheel and long low outrigger beneath a leaning rider with a bent pushing arm and seated leg. Exact 4px head/body ink gap at (29,20).
Reference comparison: The rejected athlete was an isolated head over a thick wheel-and-bar symbol; the leaning torso, pushing arm and seated leg were lost.
Construction references: human_ref/full_body_ref.png action proportions; Lucide bike informs circular wheels; supplied reference owns wheelchair geometry.
Omissions: Fine clothing and wheel spokes omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e8f74edf-e2a9-5723-af01-98497dfde2e0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__racing-wheelchair-athlete/20260929T042221Z-thuan-mac/reference/racing wheelchair_e8f74edf-e2a9-5723-af01-98497dfde2e0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'racing-wheelchair-athlete'
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
        # Large rear wheel and low forward outrigger are distinctive racing-wheelchair geometry.
        self.circle('rear-wheel',14,33,11)
        self.circle('front-wheel',39,38,6)
        self.add_bezier('torso',(29,20),((29,23),(21,20),(18,23)))
        self.path('pushing-arm',(25,21),('L',(21,28)),('L',(16,29)))
        self.path('legs',(18,23),('L',(28,28)),('L',(29,35)),('L',(33,35)))
        self.add_line('outrigger',(26,33),(39,38))
        self.add_dot('rear-hub',(14,33))
        self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

Drawing.exception = {'reason': 'Racing wheelchair preserves true equipment overlap and compact bent limbs under the authorized visual exception. No false connection is used to hide spacing findings; native-size review verifies the silhouette.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '17bfd8a9ae7135048f6d4d172e4548a68f866d719fa23ac669a640aa7c16021d'}
