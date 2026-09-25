# Rodrigo Niskier — portfólio visual

[**Abrir o portfólio**](https://rn-dev-portfolio-orcin.vercel.app)

Vitrine pública de aplicações web, IA aplicada e automação. HTML, CSS e JavaScript, sem backend, dependências de runtime ou serviços pagos de IA.

## Demonstrações

| Projeto | Demo | Código |
| --- | --- | --- |
| ExamForge AI | [Abrir](https://rn-examforge-demo.vercel.app) | [GitHub](https://github.com/rodrigoniskier/ExamForgeAI) |
| ClinicalTrack | [Abrir](https://rn-clinicaltrack-demo.vercel.app) | [GitHub](https://github.com/rodrigoniskier/ClinicalTrack) |
| ServiceFlow | [Abrir](https://rn-serviceflow-demo.vercel.app) | [GitHub](https://github.com/rodrigoniskier/ServiceFlow) |
| TeamMural | [Abrir](https://rn-teammural-demo.vercel.app) | [GitHub](https://github.com/rodrigoniskier/TeamMural) |

Todos os dados das quatro demos são sintéticos. O ExamForge AI usa geração e revisão simuladas, sem chamadas a APIs de IA. O acesso é feito pelos botões das páginas iniciais, sem senha pública.

## Capturas e interface

Dez capturas reais das aplicações online, verificadas no navegador e convertidas para WebP. As galerias têm legendas, controles por teclado e textos alternativos. Layout adaptável, imagens com dimensões reservadas e carregamento tardio abaixo da dobra. Links diretos para seis projetos complementares, contato por e-mail, LinkedIn e GitHub.

## Desenvolvimento

```bash
python -m http.server 8000
node --check script.js
python verify.py
```

Edite `index.html`, `style.css` e `script.js`; `projects.json` registra os dados dos cases. `screens/` contém somente imagens demonstrativas, sem tokens ou informações privadas.

## Publicação

Repositório conectado à Vercel: alterações em `main` geram deploy automático e executam GitHub Actions. Metadados de compartilhamento, favicon e URL canônica configurados. Nenhuma variável secreta é necessária para o portfólio.

As aplicações Python usam projetos Neon independentes no plano gratuito. A primeira abertura pode demorar alguns segundos após inatividade do banco.
