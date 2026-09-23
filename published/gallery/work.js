(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const STATE_LABELS = {working: 'Working', done: 'Done · back to Ready', 'cannot-fix': 'Cannot fix'};
  const stateOf = row => row.work.state || '';
  const STATUS_LABELS = {disapprove: 'Disapproved', claimed: 'Claimed', ready: 'Ready', approve: 'Approved', rejected: 'Rejected'};
  const REASON_LABELS = {'bad-stroke': 'Bad stroke drawn', 'manual-fix-request': 'Manual fix request', meaning: 'Unclear meaning', other: 'Other'};
  let rows = [], page = 1, loading = false;
  const open = new Set();
  const histories = new Map();
  const workerKey = 'pictographic_worker';
  try { $('workWorker').value = localStorage.getItem(workerKey) || ''; } catch {}
  // The guide targets production. The server says where that is (itself, or the dev server's sync source).
  fetch('/api/runtime', {cache: 'no-store'}).then(r => r.ok ? r.json() : null).then(runtime => {
    if (!runtime) return;
    if (runtime.mode === 'production') $('docBase').value = location.origin;
    else if (runtime.production_api) $('docBase').value = runtime.production_api;
    renderDoc();
  }).catch(() => {});
  const worker = () => $('workWorker').value.trim();
  const quote = value => "'" + String(value).replaceAll("'", "'\\''") + "'";
  function renderDoc() {
    const base = ($('docBase').value.trim() || 'https://suffered-scored-nicole-default.trycloudflare.com').replace(/\/$/, '');
    const me = worker() || 'thuan-mac';
    const setup = 'API_BASE=' + quote(base) + '\nWORKER=' + quote(me);
    const post = (route, body) => 'curl --fail-with-body -H \'Content-Type: application/json\' \\\n  --data ' + quote(JSON.stringify(body)) + ' \\\n  "$API_BASE' + route + '"';
    const claim = {icon: 'sub/plus', svg_sha256: 'HASH_FROM_STEP_1', worker: me};
    $('docFetch').textContent = setup + '\n\ncurl --fail-with-body "$API_BASE/api/work/disapproved?family=sub&limit=50&offset=0"\ncurl --fail-with-body "$API_BASE/api/work/queue?family=sub&limit=5"';
    $('docClaim').textContent = post('/api/work/claim', claim);
    $('docClaimMany').textContent = post('/api/work/claim', {worker: me, icons: [{icon: 'sub/plus', svg_sha256: 'HASH_FROM_STEP_1'}, 'sub/minus']});
    $('docBuild').textContent = 'python3 -m icon_set build --icon icon_set/model/icons/sub/plus_v3.py --no-png --no-report   # this icon only\npython3 -m icon_set publish --no-build                                                  # compact catalogs + release.json, no rebuild\ngit add icon_set/model/icons/sub/plus_v3.py published/sub32 published/gallery/icons.json published/release.json\ngit commit -m "Fix sub/plus" && git push origin icon-lib';
    $('docDone').textContent = post('/api/work/done', {...claim, note: 'sub/plus-v3, commit abc1234'});
    $('docUpload').textContent = 'python3 icon_set/scripts/work_queue.py upload --worker ' + quote(me) + ' --icon sub/plus --stage after \\\n  --svg published/sub32/plus.svg --python icon_set/model/icons/sub/plus.py --validation validation.txt --note "equalised the arms"\n\n# raw API: POST /api/work/result {icon, svg_sha256, worker, stage: "before"|"after", svg, python_path, python_source, validation, note}\n# read back: GET /api/work/result?icon=sub/plus&svg_sha256=HASH_FROM_STEP_1&stage=after&part=svg|python|validation';
    $('docResult').textContent = 'curl --fail-with-body "$API_BASE/api/work?icon=sub/plus"                      # status + work state now\ncurl --fail-with-body "$API_BASE/api/work/history?icon=sub/plus"              # revisions, claims, feedback, change log\ncurl "$API_BASE/api/work/result?icon=sub/plus&svg_sha256=HASH_FROM_STEP_1&stage=before" -o before.svg\ncurl "$API_BASE/api/icon-artwork/svg?icon=sub/plus" -o now.svg\ncurl --fail-with-body "$API_BASE/api/work/review?state=done"                 # every fixed icon awaiting review';
    $('docCli').textContent = 'export PICTOGRAPHIC_API=' + quote(base) + '\nexport PICTOGRAPHIC_WORKER=' + quote(me) + '\n\npython3 icon_set/scripts/work_queue.py next --limit 1 --offset 0 --disapprove-status bad-stroke   # fetch + claim, prints the brief; exit 3 = nothing to claim\npython3 icon_set/scripts/work_queue.py next --family sub --limit 3 --out fix-input.txt            # three sub icons at once\npython3 icon_set/scripts/work_queue.py done --icon sub/plus --note "sub/plus-v3"\npython3 icon_set/scripts/work_queue.py cannot-fix --icon sub/plus --note "why"\npython3 icon_set/scripts/work_queue.py abandon --icon sub/plus\npython3 icon_set/scripts/work_queue.py status --icon sub/plus';
  }
  $('workWorker').addEventListener('input', () => { try { localStorage.setItem(workerKey, worker()); } catch {} renderDoc(); render(); });
  $('docBase').addEventListener('input', renderDoc);

  async function api(path) {
    const response = await fetch(path, {cache: 'no-store'});
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw Error(data.error || ('HTTP ' + response.status));
    return data;
  }

  async function load() {
    if (loading) return;
    loading = true;
    $('workNotice').textContent = '';
    $('workRows').innerHTML = '<tr><td colspan="9" class="work-empty">Loading…</td></tr>';
    try {
      const all = [];
      let offset = 0;
      for (;;) {
        const data = await api('/api/work/review?limit=500&offset=' + offset);
        all.push(...data.items);
        if (data.next_offset === null || data.next_offset === undefined) break;
        offset = data.next_offset;
      }
      rows = all;
      histories.clear();
      fillFamilies();
    } catch (error) {
      rows = [];
      $('workNotice').textContent = 'Could not load the fix queue: ' + error.message;
    } finally {
      loading = false;
      render();
    }
  }

  function fillFamilies() {
    const select = $('workFamily'), current = select.value;
    const families = [...new Set(rows.map(row => row.family).filter(Boolean))].sort();
    select.replaceChildren(new Option('All families', ''), ...families.map(family => new Option(family, family)));
    select.value = families.includes(current) ? current : '';
  }

  function when(stamp) { return stamp ? new Date(stamp).toLocaleString() : ''; }
  function short(sha) { return sha ? sha.slice(0, 10) : '—'; }

  function visible() {
    const family = $('workFamily').value, state = $('workState').value, status = $('workStatus').value, reason = $('workReason').value;
    const query = $('workSearch').value.trim().toLowerCase();
    const mine = $('workMine').checked && worker();
    return rows.filter(row => (!family || row.family === family) && (!state || stateOf(row) === state) && (!status || row.status === status)
      && (!mine || row.work.worker === mine)
      && (!reason || (reason === 'missing' ? !row.reason : row.reason === reason))
      && (!query || [row.key, row.name, row.work.worker, row.feedback, row.disapproved_by, row.work.note].join(' ').toLowerCase().includes(query)));
  }

  function cell(content, className) {
    const td = document.createElement('td');
    if (className) td.className = className;
    if (typeof content === 'string') td.textContent = content; else if (content) td.append(content);
    return td;
  }

  function badge(kind, value, label) {
    const span = document.createElement('span');
    span.className = 'work-badge';
    span.dataset[kind] = value;
    span.textContent = label;
    return span;
  }

  function render() {
    const counts = {};
    for (const row of rows) counts[stateOf(row)] = (counts[stateOf(row)] || 0) + 1;
    $('workSummary').replaceChildren(...['', 'working', 'done', 'cannot-fix'].map(state => {
      const button = document.createElement('button');
      button.type = 'button';
      button.setAttribute('aria-pressed', String($('workState').value === state));
      button.innerHTML = (state ? STATE_LABELS[state] : 'All') + ' <b>' + (state ? counts[state] || 0 : rows.length) + '</b>';
      button.onclick = () => { $('workState').value = state; page = 1; render(); };
      return button;
    }));
    const shown = visible();
    const size = Number($('workPageSize').value) || 100;
    const pages = Math.max(1, Math.ceil(shown.length / size));
    page = Math.min(Math.max(1, page), pages);
    const slice = shown.slice((page - 1) * size, page * size);
    const body = $('workRows');
    body.replaceChildren();
    if (!slice.length) {
      body.innerHTML = '<tr><td colspan="9" class="work-empty">' + (rows.length ? 'No icons match these filters.' : 'No disapproved icons or fix claims on production.') + '</td></tr>';
    }
    for (const row of slice) {
      const tr = document.createElement('tr');
      tr.dataset.key = row.key;
      tr.dataset.mine = String(!!worker() && row.work.worker === worker());
      const icon = document.createElement('div'); icon.className = 'work-icon';
      if (row.preview_url) { const img = document.createElement('img'); img.src = row.preview_url; img.alt = ''; img.loading = 'lazy'; icon.append(img); }
      const label = document.createElement('div');
      const code = document.createElement('code'); code.textContent = row.key;
      const small = document.createElement('small'); small.textContent = [row.name, row.family, row.category].filter(Boolean).join(' · ');
      label.append(code, small); icon.append(label);
      tr.append(cell(icon));
      tr.append(cell(badge('status', row.status, STATUS_LABELS[row.status] || row.status)));
      const disapproval = document.createElement('div'); disapproval.className = 'work-disapproval';
      disapproval.append(badge('reason', row.reason || 'missing', REASON_LABELS[row.reason] || row.reason || 'No reason recorded'));
      const meta = document.createElement('div'); meta.className = 'work-meta'; meta.textContent = 'by ' + (row.disapproved_by || 'unknown') + ' · ' + when(row.disapproved_at);
      const feedback = document.createElement('details'); feedback.className = 'work-feedback';
      const summaryLine = document.createElement('summary'); summaryLine.textContent = row.feedback ? 'Feedback' : 'No feedback text';
      const text = document.createElement('p'); text.textContent = row.feedback || '(no feedback text)';
      feedback.append(summaryLine, text);
      disapproval.append(meta, feedback);
      tr.append(cell(disapproval));
      const stateCell = stateOf(row) ? cell(badge('state', stateOf(row), STATE_LABELS[stateOf(row)])) : cell('—');
      if ((row.work.results || []).includes('after')) stateCell.append(badge('result', 'after', 'fix uploaded'));
      tr.append(stateCell);
      tr.append(cell(row.work.worker ? (row.work.worker === worker() ? row.work.worker + ' (you)' : row.work.worker) : '—'));
      tr.append(cell(when(row.work.claimed_at) || '—'));
      let lease = '—';
      if (row.work.state === 'working' && row.work.expires_at) lease = Math.max(0, Math.round((new Date(row.work.expires_at) - Date.now()) / 36e4) / 10) + ' h left';
      else if (row.work.updated_at) lease = 'updated ' + when(row.work.updated_at);
      tr.append(cell(lease));
      tr.append(cell(row.work.note || '—'));
      const button = document.createElement('button'); button.type = 'button'; button.className = 'site-button work-history-button';
      button.textContent = open.has(row.key) ? 'Hide history' : 'History';
      button.setAttribute('aria-expanded', String(open.has(row.key)));
      button.onclick = () => { if (open.has(row.key)) open.delete(row.key); else open.add(row.key); render(); };
      tr.append(cell(button));
      body.append(tr);
      if (open.has(row.key)) body.append(detailRow(row));
    }
    $('workPageInfo').textContent = shown.length ? 'Page ' + page + ' of ' + pages + ' · ' + shown.length + ' icons' : '';
    $('workPrev').disabled = page <= 1; $('workNext').disabled = page >= pages;
  }

  function detailRow(row) {
    const tr = document.createElement('tr'); tr.className = 'work-detail';
    const td = document.createElement('td'); td.colSpan = 9;
    const history = histories.get(row.key);
    if (!history) {
      td.textContent = 'Loading history…';
      api('/api/work/history?icon=' + encodeURIComponent(row.key)).then(data => { histories.set(row.key, data); render(); })
        .catch(error => { histories.set(row.key, {error: error.message}); render(); });
    } else if (history.error) {
      td.textContent = 'Could not load history: ' + history.error;
    } else {
      td.append(changePanel(history), revisionList(history), eventLog(history));
    }
    tr.append(td);
    return tr;
  }

  function figure(src, caption, note) {
    const wrapper = document.createElement('figure');
    const img = document.createElement('img'); img.src = src; img.alt = caption;
    img.onerror = () => { img.replaceWith(Object.assign(document.createElement('p'), {className: 'work-missing', textContent: 'No drawing saved for this revision.'})); };
    const cap = document.createElement('figcaption'); cap.textContent = caption;
    wrapper.append(img, cap);
    if (note) { const p = document.createElement('p'); p.className = 'work-meta'; p.textContent = note; wrapper.append(p); }
    return wrapper;
  }

  function changePanel(history) {
    const panel = document.createElement('div'); panel.className = 'work-change';
    const heading = document.createElement('h3'); heading.textContent = 'What changed';
    panel.append(heading);
    const claimed = [...history.revisions].reverse().find(rev => rev.claim);
    const figures = document.createElement('div'); figures.className = 'work-figures';
    const resultUrl = (rev, stage, part) => '/api/work/result?icon=' + encodeURIComponent(history.icon) + '&svg_sha256=' + encodeURIComponent(rev.svg_sha256) + '&stage=' + stage + '&part=' + part;
    if (claimed) {
      const results = claimed.results || {};
      const before = results.before ? resultUrl(claimed, 'before', 'svg') : '';
      const claimNote = 'Claimed by ' + claimed.claim.worker + ' · ' + when(claimed.claim.claimed_at) + (claimed.claim.note ? ' · ' + claimed.claim.note : '');
      if (before) figures.append(figure(before, 'Before the fix · revision ' + short(claimed.svg_sha256), claimNote));
      else figures.append(figure('', 'Before the fix · revision ' + short(claimed.svg_sha256), claimNote + ' · no before drawing was uploaded'));
      if (results.after) figures.append(figure(resultUrl(claimed, 'after', 'svg'), 'Fixed · uploaded by ' + results.after.worker,
        when(results.after.saved_at) + (results.after.note ? ' · ' + results.after.note : '') + (results.after.python_path ? ' · ' + results.after.python_path : '')));
    }
    const currentNote = STATUS_LABELS[history.current.status] + (history.current.updated_by ? ' · by ' + history.current.updated_by : '') + (history.current.updated_at ? ' · ' + when(history.current.updated_at) : '');
    figures.append(figure('/api/icon-artwork/svg?icon=' + encodeURIComponent(history.icon), 'Now · revision ' + short(history.current.svg_sha256), currentNote));
    panel.append(figures);
    const verdict = document.createElement('p'); verdict.className = 'work-verdict';
    if (!claimed) verdict.textContent = 'No fix claim yet: the drawing shown is the one the reviewer disapproved.';
    else if (claimed.current) verdict.textContent = claimed.claim.state === 'done'
      ? 'Reported fixed by ' + claimed.claim.worker + ', but the new drawing has not reached production yet (same revision). The change will appear after the next production pull.'
      : 'This revision is ' + (STATE_LABELS[claimed.claim.state] || claimed.claim.state || 'not claimed').toLowerCase() + '; the drawing has not changed on production yet.';
    else verdict.textContent = 'The fix was deployed: the current revision differs from the one that was claimed. Compare the drawings above.';
    panel.append(verdict);
    if (claimed && claimed.results && (claimed.results.before?.has_python || claimed.results.after?.has_python || claimed.results.after?.has_validation)) {
      const sources = document.createElement('details'); sources.className = 'work-sources';
      const summary = document.createElement('summary'); summary.textContent = 'Python source and validation (uploaded)';
      const columns = document.createElement('div'); columns.className = 'work-source-columns';
      for (const [stage, label] of [['before', 'Before'], ['after', 'After']]) {
        const info = claimed.results[stage];
        if (!info || !info.has_python) continue;
        const column = document.createElement('div');
        const heading = document.createElement('h4'); heading.textContent = label + ' · ' + (info.python_path || 'module');
        const pre = document.createElement('pre'); pre.textContent = 'Loading…';
        fetch(resultUrl(claimed, stage, 'python'), {cache: 'no-store'}).then(r => r.ok ? r.text() : Promise.reject(Error('HTTP ' + r.status)))
          .then(text => { pre.textContent = text; }).catch(error => { pre.textContent = 'Could not load: ' + error.message; });
        column.append(heading, pre); columns.append(column);
      }
      sources.append(summary, columns);
      if (claimed.results.after?.has_validation) {
        const heading = document.createElement('h4'); heading.textContent = 'Validation after the fix';
        const pre = document.createElement('pre'); pre.textContent = 'Loading…';
        fetch(resultUrl(claimed, 'after', 'validation'), {cache: 'no-store'}).then(r => r.ok ? r.text() : Promise.reject(Error('HTTP ' + r.status)))
          .then(text => { pre.textContent = text; }).catch(error => { pre.textContent = 'Could not load: ' + error.message; });
        sources.append(heading, pre);
      }
      panel.append(sources);
    }
    return panel;
  }

  function revisionList(history) {
    const section = document.createElement('div'); section.className = 'work-revisions';
    const heading = document.createElement('h3'); heading.textContent = 'Revisions';
    section.append(heading);
    const list = document.createElement('ol');
    for (const rev of history.revisions) {
      const item = document.createElement('li');
      const title = document.createElement('div'); title.className = 'work-rev-title';
      const code = document.createElement('code'); code.textContent = short(rev.svg_sha256);
      title.append(code);
      if (rev.current) title.append(badge('status', 'current', 'current'));
      if (rev.review) title.append(badge('status', rev.review.status, STATUS_LABELS[rev.review.status] || rev.review.status), document.createTextNode(' ' + (rev.review.updated_by ? 'by ' + rev.review.updated_by + ' · ' : '') + when(rev.review.updated_at)));
      item.append(title);
      if (rev.claim) {
        const claim = document.createElement('p');
        claim.append(badge('state', rev.claim.state, STATE_LABELS[rev.claim.state] || rev.claim.state), document.createTextNode(' ' + rev.claim.worker + ' · claimed ' + when(rev.claim.claimed_at) + (rev.claim.note ? ' · ' + rev.claim.note : '')));
        item.append(claim);
      }
      for (const entry of rev.feedback) {
        const p = document.createElement('p'); p.className = 'work-feedback-entry';
        p.textContent = (REASON_LABELS[entry.reason] || entry.reason || 'feedback') + ' · ' + (entry.author || 'unknown') + ' · ' + when(entry.created_at) + (entry.edited_by ? ' (edited by ' + entry.edited_by + ')' : '') + '\n' + entry.feedback;
        item.append(p);
      }
      list.append(item);
    }
    section.append(list);
    return section;
  }

  function describe(event) {
    const d = event.details || {};
    switch (event.action) {
      case 'review': return 'Review status → ' + (STATUS_LABELS[d.status === 'pending' ? 'disapprove' : d.status] || d.status) + (d.source === 'work_done' ? ' (fix reported; feedback kept)' : '') + (d.svg_sha256 ? ' · revision ' + short(d.svg_sha256) : '');
      case 'feedback': return 'Feedback saved' + (d.reason ? ' · ' + (REASON_LABELS[d.reason] || d.reason) : '');
      case 'feedback_edit': return 'Feedback edited' + (d.reason ? ' · ' + (REASON_LABELS[d.reason] || d.reason) : '');
      case 'feedback_resolved': return 'Feedback cleared (' + (d.deleted_count || 0) + ' entries) when returned to Ready';
      case 'feedback_deleted': return 'Feedback deleted';
      case 'work_claim': return 'Claimed by ' + d.worker + ' · expires ' + when(d.expires_at);
      case 'work_heartbeat': return 'Lease extended by ' + d.worker + ' until ' + when(d.expires_at) + ' (legacy)';
      case 'work_done': return 'Reported done by ' + d.worker + (d.note ? ' · ' + d.note : '');
      case 'work_cannot_fix': return 'Reported cannot fix by ' + d.worker + (d.note ? ' · ' + d.note : '');
      case 'work_abandon': return 'Claim of ' + d.worker + ' released by ' + d.released_by + (d.previous_state ? ' (was ' + d.previous_state + ')' : '');
      case 'work_expired': return 'Claim of ' + d.worker + ' expired' + (d.taken_by ? ' · taken by ' + d.taken_by : ' · disapproved again, not claimed');
      default: return event.action.replaceAll('_', ' ') + (Object.keys(d).length ? ' · ' + JSON.stringify(d) : '');
    }
  }

  function eventLog(history) {
    const section = document.createElement('div'); section.className = 'work-events';
    const heading = document.createElement('h3'); heading.textContent = 'Change log';
    section.append(heading);
    if (!history.events.length) { const p = document.createElement('p'); p.className = 'work-meta'; p.textContent = 'No logged events for this icon.'; section.append(p); return section; }
    const list = document.createElement('ol');
    for (const event of [...history.events].reverse()) {
      const item = document.createElement('li');
      const time = document.createElement('time'); time.textContent = when(event.at);
      const who = document.createElement('b'); who.textContent = event.user;
      item.append(time, document.createTextNode(' '), who, document.createTextNode(' · ' + describe(event)));
      list.append(item);
    }
    section.append(list);
    return section;
  }

  for (const id of ['workFamily', 'workState', 'workStatus', 'workReason']) $(id).addEventListener('change', () => { page = 1; render(); });
  $('workSearch').addEventListener('input', () => { page = 1; render(); });
  $('workPageSize').addEventListener('change', () => { page = 1; render(); });
  $('workPrev').onclick = () => { page--; render(); };
  $('workNext').onclick = () => { page++; render(); };
  $('workMine').addEventListener('change', () => { page = 1; render(); });
  $('workRefresh').onclick = load;
  renderDoc();
  load();
})();
