class RingBuffer {
  constructor ( size ) {
    this._length = 0;
    this._start = 0;
    this._size = size
    this._data = new Array(size)
    this._end  = size -1
    this._overflow_cb = null; // callback function, called when overflow is occurred

    this.pop   = this.get_back
    this.shift = this.get_front
    this.push  = this.add_back
    this.unshift = this.add_front
  }
  get size() {
    return this._size;
  }
  get length() {
    return this._length;
  }
  get_back () {
    //
    if (this._length === 0) return;

    //
    var elm = this._data[this._end];

    //
    delete this._data[this._end];

    this._end = (this._end - 1 + this._size) % this._size;
    this._length--;

    return elm;
  }
  get_front() {
    //
    if (this._length === 0) return;

    //
    var elm = this._data[this._start];

    //
    delete this._data[this._start];

    this._start = (this._start + 1) % this._size;
    this._length--;

    return elm;
  }
  _get_n(n, func) {
    if (n <= 0) {
      return;
    }
    var res = [];
    for(var i = 0; i < n; i++) {
      res.push( func.apply() )
    }
    return res;
  }
  get_backn (n) {
    return this._get_n(n, this.get_back.bind(this))// callback as method
  }
  get_frontn (n) {
    return this._get_n(n, this.get_front.bind(this))// callback as method
  }
  _add_back (elm) { // add_back for single item
    var new_end = this._end = (this._end + 1) % this._size;

    // if overflow_cb is set, and if data is about to be overwritten
    if (this._overflow_cb && this._length + 1 > this._size) {
      this._overflow_cb( this._data[new_end], this );
    }
    this._data[ new_end ] = elm;

    // recalculate length
    if (this._length < this._size) {
      if (this._length + 1 > this._size) {
        this._length = this._size;
      } else {
        this._length += 1;
      }
    }
    this._end = new_end;
    this._start = (this._size + this._end - this._length + 1) % this._size;
  }
  add_back() {
    if (arguments.length < 0) {
      return this.length;
    }
    for (var i = 0; i < arguments.length; i++) {
      this._add_back(arguments[i])
    }
    return this._length;
  }
  _add_front(elm) { // add_front for single item
    // if overflow_cb is set, and if data is about to be overwritten
    if (this._overflow_cb && this._length + 1 > this._size) {
      this._overflow_cb( this._data[ this._end ], this);
    }
    this._data[ (this._size + this._start - 1) % this._size ] = elm;

    // recalculate size
    if (this._size - this._length - 1 < 0) {
      this._end += this._size - this._length - 1;
      if (this._end < 0) {
        this._end = this._size + (this._end % this._size);
      }
    }
    // recalculate length
    if (this._length < this._size) {
      if (this._length + 1 > this._size) {
        this._length = this._size;
      } else {
        this._length += 1;
      }
    }
    this._start -= 1;
    if (this._start < 0) {
      this._start = this._size + (this._start % this._size);
    }
  }
  add_front() {
    if (arguments.length < 0) {
      return this.length;
    }
    for (var i = 0; i < arguments.length; i++) {
      this._add_front(argumehts[i])
    }
    return this._length;
  }
  unshift() {
    if (arguments.length < 0) {
      return this.length;
    }
    // for (var i = 0; i < arguments.length; i++) {
    for (var i = arguments.length - 1; i >= 0; i--) { // reverse order | same as javascript array
      this._add_front(argumehts[i])
    }
    return this._length;
  }
  get_all() {
    // not implemented
  }
  clear() {
    // this._size = size // no resize
    this._length = 0;
    this._start  = 0;
    this._data = new Array(this._size)
    this._end  = this._size -1
  }
};

class TopicBuffer extends RingBuffer
{
  constructor (size, callback = null )
  {
    super(size);
    this.callback = callback;
  }
};

