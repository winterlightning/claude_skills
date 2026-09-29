"""Add a distinct ear and muzzle, a curved chest and hindquarters, hanging tail, angled supports and a pronounced bowed rocker; preserve the left-facing toy.
Reference comparison: No original was available; the supplied reference is the rejected drawing. Its triangular head and flat rail obscure the rocking-horse shape.
Construction references: No useful Lucide rocking-horse match; supplied current drawing establishes the horse-on-rocker concept.
Omissions: Tiny eye omitted to avoid a solid head; the muzzle and ear supply recognition.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8b250624-b4d9-5599-8927-bda7b954f2df'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rocking-horse-toy-solo/20260929T051531Z-thuan-mac/reference/rocking-horse-toy-solo_8b250624-b4d9-5599-8927-bda7b954f2df.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rocking-horse-toy-solo'
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
        # No original was available; use rejected horse as meaning reference, then restore missing equine anatomy.
        self.path('horse',(12,23),('L',(5,25)),('A',(4,19),4,4,True),('L',(14,11)),('L',(15,5)),('L',(20,10)),('L',(23,18)),('L',(33,18)),('A',(39,24),6,6,True),('A',(34,29),5,5,True),('L',(19,29)),('L',(16,22)),('L',(12,23)),closed=True)
        self.add_line('mane',(18,11),(23,18));self.relate('connect','horse','mane')
        self.path('tail',(39,23),('C',(44,30),(43,22),(44,26)))
        self.path('front-support',(21,29),('L',(16,39)))
        self.path('rear-support',(32,29),('L',(35,39)))
        self.path('rocker',(4,36),('C',(24,44),(7,46),(16,44)),('C',(44,36),(32,44),(41,46)))
        self.relate('connect','horse','tail');self.relate('connect','horse','front-support');self.relate('connect','horse','rear-support')

Drawing.exception = {'reason': 'Horse anatomy and support-to-rocker relationships need compact spacing. User authorized visual exception for the complete toy silhouette at48px.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'fc8bb1a9a31a0db1ec63cffa3bc1fc99d64fc0836b9e6415dbef5e24969e13b3'}
