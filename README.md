# Automatização com Selenium e Python
Este é um projeto de automação básica desenvolvido em Python utilizando a biblioteca Selenium. O objetivo deste script é automatizar a navegação em um site de compras, realizar uma busca por um produto específico e coletar os preços encontrados.

# Requisitos
 - Python 3.x
 - Biblioteca Selenium
-  Driver do navegador (recomendado: ChromeDriver)
# Instalação
  1. Certifique-se de ter o Python 3.x instalado em seu sistema. Você pode baixá-lo em python.org.
  1. Instale a biblioteca Selenium executando o seguinte comando:
```bash
pip install selenium
```

3. Baixe o driver apropriado para o navegador que pretende usar. Neste exemplo, estamos usando o ChromeDriver, que pode ser baixado em ChromeDriver Downloads.
# Uso
  1. Clone este repositório em sua máquina local:

  ```bash
  git clone https://github.com/Caio-Rodrigues-V/Selenium-exercicios
  ```

  2. Abra o arquivo main.py em um editor de texto ou IDE de sua escolha.
  3. Modifique as coordenadas específicas do mouse na função country_selecion para adequá-las à sua resolução de tela.
# Execute o script Python:

   ```bash
   python main.py
    ```

# Notas importantes
Este script foi desenvolvido para fins educacionais e de aprendizado. Certifique-se de usá-lo de forma ética e respeitando os termos de serviço do site que está sendo automatizado.
O uso de pyautogui para interações com o mouse é uma medida de última instância e foi usado aqui para contornar medidas de segurança específicas do site. Recomenda-se explorar outras alternativas antes de recorrer a essa abordagem.
Esteja ciente de que a eficácia deste script pode variar dependendo de mudanças no site alvo, como atualizações de layout ou políticas de segurança.
