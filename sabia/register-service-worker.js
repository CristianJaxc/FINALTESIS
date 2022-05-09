if ('serviceWorker')
{ window.addEventListener('load', function() { navigator.serviceWorker.register('/serviceworker.js'); }); }