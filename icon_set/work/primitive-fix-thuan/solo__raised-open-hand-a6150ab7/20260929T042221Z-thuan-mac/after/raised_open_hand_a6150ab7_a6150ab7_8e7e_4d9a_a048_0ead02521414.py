"""Restore four staggered upright fingers plus an opposing diagonal thumb, a full palm and smooth wrist curve.
Reference comparison: The rejected open hand had only three upright fingers and a horizontal thumb. Feedback requests the original open-hand meaning.
Construction references: Lucide hand: shared finger arcs and coherent outer palm. Human reference checked for stroke vocabulary.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a6150ab7-8e7e-4d9a-a048-0ead02521414'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__raised-open-hand-a6150ab7/20260929T042221Z-thuan-mac/reference/hand 1_a6150ab7-8e7e-4d9a-a048-0ead02521414.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'raised-open-hand-a6150ab7'
    keyshape = Keyshape.VRECT_L
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
        self.path('hand',(16,27),('L',(16,11)),('A',(22,11),3,3,True),('L',(22,7)),('A',(28,7),3,3,True),('L',(28,10)),('A',(34,10),3,3,True),('L',(34,15)),('A',(40,15),3,3,True),('L',(40,30)),('A',(26,44),14,14,True),('L',(24,44)),('A',(15,39),11,11,True),('L',(9,29)),('A',(14,24),4,4,True),('L',(16,27)),closed=True)
        for x,y in [(22,11),(28,10),(34,15)]:
            self.add_line(f'finger-{x}',(x,y),(x,23))
            self.relate('connect','hand',f'finger-{x}')

Drawing.exception = {'reason': 'Four complete fingers require 6-unit pitch at SOLO48. The intentional 2-unit ink slots preserve the open-hand identity and remain visible at native size; organic keyshape variance accepted.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'bbaa8ec2e3cfaae116a349a303ec83781c6656fc15741993b10ba159b4f9e59b'}
