"""Round bomb with a short angled neck, curved fuse and five detached spark rays, retaining the upper-right ignition detail.
Reference comparison: The rejected bomb had a straight stalk and a plus sign, losing the angled neck, curved fuse and radiating spark.
Construction references: Lucide bomb: round body and angled fuse housing; source defines curved fuse and radiating spark.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '334f5976-14a0-49e2-9421-a907055410d4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-bomb-with-spark/20260929T051531Z-thuan-mac/reference/bomber_334f5976-14a0-49e2-9421-a907055410d4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'round-bomb-with-spark'
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
        self.path('bomb',(26,21),('A',(32,29),14,14,True),('A',(18,44),14,15,True),('A',(4,29),14,15,True),('A',(18,15),14,14,True),('L',(21,11)),('L',(29,16)),('L',(26,21)),closed=True)
        self.path('fuse',(27,14),('A',(35,9),9,9,True))
        # Five detached rays around the burning fuse endpoint.
        for name,a,b in [('top',(39,2),(39,5)),('upper-right',(44,7),(46,5)),('right',(44,13),(46,14)),('bottom',(39,17),(39,20)),('upper-left',(32,3),(34,5))]: self.add_line(name,a,b)

Drawing.exception = {'reason': 'Compact ignition rays and neck joins require local spacing below MIC. The bomb remains a clear round silhouette with4px strokes, accepted under user authorization.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'a8b9fcc2510d7e0ff8329d6b5e4ab7c140fb92adb65a745c794cc996112333ac'}
