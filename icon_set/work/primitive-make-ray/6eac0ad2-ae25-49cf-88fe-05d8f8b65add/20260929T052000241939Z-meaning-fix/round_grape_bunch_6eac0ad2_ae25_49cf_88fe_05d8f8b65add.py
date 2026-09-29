"""Restore seven individual round fruit forms in the source cluster, using occluded rear contours around the foreground central berry and a curved stem.
Reference comparison: The rejected drawing was a scalloped flower with a dot. The reference is a cluster of seven round fruit segments with a curved stem.
Construction references: Lucide grape original and atomic-debug: independently legible round berries; supplied source controls seven-fruit arrangement.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6eac0ad2-ae25-49cf-88fe-05d8f8b65add'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-grape-bunch/20260929T051531Z-thuan-mac/reference/sugar apple_6eac0ad2-ae25-49cf-88fe-05d8f8b65add.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'round-grape-bunch'
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
        # Seven rounded berries, with rear contours interrupted behind the central foreground berry.
        self.circle('center-berry',24,22,7)
        self.path('upper-left',(18,19),('C',(8,17),(12,24),(6,22)),('C',(21,16),(7,6),(20,6)))
        self.path('upper-right',(27,16),('C',(41,17),(28,6),(41,6)),('C',(30,21),(43,23),(36,25)))
        self.path('left-middle',(17,24),('C',(11,37),(6,25),(5,34)),('C',(23,29),(20,42),(24,35)))
        self.path('right-middle',(29,27),('C',(36,38),(38,24),(43,32)),('C',(23,29),(31,42),(22,38)))
        self.path('far-right',(41,21),('C',(42,34),(49,23),(47,32)),('L',(38,35)))
        self.path('bottom',(17,38),('C',(30,38),(13,49),(34,49)))
        self.path('stem',(24,15),('C',(28,4),(23,10),(25,6)))
        self.relate('connect','center-berry','stem')

Drawing.exception = {'reason': 'Adjacent fruit contours intentionally touch or overlap as a cluster. Separate rounded interiors remain readable; organic cluster bounds and local gaps use the authorized visual exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': '4dd8f0d9b6f0f865dd266a2a7112ff7b5cb5c2e0ed0a8580595c45a6523071ff'}
