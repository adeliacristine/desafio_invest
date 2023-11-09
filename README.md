# Desafio_invest

O desafio proposto tinha o objetivo de criar um sistema que auxilia os investidores em suas decisões de compra/venda de ativos. 
Foi desenvolvido um MVP (Minimum Viable Product) com as principais funcionalidades para ser apreciado pelos clientes.

## Funcionalidades Principais

### Cadastro de Ativos
O sistema possui uma tela inicial que permite o cadastro manual de ativos desejados. 
O usuário pode inserir o nome de sua ação preferida e os parâmetros necessários. 
Neste MVP, assumimos que os limites superiores e inferiores do túnel de preço são inseridos manualmente.

### Lista de Ativos
Há uma segunda interface que exibe todos os ativos cadastrados anteriormente no sistema. 
Nesta tela, os usuários podem remover ativos do sistema ou adicioná-los à lista de monitoramento.

### Monitoramento de Ativos
Ao adicionar um ativo à lista de monitoramento, o sistema passa a acompanhá-lo periodicamente. 
O usuário pode visualizar todos os parâmetros desse ativo e, sempre que as condições de compra ou venda forem atendidas, um e-mail de notificação é disparado.

## Vídeo Explicativo
Para uma melhor compreensão das funcionalidades, você pode assistir a um vídeo explicativo [aqui](https://www.loom.com/share/6954ccb5775a410ab43a2e8b5bc1cfc1?sid=72aa92a0-7009-430e-bbc1-cc61517d7c78).

## Melhorias Futuras
É importante ressaltar que este é apenas um MVP, e planejamos implementar melhorias no futuro:

1. **Cadastro de Usuários:** No momento, a aplicação é para um único usuário. Planejamos adicionar a funcionalidade de cadastro de usuários para que mais investidores possam utilizar o sistema.

2. **Lista de Ativos da API:** Em vez de cadastrar manualmente, pretendemos apresentar uma lista inicial de todos os ativos disponíveis na API e adicionar a funcionalidade de filtro para busca de ativos desejados.

3. **Melhorias de Layout:** Planejamos aprimorar o layout, incluindo mensagens de alerta automáticas, sem a necessidade de navegação por URLs.

4. **Cálculo de Volatilidade e Rentabilidade:** Pretendemos adicionar funcionalidades de cálculo de volatilidade e rentabilidade para fornecer uma análise mais abrangente na tomada de decisão de compra ou venda de ativos.

