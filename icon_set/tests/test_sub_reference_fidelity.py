import hashlib
import json
from icon_set.scripts.sub_reference_fidelity import annotate_sub_references, resolve_audit_source

def test_audit_source_follows_a_relocated_checkout(tmp_path):
    source = tmp_path / 'pictographic-primitives' / 'state' / 'check.svg'
    source.parent.mkdir(parents=True)
    source.write_text('<svg/>')
    assert resolve_audit_source('/old/checkout/pictographic-primitives/state/check.svg', tmp_path) == source

def test_audit_source_does_not_hide_a_missing_reference(tmp_path):
    original = '/old/checkout/pictographic-primitives/state/missing.svg'
    assert str(resolve_audit_source(original, tmp_path)) == original

def test_fidelity_findings_apply_only_to_reviewed_model_revision(tmp_path):
    source=tmp_path/'model.py';source.write_text('old model')
    data=tmp_path/'icon_set/data';data.mkdir(parents=True)
    (data/'sub-reference-fidelity.json').write_text(json.dumps({'letter-b-sub':{'model_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'status':'superseded'}}))
    row={'family':'sub','icon_id':'letter-b-sub','python_source':{'path':'model.py'}}
    annotate_sub_references([row],tmp_path)
    assert row['reference_fidelity']['status']=='superseded'
    source.write_text('new complete model')
    annotate_sub_references([row],tmp_path)
    assert 'reference_fidelity' not in row

def test_missing_source_does_not_inherit_fidelity_verdict(tmp_path):
    data=tmp_path/'icon_set/data';data.mkdir(parents=True)
    (data/'sub-reference-fidelity.json').write_text(json.dumps({'x':{'model_sha256':'abc','status':'superseded'}}))
    row={'family':'sub','icon_id':'x'}
    annotate_sub_references([row],tmp_path)
    assert 'reference_fidelity' not in row

def test_replacement_link_requires_present_valid_unchanged_model(tmp_path):
    data=tmp_path/'icon_set/data';data.mkdir(parents=True)
    parent=tmp_path/'parent.py';parent.write_text('incomplete parent')
    child=tmp_path/'child.py';child.write_text('complete redraw')
    digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
    (data/'sub-reference-fidelity.json').write_text(json.dumps({'x':{
        'model_sha256':digest(parent),'status':'superseded'}}))
    (data/'sub-reference-repairs.json').write_text(json.dumps({'x':{
        'parent_model_sha256':digest(parent),'status':'redrawn','new_id':'x-v2',
        'new_model_path':'child.py','new_model_sha256':digest(child),
        'source_id':'source','review_url':'sub-reference-repairs/index.html#x'}}))
    old={'family':'sub','icon_id':'x','python_source':{'path':'parent.py'}}
    new={'family':'sub','icon_id':'x-v2','python_source':{'path':'child.py'},'validation':{'status':'valid'}}
    annotate_sub_references([old],tmp_path)
    assert 'resolution' not in old['reference_fidelity']
    annotate_sub_references([old,new],tmp_path)
    assert old['reference_fidelity']['replacement_id']=='x-v2'
    assert new['reference_fidelity']['status']=='redrawn'
    child.write_text('subsequent unreviewed edit')
    annotate_sub_references([old,new],tmp_path)
    assert 'resolution' not in old['reference_fidelity']
    assert 'reference_fidelity' not in new

def test_skipped_redraw_keeps_incomplete_parent_flagged(tmp_path):
    data=tmp_path/'icon_set/data';data.mkdir(parents=True)
    parent=tmp_path/'parent.py';parent.write_text('incomplete')
    digest=hashlib.sha256(parent.read_bytes()).hexdigest()
    (data/'sub-reference-fidelity.json').write_text(json.dumps({'x':{'model_sha256':digest,'status':'superseded'}}))
    (data/'sub-reference-repairs.json').write_text(json.dumps({'x':{
        'parent_model_sha256':digest,'status':'skip','reason':'Required detail does not fit.',
        'review_url':'sub-reference-repairs/index.html#x'}}))
    row={'family':'sub','icon_id':'x','python_source':{'path':'parent.py'}}
    annotate_sub_references([row],tmp_path)
    assert row['reference_fidelity']['status']=='superseded'
    assert row['reference_fidelity']['resolution']=='skip'
