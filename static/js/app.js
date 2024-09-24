const socket = io({autoConnect: false});
socket.connect();

function rgbToHex(r, g, b){
    const hexR = r.toString(16).padStart(2, '0');
    const hexG = g.toString(16).padStart(2, '0');
    const hexB = b.toString(16).padStart(2,'0');

    return `#${hexR}${hexG}${hexB}`;
}


socket.on('common_colors', function(data){
    let colors = data.colors;
    const target = document.getElementById('result');
    target.innerHTML = '';
    for(let rbg_color of colors[0]){
          let div = document.createElement('div');
          let container = document.createElement('div');
          let p = document.createElement('p');
          div.classList.add('color');
          div.style.backgroundColor = `rgb(${rbg_color[0]}, ${rbg_color[1]}, ${rbg_color[2]}`;
          p.textContent = rgbToHex(rbg_color[0], rbg_color[1], rbg_color[2])
          container.classList.add('container');
          container.appendChild(div);
          container.appendChild(p);
          target.appendChild(container);
    }
})

