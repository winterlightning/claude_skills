/* AI suggestions are editable drafts; this module never submits feedback or a review decision. */
window.IconFeedbackReviewer = function({getIcon, getDraft, setDraft, elements, reveal,
  request = (...args) => fetch(...args), delay = ms => new Promise(resolve => setTimeout(resolve, ms))}) {
  const jobs = new Map();
  const key = icon => icon && icon.key + ':' + icon.svg_sha256;
  const current = state => key(getIcon()) === state.key;
  function paint() {
    const icon = getIcon(), state = jobs.get(key(icon));
    elements.button.disabled = !icon || !!state?.running;
    elements.button.textContent = state?.running ? 'AI agent is reviewing…' : 'Ask Ai Agent for feedback';
    elements.status.textContent = state?.message || '';
    elements.result.hidden = !state?.feedback;
    elements.text.value = state?.feedback || '';
  }
  async function json(url, options) {
    const response = await request(url, options);
    let data;
    try { data = await response.json(); }
    catch { throw Error('AI feedback is unavailable. Restart the gallery server and try again.'); }
    if (!response.ok) throw Error(data?.error || 'Could not get AI feedback. Please try again.');
    return data;
  }
  async function ask() {
    const icon = getIcon();
    if (!icon) return;
    const identity = key(icon), existing = jobs.get(identity);
    if (existing?.running) return;
    // Reconnect after a polling/network error rather than buying another review.
    const state = {key: identity, icon: icon.key, sha: icon.svg_sha256,
      id: existing?.resumeId, running: true, message: 'Reviewing the artwork and profile…'};
    jobs.set(identity, state); paint();
    try {
      if (!state.id) {
        const started = await json('../api/ai-feedback', {method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({icon: state.icon, svg_sha256: state.sha})});
        if (!started.id) throw Error('The server did not return a review job. Please try again.');
        state.id = started.id;
      }
      let result;
      for (;;) {
        result = await json('../api/ai-feedback?id=' + encodeURIComponent(state.id), {cache: 'no-store'});
        if (result.status !== 'running') break;
        await delay(2000);
      }
      state.id = null;
      if (result.status !== 'completed') throw Error(result.error || 'AI review could not finish. Please try again.');
      if (result.icon !== state.icon || result.svg_sha256 !== state.sha)
        throw Error('The review does not match this artwork. Ask again.');
      if (typeof result.feedback !== 'string' || !result.feedback.trim())
        throw Error('The agent returned no feedback. Please try again.');
      state.feedback = result.feedback.trim();
      // Never put old artwork's feedback into a newly edited version of the same icon.
      const selected = getIcon();
      if (selected?.key === state.icon && !current(state)) return;
      const draft = getDraft(state.icon).trim();
      const combined = [draft, state.feedback].filter(Boolean).join('\n\n');
      if (combined.length > 10000) {
        state.message = 'AI feedback is ready below. Your draft is full; copy the suggestions you want to keep.';
      } else {
        setDraft(state.icon, combined);
        state.message = result.verdict === 'keep'
          ? 'AI suggests keeping this icon. Its feedback is in the form; no decision has been saved.'
          : 'AI feedback added to the form. Edit it to save automatically; no decision has been saved.';
        if (current(state)) { elements.feedback.value = combined; reveal(); }
      }
    } catch (error) {
      state.resumeId = state.id;
      state.message = error.message || 'Could not get AI feedback. Please try again.';
    } finally {
      state.running = false;
      if (current(state)) paint();
    }
  }
  elements.button.onclick = ask;
  return {ask, open() { paint(); if (jobs.get(key(getIcon()))?.feedback) reveal(); },
    hasResult() { return !!jobs.get(key(getIcon()))?.feedback; }};
};
