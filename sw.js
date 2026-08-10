/* Domain redirect service worker
 * Redirects all requests using HTTP 307
 * Uses Response.redirect() for proper 307 temporary redirect
 *
 */

importScripts('/_redirect/redirect-config.js');

const OLD_DOMAIN = REDIRECT_CONFIG.OLD_DOMAIN;
const NEW_DOMAIN = REDIRECT_CONFIG.NEW_DOMAIN;
const PROTOCOL = REDIRECT_CONFIG.PROTOCOL;

// Install event - skip waiting to activate immediately
self.addEventListener('install', function(event) {
  console.log('[Redirect Service Worker] Installing redirect service worker');
  self.skipWaiting();
});

// Activate event - take control immediately
self.addEventListener('activate', function(event) {
  console.log('[Redirect Service Worker] Activated, taking control');
  event.waitUntil(clients.claim());
});

// Fetch event - redirect all requests
self.addEventListener('fetch', function(event) {
  const requestUrl = new URL(event.request.url);

  // Only redirect requests to the exact old domain
  if (requestUrl.hostname === OLD_DOMAIN) {

    // Don't redirect the service worker itself or the config
    if (requestUrl.pathname === '/sw.js' ||
        requestUrl.pathname === '/_redirect/redirect-config.js') {
      return;
    }

    // Construct the new URL
    const newUrl = PROTOCOL + NEW_DOMAIN + requestUrl.pathname + requestUrl.search;

    console.log('[Redirect Service Worker] Redirecting:', event.request.url, '->', newUrl);

    // Use Response.redirect for 307 temporary redirect
    event.respondWith(
      Response.redirect(newUrl, 307)
    );
  }
});
