from author import author,ROOT
import ast,json
src=(ROOT/'drawings.py').read_text();s={}
for n in ast.parse(src).body:
 if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call):s[str(ast.literal_eval(n.value.args[0]))]=ast.get_source_segment(src,n)
H='Human full_body_ref.png: circular head, coherent limbs and exact 4-unit detached head gap'
edits={
0:[("16,12,6","14,10,6"),("(16,26)","(14,24)"),("(16,32)","(14,32)"),("(24,42)","(22,44)"),("(32,30)","(30,30)"),("(40,42)","(40,44)"),("(28,26)","(26,26)"),("join('arm','legs')","join('arm','legs')\nself.mark_human_figure('person',head='head',torso='torso',torso_junction='start')")],
2:[("(14,32)","(14,36)"),("(34,32)","(34,36)")],
3:[("('C',(40,18),(34,8),(39,12))","('C',(36,12),(31,8),(34,9)),('C',(40,18),(38,14),(39,16))"),("(34,10),[('C',(29,25),(36,15),(34,22))]","(36,12),[('C',(29,25),(35,17),(33,22))]")],
4:[("(26,29)","(26,25)"),("(44,29)","(44,25)"),("(40,29)","(40,25)"),("(4,29),(7,29),(21,29),(26,25)","(4,25),(7,25),(21,25),(26,25)"),("(x,29)","(x,25)"),("poly('window',(34,16),(34,24),(44,24));join('window','cab')","line('window',(34,16),(40,16));join('window','cab')")]
}
for i,pairs in edits.items():
 code=s[str(i)]
 for old,new in pairs:
  assert old in code,(i,old);code=code.replace(old,new)
 s[str(i)]=code;exec(code)
(ROOT/'specs.json').write_text(json.dumps(s,indent=2))
