from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '948299f2-5256-57b6-9095-5640e5be11ca'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stacked-file-documents/20260929T091947Z-thuan-mac/reference/common file double_948299f2-5256-57b6-9095-5640e5be11ca.svg'
AUTHOR = "gpt-6"
# Plan: Restore two rounded overlapping file outlines with clipped upper-right corners.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: files.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'stacked-file-documents'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'front', 'M 10 14 L 23 14 C 25 14 26 16 28 18 L 32 22 L 32 38 A 4 4 1 28 42 L 10 42 A 4 4 1 6 38 L 6 18 A 4 4 1 10 14 Z')
        _draw(self, 'rear', 'M 15 14 L 15 10 A 4 4 1 19 6 L 31 6 C 33 6 34 8 36 10 L 42 16 L 42 30 A 4 4 1 38 34 L 32 34')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
