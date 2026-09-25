# Verificação da entrega — 25/09/2026

## Sites publicados

| Projeto | URL | Fluxo verificado no navegador |
| --- | --- | --- |
| Portfólio | https://rn-dev-portfolio-orcin.vercel.app | Navegação, quatro cases, imagens carregadas, galeria, contato e viewport mobile |
| ClinicalTrack | https://rn-clinicaltrack-demo.vercel.app | Gestor, supervisor, trainee, placements, registro de avaliação e feedback visível ao trainee |
| ServiceFlow | https://rn-serviceflow-demo.vercel.app | Cadastro, busca da referência criada, detalhe, filtros, download CSV e Excel |
| ExamForge AI | https://rn-examforge-demo.vercel.app | Rascunho simulado, revisão humana, revisão simulada, montagem de cinco itens, gabarito e download Blackboard |
| TeamMural | https://rn-teammural-demo.vercel.app | Canal geral, conversa individual, envio e leitura persistente, download do anexo sintético |

## Evidências

- Dez screenshots reais em `screens/`, com duas ou três telas por aplicação, convertidas para WebP.
- Capturas do portfólio: [desktop](portfolio-desktop.jpg) e [mobile](portfolio-mobile.jpg).
- A largura mobile foi verificada no Chrome em iframe de mesma origem com viewport 390 × 844, usando `qa/responsive.html`. A área útil tinha 375 px e nenhuma rolagem horizontal. Galeria e contato foram exercitados nesse viewport. Isso é uma verificação de layout responsivo, não um teste em aparelho físico.
- CSV e Excel filtrados baixados e abertos: uma demanda fictícia, nove colunas. Blackboard baixado: cinco itens com marcação de respostas. Anexo TXT do TeamMural conferido.
- PostgreSQL após os testes: ClinicalTrack com 20 placements e 41 avaliações; ServiceFlow com 57 demandas; ExamForge AI com 33 questões e três avaliações; TeamMural com sete membros e 23 mensagens. Os registros criados no navegador permaneceram entre requisições e novos deploys.
- Suítes GitHub Actions aprovadas nas branches principais. Vercel com deploy automático conectado a `main` nos cinco repositórios.
- Correção de integração: `Referrer-Policy: same-origin` mantém a origem das submissões protegidas por CSRF.
- Correção de carga: duplicatas legítimas criadas por visitantes não impedem o reseed nem substituem registros existentes. Testes de regressão adicionados em ExamForge AI e ServiceFlow.

## Limites e segurança

Somente os quatro repositórios públicos sanitizados, o novo portfólio e o README público do perfil foram alterados. Os sistemas privados originais não foram acessados nem modificados.

As aplicações estão em modo `PORTFOLIO_DEMO=1`. O ExamForge força IA simulada e usa `USE_FAKE_AI=1`; nenhuma API paga foi utilizada. Há dados sintéticos, limites de escrita, proteção de registros-base, CSRF, cookies seguros e bloqueio dos painéis administrativos desnecessários. Upload público desabilitado.

Os visitantes devem usar somente conteúdo fictício: as contas são demonstrações compartilhadas. Não são serviços de produção para dados confidenciais.

Varredura dos arquivos públicos sem secrets, bases SQLite, dumps ou arquivos `.env` rastreados. Credenciais de infraestrutura ficam nas variáveis da plataforma.

Vercel Hobby e quatro projetos Neon gratuitos e independentes. Nenhum cartão cadastrado, upgrade, API paga ou serviço pago contratado. Os limites dos planos gratuitos continuam aplicáveis; a primeira abertura após inatividade pode levar alguns segundos.
