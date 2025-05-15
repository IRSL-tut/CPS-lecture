//
//
//
if (window.name) {
  document.title = window.name;
}

// global variables
const myGlobal = {};

// settings of myGlobal.BM
function setupMessageBuffer(buffer_size=1, force_websocket=false)
{
  const url = new URL(window.location);
  const params = url.searchParams;

  if (force_websocket || params.size > 0 || !window.opener) {
    const wshost = (() => {
      let res = params.get('host');
      if (res) {
        return res;
      } else {
        return 'localhost';
      }
    })();
    const wsport = (() => {
      let res = params.get('port');
      if (res) {
        return res;
      } else {
        return '5001';
      }
    })();
    const ssl = (() => {
      let res = params.get('ssl');
      console.log(res);
      if (res && ( res == "true" || res > 0 )) {
        console.log('true');
        return true;
      } else {
        console.log('false');
        return false;
      }
    })();
    let ws_url;
    if (ssl) {
      ws_url = 'wss://' + wshost + ':' + wsport;
    } else {
      ws_url = 'ws://' + wshost + ':' + wsport;
    }
    console.log('server address: ' + ws_url);
    myGlobal.BM = new WebMessage(ws_url, buffer_size);
    myGlobal.BM.msg_pool.debug = false;
    if (ssl) {
      myGlobal.connection_type = 'websocket';
    } else {
      myGlobal.connection_type = 'websocket(ssl)';
    }
  } else {
    myGlobal.opener = window.opener;
    myGlobal.BM = new BrowserMessage(myGlobal.opener, buffer_size);
    myGlobal.BM.msg_pool.debug = false;
    myGlobal.connection_type = 'browser';
  }
};
//setupMessageBuffer();
