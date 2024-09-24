const socket = io({autoConnect: false});
socket.connect();


socket.on('common_colors', function(data){
    let colors = data.colors;
    const target = document.getElementById('result');
    console.log(target);
    for(let rbg_color of colors[0]){
          let div = document.createElement('div');
          div.classList.add('color');
          div.style.backgroundColor = `rgb(${rbg_color[0]}, ${rbg_color[1]}, ${rbg_color[2]}`;
          target.appendChild(div);
    }
})