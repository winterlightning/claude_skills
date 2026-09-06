'use strict';

const ProfileAPI = (() => {
  function create(token, request = fetch) {
    async function send(method, payload) {
      const response = await request('/api/profiles', { method, cache: 'no-store', headers: { 'X-Profile-Token': token, ...(payload ? { 'Content-Type': 'application/json' } : {}) }, ...(payload ? { body: JSON.stringify(payload) } : {}) });
      const data = await response.json();
      if (!response.ok) { const error = new Error(data.error || `Profile request failed (${response.status}).`); error.status = response.status; throw error; }
      if (!data.configuration || typeof data.revision !== 'string' || !data.resolvedProfiles) throw new Error('The server returned an invalid profile response.');
      return data;
    }
    return { load: () => send('GET'), save: (configuration, revision) => send('PUT', { configuration, revision }) };
  }
  return Object.freeze({ create });
})();
if (typeof module !== 'undefined' && module.exports) module.exports = ProfileAPI;
