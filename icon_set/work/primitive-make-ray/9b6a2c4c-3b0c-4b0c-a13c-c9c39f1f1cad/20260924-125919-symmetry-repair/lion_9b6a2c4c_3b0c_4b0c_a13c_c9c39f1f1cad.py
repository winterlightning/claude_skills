"""A lion's butterfly-shaped face nested inside its heart-shaped mane.
Plan: SQUARE extremes (6,6)-(42,42); both closed silhouettes generated
from a shared axis x=24 and mirrored cubic control points. No useful local
Lucide lion match; coherent paired lobes follow the geometric construction guide.
Fine facial marks omitted as in the supplied reference; complete contours retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "9b6a2c4c-3b0c-4b0c-a13c-c9c39f1f1cad"
SOURCE_PATH = "pictographic-primitives/animals/lion_9b6a2c4c-3b0c-4b0c-a13c-c9c39f1f1cad.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "lion"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("lion face",)
    keywords = ("lion", "mane", "face")
    def mirrored_loop(self,name,start,segments):
        axis=24
        mirror=lambda p:(2*axis-p[0],p[1])
        nodes=[start]+[s[2] for s in segments]
        reflected=[(mirror(c2),mirror(c1),mirror(nodes[i]))
                   for i,(c1,c2,end) in reversed(list(enumerate(segments)))]
        self.add_bezier(name,start,*segments,*reflected)
        self.add_contour(name+'-outline',name,closed=True)
    def build(self):
        self.mirrored_loop('mane',(24,10),[
            ((21,7),(18,6),(15,6)),
            ((9,6),(6,12),(6,20)),
            ((6,30),(16,38),(24,42)),
        ])
        self.mirrored_loop('face',(24,21),[
            ((21,15),(14,17),(17,23)),
            ((19,25),(18,27),(19,28)),
            ((20,31),(23,30),(24,29)),
        ])
