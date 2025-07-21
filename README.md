
# Testes Automatizados com Selenium - SauceDemo

Este projeto realiza testes automatizados na aplicação [SauceDemo](https://www.saucedemo.com/) utilizando **Python** e **Selenium WebDriver**, com foco na validação do fluxo de compra e comportamento da interface do usuário.

---

## ✅ Cenários de Teste Cobertos

Para cada um dos usuários fornecidos pela plataforma (`standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user` e `visual_user`), o teste realiza o seguinte fluxo:

1. **Login** com credenciais válidas.  
2. **Verificação de redirecionamento** para a página de inventário.  
3. **Adição de todos os produtos ao carrinho.**  
4. **Navegação até o carrinho.**  
5. **Remoção de metade dos produtos do carrinho.**  
6. **Preenchimento de informações do usuário.**  
7. **Confirmação do pedido.**  
8. **Validação da finalização da compra.**  

Cada etapa é validada com `asserts`, exibindo mensagens de erro descritivas em caso de falha.

---

## 🧠 O Que o Código Faz (Fluxo e Validações)

O teste segue o **padrão Page Object Model (POM)**, separando responsabilidades por páginas da aplicação. A estrutura é composta por:

- **BasePage**: métodos genéricos para interação com elementos.  
- **Classes de Página**: como `LoginPage`, `CartPage`, `CheckoutPage` e `CompletePage`, representando partes da aplicação.  
- **Locators**: armazenam seletores CSS e identificadores dos elementos.

Cada função da classe `TestUsers` executa o fluxo completo descrito acima para um usuário específico.

Durante a execução:

- O código verifica o sucesso das navegações via `check_url` e a mensagem de confirmação da compra presente no final do fluxo.  
- Caso haja falha, uma mensagem de alerta (se presente) na interface é capturada e exibida.  
- O resultado de cada etapa é validado com `assertTrue` para garantir o funcionamento esperado.

---

## 📦 Instalação das Dependências

> Certifique-se de ter o Python instalado (versão 3.10 ou superior recomendada).

1. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
````

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

> **Requisitos principais:**
>
> * `selenium`
> * `Chrome WebDriver`

> **Chrome WebDriver:**
>
> * Instale uma versão compatível com a sua versão do Google Chrome neste link: [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)
> * Caso o caminho do WebDriver no seu computador seja diferente do configurado no arquivo `main.py` (variável PATH dentro da classe `SauceDemoTests`), ajuste-o conforme necessário.

---

## 🚀 Como Executar os Testes

Execute o seguinte comando no terminal:

```bash
python -m unittest test_saucedemo.py
```

Para exibir mais detalhes dos testes:

```bash
python -m unittest -v test_saucedemo.py
```

---

## 👨‍💻 Autor

Gabriel Diegues Figueiredo Rocha
Estudante de Engenharia de Software - FIAP
