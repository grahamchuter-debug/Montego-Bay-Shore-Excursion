/**
 * Montego Bay Shore Excursion — Workers Assets entry.
 * www → apex (one hop); .html → trailing-slash path (one hop); combined when both apply.
 * Query strings preserved. Soft homepage 404s eliminated via ASSETS 404-page.
 */
const APEX_HOST = 'montegobayshoreexcursion.com';

function stripHtmlPath(pathname) {
  if (!pathname.toLowerCase().endsWith('.html')) return pathname;
  let path = pathname.slice(0, -5);
  if (path.toLowerCase().endsWith('/index')) path = path.slice(0, -6);
  if (path === '' || path === '/index') path = '/';
  if (path !== '/' && !path.endsWith('/')) path += '/';
  return path || '/';
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname.toLowerCase();
    const isWww = host === `www.${APEX_HOST}`;
    const hasHtml = url.pathname.toLowerCase().endsWith('.html');
    const isHttp = url.protocol === 'http:';

    if (isWww || hasHtml || isHttp) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      if (hasHtml) dest.pathname = stripHtmlPath(url.pathname);
      else if (isWww || isHttp) {
        let p = url.pathname || '/';
        if (p !== '/' && !p.endsWith('/') && !p.includes('.')) p += '/';
        dest.pathname = p;
      }
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    // Extensionless without trailing slash → trailing slash (preserve equity)
    const path = url.pathname || '/';
    if (
      path !== '/' &&
      !path.endsWith('/') &&
      !path.includes('.') &&
      host === APEX_HOST
    ) {
      const dest = new URL(url.toString());
      dest.pathname = path + '/';
      return Response.redirect(dest.toString(), 301);
    }

    const assetResponse = await env.ASSETS.fetch(request);

    if (assetResponse.status === 404) {
      const notFound = await env.ASSETS.fetch(new URL('/404.html', url.origin));
      return new Response(notFound.body, {
        status: 404,
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'cache-control': 'no-store',
        },
      });
    }

    return assetResponse;
  },
};
