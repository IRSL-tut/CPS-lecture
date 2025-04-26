function getID() {
  let N=16
  return btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(N)))).substring(0,N);
}
////
function registerProc(id, args) {
  let obj = {args: args, start: true, count: 0};
  myGlobal.proc_map.set(id, obj);
}
function deleteProc(id) {
  if (myGlobal.proc_map.has(id)) {
    myGlobal.proc_map.delete(id);
  }
}
function doProc() {
  let lst = Array.from(myGlobal.proc_map.keys());
  let obj = null;
  let key = null;
  if (lst.length > 0) {
    key = lst[0]
    obj = myGlobal.proc_map.get(key)
  }
  if(key) {
    let res = myGlobal.proc_func(obj);
    if (res) {
      myGlobal.proc_map.delete(key);
      return [key, res];
    } else {
      return false;
    }
  }
  return false;
}
function setProcFunction(func) { //// func = function(obj) { ... };
  myGlobal.proc_func = func;
}
