from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '48b58407-6e7b-4cf9-b629-9742f8a963af'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-phone-hangup/20260929T091947Z-thuan-mac/reference/square phone hangup_48b58407-6e7b-4cf9-b629-9742f8a963af.svg'
AUTHOR = "gpt-6"
# Plan: Restore the reference’s soft curved handset and broad rounded terminal pieces.
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
    icon_id = 'square-phone-hangup'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the soft hooked handset and rounded terminal pieces; retain its narrow curved interior as in the original.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '2283373cb2c6bfc39e647dd4c6a10623e05e8600a4f8a644deb967505023db9c'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'frame', 'M 13 6 L 35 6 A 7 7 1 42 13 L 42 35 A 7 7 1 35 42 L 13 42 A 7 7 1 6 35 L 6 13 A 7 7 1 13 6 Z')
        _draw(self, 'receiver', 'M 17 13 C 19 12 19 14 21 18 C 22 20 18 20 19 23 C 21 27 24 29 27 29 C 29 28 29 26 31 27 L 35 29 C 39 32 33 37 29 35 C 20 32 13 25 13 18 C 13 16 15 14 17 13 Z')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
