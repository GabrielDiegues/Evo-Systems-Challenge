````markdown
# Testes Automatizados com Selenium - SauceDemo

Este projeto realiza testes automatizados na aplicação [SauceDemo](https://www.saucedemo.com/) utilizando **Python** e **Selenium WebDriver** com foco em validação de fluxo de compra e comportamento da interface do usuário.

---

## ✅ Cenários de Teste Cobertos

Para cada um dos usuários fornecidos pela plataforma (`standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user` e `visual_user`), o teste realiza o seguinte fluxo:

1. **Login** com credenciais válidas.
2. **Verificação de redirecionamento** para a página de inventário.
3. **Adição de todos os produtos ao carrinho.**
4. **Navegação até o carrinho.**
5. **Remoção de metade dos produtos do carrinho.**
8. **Preenchimento de informações do usuário.**
9. **Confirmação do pedido.**
10. **Validação da finalização da compra.**

Cada etapa é validada com `asserts`, e mensagens de erro descritivas são exibidas quando algo falha.

---

## 🧠 O Que o Código Faz (Fluxo e Validações)

O teste segue o **padrão Page Object Model (POM)**, separando responsabilidades por páginas da aplicação. A estrutura é composta por:

- **BasePage**: contém métodos genéricos para interação com elementos.
- **Classes de Página**: como `LoginPage`, `CartPage`, `CheckoutPage` e `CompletePage`, cada uma representando uma parte da aplicação.
- **Locators**: armazenam os seletores CSS de elementos.

Cada função da classe `TestUsers` executa o fluxo completo descrito acima para um usuário específico.

Durante a execução:

- O código verifica o sucesso de navegações via `check_url` e a mensagem de confimação da compra, presentde no final do fluxo.
- Caso haja falha, é capturada uma mensagem de alerta (se presente) na interface.
- O resultado de cada etapa é validado com `assertTrue`.

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
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

> **Requisitos principais:**
> * `selenium`
> * `Chrome Web driver`

> **Chrome Web Driver:**
> * `Instale uma versão compatível com o seu browser por meio deste link: https://googlechromelabs.github.io/chrome-for-testing/`
> * `Se o caminho para o web driver instalado no seu computador for diferente do armazenado na variável PATH, presente na classe SauceDemoTests, localizada no arquivo main.py, mude a variável para conter o caminho localizado no seu computador`
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
