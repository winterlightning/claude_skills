"""An open padded glove tilts from lower left to upper right, with four long separated fingers and an outward thumb. A broad straight cuff wraps around its wrist.

Glove made upright; four rounded fingertips, thumb and broad cuff retained with three shared finger seams.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '765f4935-d388-462f-ab4d-ad786a029631'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__goalkeeper-glove-sports/20260927T075459Z-thuan-mac-1/reference/goalkeeper glove_765f4935-d388-462f-ab4d-ad786a029631.svg'
AUTHOR = 'gpt-6'

class GoalkeeperGloveSports(Solo48):
    icon_id = 'goalkeeper-glove-sports'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('goalkeeper', 'glove', 'soccer', 'football', 'hand', 'protection')

    def circle(self,name,x,y,r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def skeleton(self,branches):
        parts=[]
        for name,points in branches:
            members=[]
            for index,(a,b) in enumerate(zip(points,points[1:])):
                key=f'{name}-{index}';members.append(key)
                self.add_line(key,a,b);parts.append((key,a,b))
            if len(members)>1:self.add_contour(name,*members)
        for index,(a,p,q) in enumerate(parts):
            for b,r,s in parts[index+1:]:
                if p in (r,s) or q in (r,s):self.relate('connect',a,b)

    def rounded(self,name,x,y,w,h,r):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%8];key=f'{name}-{index}';members.append(key)
            if index%2:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def weight(self,name,x,y,w,h,r):
        # Expose bar attachment nodes at the midpoint of each vertical wall.
        middle=y+h//2
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,middle),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,middle),(x,y+r)]
        members=[]
        for index,a in enumerate(pts):
            b=pts[(index+1)%len(pts)];key=f'{name}-{index}';members.append(key)
            if index in [1,4,6,9]:self.add_arc(key,a,b,radius_x=r)
            else:self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)

    def build(self):
        # Mirror the source's right-facing thumb, keeping the four shared finger radii.
        mirror = lambda p: (48-p[0], p[1])
        for i,x in enumerate([10,18,26,34]):
            self.add_arc(f'finger-{i}',mirror((x,10)),mirror((x+8,10)),radius_x=4,sweep=False)
        branches=[('left',[(10,10),(10,22),(6,22),(6,28),(14,34),(14,42),(34,42),(34,34),(42,26),(42,10)]),('cuff',[(14,34),(34,34)]),('index-seam',[(18,10),(18,20)]),('middle-seam',[(26,10),(26,20)]),('ring-seam',[(34,10),(34,20)])]
        self.skeleton([(name,[mirror(p) for p in points]) for name,points in branches])
        self.relate('connect','finger-0','left-0');self.relate('connect','finger-3','left-8')
        for i,n in enumerate(['index-seam','middle-seam','ring-seam']):
         for j in [i,i+1]:self.relate('connect',n+'-0',f'finger-{j}')
        for i in range(3):self.relate('connect',f'finger-{i}',f'finger-{i+1}')
