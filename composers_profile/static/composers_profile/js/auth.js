var OAUTH2_CLIENT_ID = '660478359243-4u455gipq1lotnohau35apcph0sk4nmf.apps.googleusercontent.com';
var OAUTH2_SCOPES = [
  'https://www.googleapis.com/auth/youtube'
];

googleApiClientReady = function() {
  gapi.auth.init(function() {
    window.setTimeout(checkAuth, 1);
  });
}

function checkAuth() {
  gapi.auth.authorize({
    client_id: OAUTH2_CLIENT_ID,
    scope: OAUTH2_SCOPES,
    immediate: true
  });
}

function loadAPIClientInterfaces() {
    gapi.client.load('youtube', 'v3', function() {
    handleAPILoaded();
  });
}
function handleAPILoaded(){
    search();
}
function search(){

}
