let voices = [];
const speech = new SpeechSynthesisUtterance();

// Configurações do speech
speech.volume = 1;      // 0 a 1 Volume da voz
speech.rate = 1;        // 0.1 a 10 Velocidade da voz
speech.pitch = 1;       // 0 a 2 Naturalidade da voz
speech.lang = 'pt-BR';  // Linguagem da voz

// Função que busca voz do Google ou Chama a voz padrão
function loadvoices() {
  voices = speechSynthesis.getVoices();
  console.log("lista de vozes:", voices);

  let selectedVoice = voices.find(v => v.name.includes("Google português do Brasil"));
  speech.voice = selectedVoice || voices[0];
}

speechSynthesis.onvoiceschanged = loadvoices;
loadvoices();

// Click no botão 
const speech_btn = document.querySelector("#button");

speech_btn.addEventListener('click', () => {
  let inputText = document.getElementById('inputText').value;

  speechSynthesis.cancel();

  if (inputText === '') {
    speech.text = 'Digite algo neste campo ao lado';
  } else {
    speech.text = inputText;
  }

  console.log("Voz selecionada:", speech.voice);
  speechSynthesis.speak(speech);
});
