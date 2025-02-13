const speech = new SpeechSynthesisUtterance();
//Configurações do speech
speech.text = 'Olá. Eu sou o script de configuração do speech!';
speech.volume = 1;      // 0 a 1  Volume da voz
speech.rate = 1;        // 0.1 a 10 Velocidade da voz
speech.pitch = 2;       // 0 a 2 Natularidade da voz
speech.lang = 'pt-BR';  // Linguagem da voz
speechSynthesis.speak(speech);

document.querySelector("#button").addEventListener('click', () => {
    inputText = document.getElementById('inputText').value;
    if(inputText == ''){
        speech.text = 'Você precisa digitar algo para eu poder falar!';
    }else{
        speech.text = inputText;
    }
    speechSynthesis.speak(speech);
});     