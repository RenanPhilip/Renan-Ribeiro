let selectSeconds = document.querySelector('#selectSeconds')
let timeSelected = document.querySelectorAll('#timer')
const iniciar = document.querySelector('#iniciar')
const timerDisplay = document.getElementById('timerSelected');
let countdownInterval;
// let calcIdade = document.querySelector('#calcIdade')
let idadeInput = document.querySelector('#idade')

// idadeInput.addEventListener('blur', ()=>{
//     let batimento_medio = 220 - Number(idadeInput.value)
//     if(idadeInput != ""){
//         calcIdade.innerHTML = `Os batimentos deves estar no maiximo de: <br>${batimento_medio} <br> por minuto`
//     }
// })

function timeSec (){
    let timeSelected = document.querySelectorAll('#timer')
    let n = 0
    timeSelected.forEach((e)=>{
        if(e.checked){
            n  = e.alt
        }
    })
    return Number(n)
}

selectSeconds.addEventListener('click', ()=>{
    document.querySelector("#batimentos").innerHTML=''
    timeSec()
    console.log(timeSec())
})



function bpsInput() {
    const batimentos = document.querySelector('#batimentos');

    // Cria o input apenas se ainda não existir
    if (!document.querySelector('#batimentosInput')) {
        const bps = document.createElement("input");
        bps.type = 'number';
        bps.name = "batimentosInput";
        bps.id = "batimentosInput";
        bps.placeholder = "Batimentos Contados";

        batimentos.appendChild(bps);
        function addValor(){
            const valorBatimentos = Number(bps.value);
            console.log("Batimentos digitados:", valorBatimentos);

            // Aqui você pode fazer qualquer cálculo ou atualização
            // Exemplo: calcular BPM por minuto baseado no tempo selecionado
            const segundos = timeSec();
            if (segundos > 0 && valorBatimentos > 0) {
                const bpmPorMinuto = (60 / segundos) * valorBatimentos ;
                console.log(`BPM estimado: ${bpmPorMinuto.toFixed(1)}`);
                
                bpm = document.createElement('p')
                bpm.innerHTML = `BPM aproximado: ${bpmPorMinuto.toFixed(1)}
                <br>Os batimentos podem estar variando entre ${(bpmPorMinuto-10)} e ${(bpmPorMinuto+10)}`
                
                batimentos.appendChild(bpm)

            }
        }

        // Adiciona o listener para capturar o valor após o usuário digitar
        bps.addEventListener('blur', () => {
            addValor()
        });

        // Chama handle ao pressionar Enter
        bps.addEventListener('keydown', (e) => {
            if (e.key === "Enter") {
                e.preventDefault(); // evita submit de forms
                addValor()
            }
        });
    }
}


let interval = (time)=>{
    setInterval(()=>{
    },time)
}

function startCountdown(seconds) {
    clearInterval(countdownInterval);
    let remaining = seconds;

    function updateDisplay() {
        const min = Math.floor(remaining / 60);
        const sec = remaining % 60;
        timerDisplay.textContent = `${String(min).padStart(2,'0')}:${String(sec).padStart(2,'0')}`;
    }

    updateDisplay();

    countdownInterval = setInterval(() => {
        remaining--;
        if (remaining < 1) {
            clearInterval(countdownInterval);
            timerDisplay.textContent = "Informe quantos batimentos contou";
            bpsInput()
            return;
        }
        updateDisplay();
    }, 1000);
}

function startPreparation(prepSeconds, mainSeconds) {
    clearInterval(countdownInterval);
    let remaining = prepSeconds;

    timerDisplay.textContent = `Prepare-se para iniciar a contagem em ${remaining}s`;

    countdownInterval = setInterval(() => {
        remaining--;
        if (remaining < 1) {
            clearInterval(countdownInterval);
            startCountdown(mainSeconds); // Cronometro principal após a preparação
            return;
        }
        timerDisplay.textContent = `Prepare-se para iniciar a contagem em ${remaining}s`;
    }, 1000);
}

iniciar.addEventListener('click', () => {
    const segundos = timeSec();
    batimentos.innerHTML = '' 
    if (segundos > 0) {
        startPreparation(5, segundos); // Preparação + Tempo selecioado no radio
    } else {
        alert("Selecione um tempo válido!");
    }
});
