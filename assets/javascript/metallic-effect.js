// Efeito metálico que segue o mouse nos cards
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('#projects-list > div');
    
    cards.forEach(card => {
        card.addEventListener('mousemove', function(e) {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Posiciona o efeito de luz onde o mouse está
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
        
        card.addEventListener('mouseleave', function() {
            // Remove as variáveis quando o mouse sai
            card.style.removeProperty('--mouse-x');
            card.style.removeProperty('--mouse-y');
        });
    });
});