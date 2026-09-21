"""Persist scoped solo corrections atomically, preserving every unrelated edit."""
import json,sqlite3,sys
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parents[2];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_status import load_status,set_status
from icon_set.scripts.primitive_briefs import load_primitive_briefs,save_primitive_brief
from icon_set.scripts.deploy import record_activity
data=json.loads((P/'review.json').read_text());rows=[r for r in data['rows'] if r['route']=='solo']
snapshot=json.loads((P/'before.json').read_text());known=set(snapshot);affected={r['uuid'] for r in rows}
assert len(known)==750 and len(affected)==382
for r in rows:
    assert r['uuid'] in r['reference_brief'] and r['reference_path'] in r['reference_brief']
    assert 50<len(r['reference_brief'])<=20000
    if r['brief_link']:
        p=Path(r['brief_link']);assert p.is_file() and p.with_suffix('.json').is_file()
        subject=json.loads(p.with_suffix('.json').read_text())
        assert subject['family']=='solo' and 6<=len(subject['tags'])<=10
        assert set(subject)=={'concept','icon_id','family','description','tags'}
db=ROOT/'icon_set/.local/state/feedback.sqlite3'
conn=sqlite3.connect(db,timeout=30)
with conn:
    conn.execute('BEGIN IMMEDIATE')
    before=load_status(conn);before_refs=load_primitive_briefs(conn)
    for uid,v in snapshot.items():
        assert before.get(uid)==v['decision'],f'Concurrent decision change: {uid}'
        assert before_refs.get(uid)==v['reference_brief'],f'Concurrent brief change: {uid}'
    backup={uid:{'decision':before.get(uid),'reference_brief':before_refs.get(uid)} for uid in affected}
    bp=P/'before-save.json'
    if bp.exists():assert json.loads(bp.read_text())==backup
    else:bp.write_text(json.dumps(backup,indent=2)+'\n')
    for r in rows:
        note='Solo: '+r['visual_reason']+' Reuse decision: '+r['reuse_action']+'. '
        if r['existing_target']:note+='Existing icon: '+r['existing_target']['icon_id']+'. '
        if r['canonical_source_number']!=r['number']:note+='Share authoring target with source '+str(r['canonical_source_number'])+'. '
        note+='See saved SOLO48 reference brief; no duplicate generation.'
        save_primitive_brief(conn,r['uuid'],'solo',r['reference_brief'],known=known,user='agent',record=record_activity)
        set_status(conn,[r['uuid']],r['status'],r['reason'],note,user='agent',record=record_activity,known=known)
    after=load_status(conn);after_refs=load_primitive_briefs(conn)
    for r in rows:
        uid=r['uuid'];d=after.get(uid);ref=after_refs[uid]
        assert ref['family']=='solo' and ref['brief']==r['reference_brief'].strip()
        if r['status']=='todo':assert d is None
        else:assert d['status']=='skip' and d['reason']=='other' and d['main_brief'] is None and d['sub_brief'] is None
    assert {k:v for k,v in before.items() if k not in affected}=={k:v for k,v in after.items() if k not in affected}
    assert {k:v for k,v in before_refs.items() if k not in affected}=={k:v for k,v in after_refs.items() if k not in affected}
    for uid in known:
        ref=after_refs.get(uid);assert ref and ref['brief'].strip() and uid in ref['brief']
conn.close()
result={'saved':True,'database':str(db),'solo_mappings_saved':len(rows),'scoped_reference_brief_coverage':'750/750',
        'unchanged_container_and_side_sources':368,'unrelated_decisions_unchanged':True,'unrelated_briefs_unchanged':True,
        'concurrent_change_check_passed':True,'summary':data['summary'],'generation_jobs_queued':0}
(P/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
