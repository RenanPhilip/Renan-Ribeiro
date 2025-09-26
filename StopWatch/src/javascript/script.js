const power = document.getElementById('power');
const mark = document.getElementById('mark');
const pause = document.getElementById('pause');
const resetButton = document.getElementById('reset');

let timerEl = document.getElementById('timer');

let marksList = document.getElementById('marks-list');
let lapList = 0
newLap = (txt) => {
    lapList++;
    let p = document.createElement('p');
    p.innerHTML = `• Marca ${lapList.toString().padStart(2,'0')} : ${txt}`;
        marksList.appendChild(p);
        marksList.scrollTop = marksList.scrollHeight
}
// newLap("12:12:12'12");

var time = 0;
let intervalId = 0;
let isRunning = false;

const formatTime = (time) => {
 const hh = Math.floor(time / 360000);
 const mm = Math.floor((time % 360000) / 6000);
 const ss = Math.floor((time % 6000) / 100);
 const ms = time % 100;

    return `${hh.toString().padStart(2, '0')}:${mm.toString().padStart(2, '0')}:${ss.toString().padStart(2, '0')}'${ms.toString().padStart(2, '0')}`;
}

const toggleTimer = () => {
    const button = document.querySelector('#power');
    const action = button.getAttribute('action');

    if (action === 'start' || action === 'continue') {

        intervalId = setInterval(() => {
            time +=1;
            setTimer(time);
        }, 10);
        button.setAttribute('action', 'pause');
        button.innerHTML = '<i class="fa-solid fa-pause"></i>';
    }
    else if (action === 'pause'){
        button.setAttribute('action', 'continue');
        button.innerHTML = '<i class="fa-solid fa-play"></i>';
        clearInterval(intervalId);
    }


}

const setTimer = (time) => {
        timerEl.innerHTML = formatTime(time);
}
resetButton.addEventListener('click', () => {
    clearInterval(intervalId)
    const button = document.querySelector('#power');
    button.setAttribute('action', 'start');
    marksList.innerHTML=''
    time=0
    lapList=0
    timerEl.innerHTML = formatTime(time)
    button.innerHTML = '<i class="fa-solid fa-play"></i>';

});

power.addEventListener('click', () => {
    toggleTimer();
});
let lastMark = 0

mark.addEventListener('click', () => {
    if (time!=0 && time != lastMark){
        newLap(formatTime(time));
        lastMark = time
    }
});

pause.addEventListener('click', () => {
    newLap(formatTime(time));
    clearInterval(intervalId);
});

