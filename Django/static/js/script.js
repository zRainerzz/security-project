function vigenereCipher(text, key, encrypt) {
    let result = '';
    const cleanKey = key.toUpperCase().replace(/[^A-Z]/g, '');
    
    if (!cleanKey) return '';
    
    let keyIndex = 0;
    
    for (let i = 0; i < text.length; i++) {
        if (!/[A-Za-z]/.test(text[i])) {
            result += text[i];
            continue;
        }
        
        const isUpperCase = text[i] === text[i].toUpperCase();
        const textChar = text[i].toUpperCase().charCodeAt(0);
        const keyChar = cleanKey.charCodeAt(keyIndex % cleanKey.length);
        
        let processedChar;
        if (encrypt) {
            processedChar = String.fromCharCode(((textChar + keyChar - 130) % 26) + 65);
        } else {
            processedChar = String.fromCharCode(((textChar - keyChar + 26) % 26) + 65);
        }
        
        result += isUpperCase ? processedChar : processedChar.toLowerCase();
        keyIndex++;
    }
    
    return result;
}

document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text');
    const keyInput = document.getElementById('key');
    const resultOutput = document.getElementById('result');
    const encryptButton = document.getElementById('encrypt');
    const decryptButton = document.getElementById('decrypt');
    const loadingElement = document.getElementById('loading');

    function processText(encrypt) {
        const text = textInput.value;
        const key = keyInput.value;

        loadingElement.style.display = 'flex';

        setTimeout(() => {
            const result = vigenereCipher(text, key, encrypt);
            resultOutput.value = result;
            loadingElement.style.display = 'none';
        }, 1000);
    }

    encryptButton.addEventListener('click', () => processText(true));
    decryptButton.addEventListener('click', () => processText(false));
});

