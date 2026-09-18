LOG: 
Estou criando um sistema com login para retornar quando o usuario estiver logado a quantidade de vagas por setor ou todas. Com alerta de vaga reservadas.
Precisei arrumar o código base que a IA me deu para quando criar a conta mandar o usuário para o menu direto.
Também melhorei a documentação das funções.

Requisitos Cobertos:
- Autenticação: Login e criação de contas com persistência em CSV e senhas codificadas em Base64.
- Gestão de Vagas: Consulta geral, cálculo dinâmico de vagas disponíveis (totais - ocupadas) e busca por setor.
- Alertas de Restrição: Exibição automática de alerta visual para setores com vagas reservadas/exclusivas.

Como Funciona:
O sistema inicia criando os bancos CSV se necessário. O usuário se autentica ou cria conta (sendo redirecionado ao menu) e pode navegar pelo menu CLI para consultar o status atual e avisos de cada setor em tempo real.

Como Executar:
Certifique-se de ter o Python 3 instalado e execute no terminal: python main.py

AUTOAVALIAÇÃO:

Executei o protótipo e os 3 critérios definidos foram atendidos parcialmente, com muitas melhorias que foram identificadas. Não é mais fácil de traduzir em código, acho que se tivesse uma lista de requisitos melhor talvez fosse mais fácil. A IA me deu um código base nos requisitos que a pedi para contemplar. Mas o código dela as vezes acaba sendo mais complexo e grande desnecessáriamente, e precisei refatorar certas coisas. Tempo e não familiaridade no PY foram contratempos. 

LINK CHAT IA GEMINI: https://gemini.google.com/app/e71088266424f30e