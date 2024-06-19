
# Recaptcha Solver

Este projeto fornece uma solução automatizada para resolver reCAPTCHAs auditivos usando Selenium e reconhecimento de fala. 

## Descrição

O script `recaptcha_solver.py` contém uma classe `RecaptchaSolver` que facilita o download, conversão e reconhecimento de áudio de reCAPTCHAs auditivos. Utiliza Selenium para automação da web e a biblioteca `speech_recognition` para transcrever o áudio.

## Pré-requisitos

- Python 3.x
- Selenium
- Pydub
- SpeechRecognition
- ffmpeg (para conversão de áudio)
- Webdriver para o navegador que será usado (ChromeDriver, GeckoDriver, etc.)

## Instalação

1. Clone este repositório.
2. Instale os pacotes Python necessários:
    ```bash
    pip install selenium pydub SpeechRecognition webdriver-manager
    ```
3. Certifique-se de que o `ffmpeg` está instalado no seu sistema. Você pode seguir as instruções de instalação [aqui](https://ffmpeg.org/download.html).

## Uso

### Script de Exemplo

O [script exemplo](https://github.com/wallesom/reCAPTCHA-Solver/blob/master/script_exemplo.py) mostra um exemplo de como utilizar a classe `RecaptchaSolver` para resolver um reCAPTCHA auditivo.

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from recaptcha_solver import RecaptchaSolver  # Supondo que o arquivo seja nomeado como recaptcha_solver.py

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get('link-que-contem-um-recaptcha')  # Substitua pela URL real onde deseja resolver o reCAPTCHA

solver = RecaptchaSolver(driver)
solver.solve_recaptcha(
    captcha_iframe_xpath='/html/body/div[1]/div/div[1]/section/form/div[3]/div/div/iframe',
    captcha_button_xpath='/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]',
    audio_challenge_iframe_xpath='/html/body/div[3]/div[4]/iframe',
    audio_button_id='recaptcha-audio-button',
    audio_source_xpath='/html/body/div/div/div[7]/a',
    audio_response_id='audio-response',
    verify_button_id='recaptcha-verify-button'
)

driver.quit()
```

### Métodos da Classe `RecaptchaSolver`

- `__init__(self, driver)`: Inicializa a classe com o objeto driver do Selenium.
- `download_audio(self, src, dest)`: Faz o download do arquivo de áudio a partir de uma URL.
- `convert_audio(self, mp3_path, wav_path)`: Converte um arquivo de áudio de MP3 para WAV.
- `recognize_audio(self, wav_path)`: Transcreve o áudio usando a biblioteca `speech_recognition`.
- `solve_recaptcha(self, captcha_iframe_xpath, captcha_button_xpath, audio_challenge_iframe_xpath, audio_button_id, audio_source_xpath, audio_response_id, verify_button_id)`: Realiza o processo completo de resolver o reCAPTCHA auditivo.

### Executando o Script

Para executar o script de exemplo:
1. Atualize os `xpath` e `id` conforme necessário para corresponder à estrutura do reCAPTCHA da página que você está automatizando.
2. Execute o script de exemplo:
    ```bash
    python script_exemplo.py
    ```