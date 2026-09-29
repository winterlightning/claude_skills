from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '91565135-36f8-42bb-b2ed-6c12f04a7eb5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__tty-answer/20260929T090755Z-thuan-mac/reference/tty answer_91565135-36f8-42bb-b2ed-6c12f04a7eb5.svg'
AUTHOR = "gpt-6"
# Plan: Restore a contoured telephone receiver inside the answer speech bubble.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: phone.

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
    icon_id = 'tty-answer'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve an outlined telephone handset with earpieces inside its reply bubble; accept small handset apertures and the tail envelope.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '119387d0ab93da6b8cb9964d5cc3180afe466aa4b2ee6dd52c4a55188493be21'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'bubble', 'M 14 6 L 34 6 A 8 8 1 42 14 L 42 29 A 8 8 1 34 37 L 21 37 L 12 44 L 12 37 C 8 36 6 33 6 29 L 6 14 A 8 8 1 14 6 Z')
        _draw(self, 'receiver', 'M 16 13 L 21 18 L 18 21 C 20 24 23 27 26 28 L 29 25 L 34 29 C 31 34 26 32 20 27 C 14 22 12 17 16 13 Z')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
