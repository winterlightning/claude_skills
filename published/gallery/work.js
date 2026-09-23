(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const STATE_LABELS = {open: 'Open', working: 'Working', expired: 'Claim expired', done: 'Done · awaiting review', 'cannot-fix': 'Cannot fix'};
  const REASON_LABELS = {'bad-stroke': 'Bad stroke drawn', 'manual-fix-request': 'Manual fix request', meaning: 'Unclear meaning', other: 'Other'};
  let rows = [], page = 1, loading = false;
  const selected = new Set();

  const workerKey = 'pictographic_worker';
  try { $('workWorker').value = localStorage.getItem(workerKey) || ''; } catch {}
  $('workWorker').addEventListener('input', () => { try { localStorage.setItem(workerKey, $('workWorker').value.trim()); } catch {} updateActions(); });

  async function api(method, path, body) {
    const response = await fetch(path, {method, cache: 'no-store', headers: body ? {'Content-Type': 'application/json'} : {}, body: body ? JSON.stringify(body) : undefined});
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw Object.assign(Error(data.error || ('HTTP ' + response.status)), {data});
    return data;
  }

  async function load() {
    if (loading) return;
    loading = true;
    $('workNotice').textContent = '';
    $('workRows').innerHTML = '<tr><td colspan="8" class="work-empty">Loading…</td></tr>';
    try {
      const all = [];
      let offset = 0;
      for (;;) {
        const data = await api('GET', '/api/work/disapproved?limit=500&offset=' + offset);
        all.push(...data.items);
        if (data.next_offset === null || data.next_offset === undefined) break;
        offset = data.next_offset;
      }
      rows = all;
      for (const key of selected) if (!rows.some(row => row.key === key)) selected.delete(key);
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

  function hoursLeft(row) {
    if (!row.work.expires_at) return null;
    return Math.max(0, Math.round((new Date(row.work.expires_at) - Date.now()) / 36e5 * 10) / 10);
  }

  function visible() {
    const family = $('workFamily').value, state = $('workState').value, reason = $('workReason').value;
    const query = $('workSearch').value.trim().toLowerCase();
    return rows.filter(row => (!family || row.family === family) && (!state || row.work.state === state)
      && (!reason || (row.reason || '') === reason)
      && (!query || [row.key, row.name, row.work.worker, row.feedback, row.disapproved_by, row.work.note].join(' ').toLowerCase().includes(query)));
  }

  function when(stamp) { return stamp ? new Date(stamp).toLocaleString() : ''; }

  function render() {
    const counts = {};
    for (const row of rows) counts[row.work.state] = (counts[row.work.state] || 0) + 1;
    const summary = $('workSummary');
    summary.replaceChildren(...['', 'open', 'working', 'expired', 'done', 'cannot-fix'].map(state => {
      const button = document.createElement('button');
      button.type = 'button';
      button.setAttribute('aria-pressed', String($('workState').value === state));
      button.innerHTML = (state ? STATE_LABELS[state] : 'All disapproved') + ' <b>' + (state ? counts[state] || 0 : rows.length) + '</b>';
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
      body.innerHTML = '<tr><td colspan="8" class="work-empty">' + (rows.length ? 'No disapproved icons match these filters.' : 'No disapproved icons on production.') + '</td></tr>';
    }
    for (const row of slice) {
      const tr = document.createElement('tr');
      tr.dataset.selected = String(selected.has(row.key));
      const check = document.createElement('input');
      check.type = 'checkbox'; check.checked = selected.has(row.key); check.setAttribute('aria-label', 'Select ' + row.key);
      check.onchange = () => { if (check.checked) selected.add(row.key); else selected.delete(row.key); tr.dataset.selected = String(check.checked); updateActions(); };
      tr.append(cell(check));
      const icon = document.createElement('div'); icon.className = 'work-icon';
      if (row.preview_url) { const img = document.createElement('img'); img.src = row.preview_url; img.alt = ''; img.loading = 'lazy'; icon.append(img); }
      const label = document.createElement('div');
      const code = document.createElement('code'); code.textContent = row.key;
      const small = document.createElement('small'); small.textContent = [row.name, row.family, row.category].filter(Boolean).join(' · ');
      label.append(code, small); icon.append(label);
      tr.append(cell(icon));
      const feedback = document.createElement('details'); feedback.className = 'work-feedback';
      const summaryLine = document.createElement('summary'); summaryLine.textContent = REASON_LABELS[row.reason] || (row.reason ? row.reason : 'No reason recorded');
      const text = document.createElement('p'); text.textContent = row.feedback || '(no feedback text)';
      const meta = document.createElement('div'); meta.className = 'work-meta'; meta.textContent = (row.disapproved_by || 'unknown') + ' · ' + when(row.disapproved_at);
      feedback.append(summaryLine, text, meta);
      tr.append(cell(feedback));
      const badge = document.createElement('span'); badge.className = 'work-badge'; badge.dataset.state = row.work.state; badge.textContent = STATE_LABELS[row.work.state] || row.work.state;
      tr.append(cell(badge));
      tr.append(cell(row.work.worker || '—'));
      tr.append(cell(when(row.work.claimed_at) || '—'));
      const left = hoursLeft(row);
      tr.append(cell(row.work.state === 'working' ? left + ' h left · until ' + when(row.work.expires_at) : row.work.updated_at ? 'updated ' + when(row.work.updated_at) : '—'));
      tr.append(cell(row.work.note || '—'));
      body.append(tr);
    }
    $('workPageInfo').textContent = shown.length ? 'Page ' + page + ' of ' + pages + ' · ' + shown.length + ' icons' : '';
    $('workPrev').disabled = page <= 1; $('workNext').disabled = page >= pages;
    const onPage = slice.filter(row => selected.has(row.key)).length;
    $('workSelectAll').checked = slice.length > 0 && onPage === slice.length;
    $('workSelectAll').indeterminate = onPage > 0 && onPage < slice.length;
    updateActions();
  }

  function cell(content) {
    const td = document.createElement('td');
    if (typeof content === 'string') td.textContent = content; else td.append(content);
    return td;
  }

  function updateActions() {
    const worker = $('workWorker').value.trim();
    $('workSelection').textContent = selected.size + ' selected';
    $('workClaim').disabled = !selected.size || !worker || loading;
    $('workRelease').disabled = !selected.size || !worker || loading;
  }

  async function claimSelected() {
    const worker = $('workWorker').value.trim();
    const icons = rows.filter(row => selected.has(row.key)).map(row => ({icon: row.key, svg_sha256: row.svg_sha256}));
    if (!icons.length || !worker) return;
    $('workClaim').disabled = true;
    try {
      const result = await api('POST', '/api/work/claim', {worker, icons});
      const lines = ['Claimed ' + result.claimed.length + ' icon' + (result.claimed.length === 1 ? '' : 's') + ' for ' + worker + '.'];
      for (const refused of result.refused) lines.push(refused.icon + ': ' + refused.error);
      $('workNotice').textContent = lines.join('\n');
      for (const item of result.claimed) selected.delete(item.key);
    } catch (error) {
      $('workNotice').textContent = 'Claim failed: ' + error.message;
    }
    await load();
  }

  async function releaseSelected() {
    const worker = $('workWorker').value.trim();
    const targets = rows.filter(row => selected.has(row.key));
    if (!targets.length || !worker) return;
    $('workRelease').disabled = true;
    let released = 0; const problems = [];
    for (const row of targets) {
      try { await api('POST', '/api/work/abandon', {icon: row.key, svg_sha256: row.svg_sha256, worker}); released++; selected.delete(row.key); }
      catch (error) { problems.push(row.key + ': ' + error.message); }
    }
    $('workNotice').textContent = ['Released ' + released + ' claim' + (released === 1 ? '' : 's') + '.', ...problems].join('\n');
    await load();
  }

  $('workSelectAll').onchange = () => {
    const shown = visible(); const size = Number($('workPageSize').value) || 100;
    for (const row of shown.slice((page - 1) * size, page * size)) { if ($('workSelectAll').checked) selected.add(row.key); else selected.delete(row.key); }
    render();
  };
  for (const id of ['workFamily', 'workState', 'workReason']) $(id).addEventListener('change', () => { page = 1; render(); });
  $('workSearch').addEventListener('input', () => { page = 1; render(); });
  $('workPageSize').addEventListener('change', () => { page = 1; render(); });
  $('workPrev').onclick = () => { page--; render(); };
  $('workNext').onclick = () => { page++; render(); };
  $('workRefresh').onclick = load;
  $('workClaim').onclick = claimSelected;
  $('workRelease').onclick = releaseSelected;
  load();
})();
