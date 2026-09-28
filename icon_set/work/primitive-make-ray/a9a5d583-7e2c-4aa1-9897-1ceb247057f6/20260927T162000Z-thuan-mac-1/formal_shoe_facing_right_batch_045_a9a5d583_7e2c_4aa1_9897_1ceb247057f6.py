"""Low shoe with scooped opening, broad toe and integral stepped heel; asymmetric side view.
Keyshape HRECT_M: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a9a5d583-7e2c-4aa1-9897-1ceb247057f6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__formal-shoe-facing-right-batch-045/20260927T160114Z-thuan-mac-1/reference/footwear_a9a5d583-7e2c-4aa1-9897-1ceb247057f6.svg'
AUTHOR = 'gpt-6'
class Batch045Icon3(Solo48):
    icon_id = 'formal-shoe-facing-right-batch-045'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('shoe', 'formal', 'footwear', 'heel', 'toe', 'clothing', 'dress')
    # Reference: No useful local shoe match; source establishes toe and heel.
    # Reduction: Dropped separate sole seam; kept integral block heel and scooped opening.
    # Bounds: (2, 8, 46, 40)
    def build(self):
        def path(name, start, *steps, closed=False):
            members=[]; p=start
            for i,step in enumerate(steps):
                q=step[1]
                if p == q: continue
                member=f"{name}-{i}"
                if step[0]=='L': self.add_line(member,p,q)
                else: self.add_arc(member,p,q,radius_x=step[2],radius_y=step[3],sweep=step[4])
                members.append(member); p=q
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

        path('shoe',(4,20),('L',(16,18)),('L',(25,10)),('L',(34,20)),('L',(38,20)),('A',(44,30),8,10,True),('L',(20,30)),('L',(20,38)),('L',(4,38)),('L',(4,20)),closed=True)
