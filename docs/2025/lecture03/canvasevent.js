const canvas_elem = document.getElementById('canvas');
const canvas_ctx = canvas_elem.getContext('2d');
let canvas_dragging = false;
let canvas_lastPos;

let canvas_stored_scolor = 'blue';
let canvas_stored_fcolor = 'blue';
let canvas_stored_width = 1;

let canvas_mouse_down_func = null;
let canvas_mouse_up_func = null;
let canvas_mouse_click_func = null;
let canvas_mouse_move_func = null;

let canvas_use_local_echo_flag = true;

function canvas_use_local_echo(on) {
  canvas_use_local_echo_flag = on;
}

function canvas_register_callback(type, func) {
  switch(type) {
  case 'down':
    canvas_mouse_down_func = func;
    break;
  case 'up':
    canvas_mouse_up_func = func;
    break;
  case 'click':
    canvas_mouse_click_func = func;
    break;
  case 'move':
    canvas_mouse_move_func = func;
    break;
  }
}

function canvas_old_move(pos) {
  if (canvas_dragging) {
    // #TODO# drawing
    canvas_store_style();
    canvas_default_style();
    canvas_drawLine(canvas_lastPos, pos);
    canvas_lastPos = pos;
    canvas_restore_style();
  }
}

function canvas_old_down(pos) {
  canvas_dragging = true;
  canvas_lastPos = pos;
}

function canvas_old_up(pos) {
  canvas_old_move(pos);
  canvas_dragging = false;
}

function canvas_old_click(pos) {

}

function canvas_event_pos(e) {
  const x = e.clientX - canvas_elem.getBoundingClientRect().left;
  const y = e.clientY - canvas_elem.getBoundingClientRect().top;
  return { x: x, y: y };
}

function strPair(pos) {
  return `(${pos.x}, ${pos.y})`;
}

function showMessage(message) {
  const current = document.getElementById('message').textContent;
  message = `${current}\n${message}`;
  document.getElementById('message').innerHTML = message;
}

function showMessageMouse(message) {
  document.getElementById('messageMouse').innerHTML = message;
}

//// send Methods
function sendDownMessage(pos) {
  const message = `mousedown${strPair(pos)}`;
  showMessage(message);
  document.getElementById('message').innerHTML = message;
}

function sendUpMessage(pos) {
  const message = `mouseup${strPair(pos)}`;
  showMessage(message);
  document.getElementById('message').innerHTML = message;
}

function sendClickMessage(pos) {
  const message = `click${strPair(pos)}`;
  showMessage(message);
  document.getElementById('message').innerHTML = message;
}

function sendMoveMessage(pos) {
  const message = `mousemove${strPair(pos)}`;
  showMessageMouse(message);
  document.getElementById('messageMouseMove').innerHTML = message;
}

//// receive Methods
function canvas_drawDot(pos) {
  canvas_ctx.beginPath();
  canvas_ctx.arc(pos.x, pos.y, 5, 0, Math.PI * 2, true);
  canvas_ctx.fill();
}

function canvas_drawLine(posa, posb) {
  canvas_ctx.beginPath();
  canvas_ctx.moveTo(posa.x, posa.y);
  canvas_ctx.lineTo(posb.x, posb.y);
  canvas_ctx.stroke();
}

function canvas_setColor(color) {
  canvas_ctx.strokeStyle = color;
  canvas_ctx.fillStyle   = color;
}

function canvas_setLineWidth(width) {
  canvas_ctx.lineWidth = width;
}

function canvas_default_style() {
  canvas_ctx.strokeStyle = 'blue';
  canvas_ctx.fillStyle   = 'blue';
  canvas_ctx.lineWidth   = 1;
}
function canvas_store_style() {
  canvas_stored_scolor = canvas_ctx.strokeStyle;
  canvas_stored_fcolor = canvas_ctx.fillStyle;
  canvas_stored_width  = canvas_ctx.lineWidth;
}
function canvas_restore_style() {
  canvas_ctx.strokeStyle = canvas_stored_scolor;
  canvas_ctx.fillStyle   = canvas_stored_fcolor;
  canvas_ctx.lineWidth   = canvas_stored_width;
}

function canvas_init() {
  let i;
  let message;

  canvas_default_style();

  canvas_elem.addEventListener('mousedown', (e) => {
    showMessage(`mousedown${strPair(canvas_event_pos(e))}`);
    showMessageMouse(`mousedown${strPair(canvas_event_pos(e))}`);
    let cur_pos = canvas_event_pos(e)
    if (canvas_mouse_down_func) {
      canvas_mouse_down_func(cur_pos);
    }
    if (canvas_use_local_echo_flag) {
      canvas_old_down(cur_pos);
    }
  });

  canvas_elem.addEventListener('mouseup', (e) => {
    showMessage(`mouseup${strPair(canvas_event_pos(e))}`);
    showMessageMouse(`mouseup${strPair(canvas_event_pos(e))}`);
    let cur_pos = canvas_event_pos(e)
    if (canvas_mouse_up_func) {
      canvas_mouse_up_func(cur_pos);
    }
    if (canvas_use_local_echo_flag) {
      canvas_old_up(cur_pos);
    }
  });

  canvas_elem.addEventListener('click', (e) => {
    showMessage(`click${strPair(canvas_event_pos(e))}`);
    showMessageMouse(`click${strPair(canvas_event_pos(e))}`);
    let cur_pos = canvas_event_pos(e)
    if (canvas_mouse_click_func) {
      canvas_mouse_click_func(cur_pos);
    }
    if (canvas_use_local_echo_flag) {
      canvas_old_click(cur_pos);
    }
  });

  canvas_elem.addEventListener('mousemove', (e) => {
    showMessageMouse(`mousemove${strPair(canvas_event_pos(e))}`);
    let cur_pos = canvas_event_pos(e)
    if (canvas_mouse_move_func) {
      canvas_mouse_move_func(cur_pos);
    }
    if (canvas_use_local_echo_flag) {
      canvas_old_move(cur_pos);
    }
  });

  let print_echo = document.getElementById("print_echo");
  if (print_echo) {
    print_echo.addEventListener("change", () => {
      console.log("change :" + print_echo.checked);
      canvas_use_local_echo(print_echo.checked);
    });
    //print_echo.addEventListener("input", () => {
    //  console.log("input :" + print_echo.checked);
    //});
  }
}

function canvas_clear() {
  canvas_ctx.clearRect(0, 0, canvas_elem.width, canvas_elem.height)

  document.getElementById('message').innerHTML = ''
  showMessageMouse('(cleared)')
}
