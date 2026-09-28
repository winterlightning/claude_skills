"""Left fist over rising forearm with broad rounded elbow and bicep bulge; mirrored anatomy.
Keyshape SQUARE: exact SOLO48 centerline envelope, chosen for subject proportions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ee5bfb94-7340-47f3-893b-14b8899829f6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__flexed-arm-with-left-fist-batch-045/20260927T161452Z-thuan-mac-1/reference/forearm_ee5bfb94-7340-47f3-893b-14b8899829f6.svg'
AUTHOR = "gpt-6"
class Batch045Icon15(Solo48):
    icon_id = 'flexed-arm-with-left-fist-batch-045'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('arm', 'muscle', 'bicep', 'flex', 'fist', 'strength', 'body')
    # Reference: biceps-flexed: fist, forearm and bicep silhouette. Human full_body_ref.png inspected for continuous rounded limb vocabulary.
    # Reduction: Dropped interior muscle creases; continuous flexed arm with fist and bicep retained.
    # Bounds: (4, 4, 44, 44)
    # Isolated arm: no head/torso or detached-head measurement applies.
    def build(self):
        # Mirror the rejected silhouette so its fist and bicep match the source.
        def flip(point): return (48-point[0], point[1])
        def path(name, start, *steps, closed=False):
            members=[]; p=start
            for i,step in enumerate(steps):
                q=step[1]
                if p == q: continue
                member=f"{name}-{i}"
                if step[0]=='L': self.add_line(member,flip(p),flip(q))
                else: self.add_arc(member,flip(p),flip(q),radius_x=step[2],radius_y=step[3],sweep=not step[4])
                members.append(member); p=q
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

        path('arm',(42,30),('A',(24,30),9,10,False),('L',(22,14)),('A',(16,6),6,8,False),('L',(12,6)),('A',(6,12),6,6,False),('A',(12,18),6,6,False),('L',(14,18)),('L',(6,34)),('A',(14,42),8,8,False),('L',(30,42)),('A',(42,30),12,12,False),closed=True)