class MessagePool {
//exports.MessagePool = class {
  constructor (_size = 100)
  {
    this.ws_client = null;
    this.topic_map = new Map();
    this.buffer_size = _size;
    this.publish_method = false;
    this.debug = false;
  }
  setPublishMethod(func)
  {
    this.publish_method = func;
  }
  // setSocket(sok)
  // {
  //   this.socket = sok;
  //   var self = this;
  //   self.socket.onmessage = function(e) {
  //     //console.log('recv message');//debug
  //     //console.log(self)
  //     //console.log(e.data);//debug
  //     self._receiveData(e.data);
  //   };
  // }
  static makeMessageStr(topic_name, data)
  {
    const msg = {
      hash: "TUTCPS",
      topic: topic_name,
      data:  data
    };
    const msg_str = JSON.stringify(msg);
    return msg_str;
  }
  publish(topic_name, data)//"topic_name", data)
  {
    if (this.publish_method) {
      const msg_str = MessagePool.makeMessageStr(topic_name, data);
      if (this.debug) {
        console.log('publish: ' + msg_str);
      }
      this.publish_method(msg_str);
    }
  }
  getMessage(topic_name, timeout = -1)// ("topic_name", timeout) => time, data
  {
    if ( this.topic_map.has(topic_name) ) {
      var buf = this.topic_map.get(topic_name);
      return buf.get_front()
    }
  }
  subscribe(topic_name, callback = null)//("topic_name", function=None)
  {
    if ( this.topic_map.has(topic_name) ) {
      // already subscribed
      var buf = this.topic_map.get(topic_name)
      if (callback) {
        if (buf.callback) {
          // overwrite callback
          buf.callback = callback
        } else {
          // add callback
          buf.callback = callback
        }
      }
    } else {
      this.topic_map.set(topic_name, new TopicBuffer(this.buffer_size, callback))
    }
  }
  // attribute
  get subscribingTopicList()
  {
    return Array.from(this.topic_map.keys())
  }
  get subscribingTopicIter()
  {
    return this.topic_map.keys();
  }
  //// private method
  _receiveData(instr) // when messageRecv
  {
    //parsing -> run callback -> store message
    var msg = JSON.parse(instr);
    if (this.debug) {
      console.log("revc: " + String(msg));
    }
    if (msg.hash != undefined && msg.hash == "TUTCPS") {
      if (msg.topic != undefined && msg.data != undefined) {
        if ( this.topic_map.has(msg.topic) ) {
          var buf = this.topic_map.get(msg.topic);
          if (this.debug) {
            console.log("cb_func: " + buf.callback);
          }
          //if (buf.callback && buf.callback.apply(buf, [msg.data])) {
          if (buf.callback && buf.callback(buf, [msg.data])) {
            if (this.debug) {
              console.log('do not stack message to buffer');
            }
            return;
          }
          if (this.debug) {
            console.log('stack message to buffer');
          }
          buf.push([new Date(), msg.data]);
        } else {
          console.log('receive not subscribing topic : ' + msg.topic);
          // receive not subscribing data
          //buf = new RingBuffer(this.buffer_size);
          //this.topic_map.set(msg.topic,  buf);
        }
      }
    }
  }
};

class WebMessage {
  constructor(addr, _size = 100)
  {
    this.addr = addr;
    this.connection = false;
    //this.ws_client = new WebSocket(this.addr);
    //this.msg_pool  = new MessagePool(_size);
    //this.msg_pool.setSocket(this.ws_client);

    this.connect();
  }
  connect()
  {
    this.ws_client = new WebSocket(this.addr);
    this.msg_pool  = new MessagePool(_size);
    this.msg_pool.setSocket(this.ws_client);

    this.ws_client.onerror = (e) => {
    };// bundle
    this.ws_client.onclose = (e) => {
      // connect
    };// bundle
  }
};

class BrowserMessage {
  constructor(hostwindow, _size = 100)
  {
    this.size = _size;
    this.hostwindow = hostwindow;
    this.connection = false;
    this.connect();
  }
  connect ()
  {
    this.msg_pool = new MessagePool(this.size);
    var pool = this.msg_pool;
    var host = this.hostwindow;
    this.msg_pool.setPublishMethod((instr) => {
      host.postMessage(instr, '*');
    });
    window.addEventListener("message", //// message from host
                            (ev) => {
                              //console.log('msg:' + ev.data);
                              pool._receiveData(ev.data);
                            }, false);
    this.connection = true;
  }
};
