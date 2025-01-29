# Documento de Visão

## Sistema de assinsstência para vestuário

### Histórico da Revisão 

|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 28/01/2025 |  **`1.00`** | Versão Inicial  | Gustavo Tavares e Isabella Camille |


### 1. Objetivo do Projeto 

O projeto **Cloud Wear** tem como objetivo fornecer uma solução eficiente e prática para a criação de combinações de roupas de acordo com a temperatura de um local selecionado.

### 2. Descrição do Problema 

|         __        | __   |
|:------------------|:-----|
| **_O problema_**    | Dificuldades para escolher roupas adequadas ao clima, criar combinações bonitas e condizentes com a atual situação climática de uma cidade. |
| **_afetando_**      | Pessoas com rotinas agitadas, profissionais, estudantes e qualquer um que tenha um guarda-roupa grande, mas dificuldade em escolher combinações, otimizar o tempo e planejar o que vestir. |
| **_cujo impacto é_**| Perda de tempo na escolha de roupas, aumento da indecisão, frustração com a falta de combinações eficientes e, muitas vezes, um guarda-roupa subutilizado ou mal aproveitado. |
| **_uma boa solução seria_** | Fornecer sugestões utilizando as peças do guarda roupas usuário de acordo com o clima da cidade selecionada, organizar o guarda roupas dando visão das peças que o usuário possui. |

### 3. Descrição dos Usuários

| Nome | Descrição | Responsabilidades |
|:---  |:--- |:--- |
| Administrador  | Gerencia as configurações do sistema | Mantém o cadastro dos usuários e realiza ajustes no sistema |
| Cliente | Realiza as atividades relacionadas ao gerenciamento do guarda roupas e geração de combinações | Realiza o próprio cadastro no sistema; Adicionar e remover peças do guarda roupas; Gerar combinações utilizando as peças cadastradas no guarda roupas|

### 4. Descrição do Ambiente dos Usuários

No cotidiano, muitas pessoas enfrentam dificuldades para escolher rapidamente o que vestir, especialmente profissionais, estudantes ou quem possui um guarda-roupa grande. O processo de selecionar roupas adequadas para o dia a dia pode ser demorado e, muitas vezes, pouco eficiente.

Atualmente, a maioria das pessoas precisa escolher suas combinações de forma manual, o que consome tempo e energia. Para pessoas com rotinas agitadas, isso pode se tornar um desafio constante.

A ideia central da aplicação é permitir que os usuários registrem suas roupas digitais e gerem combinações de roupas com base na temperatura da cidade escolhida. Isso proporciona uma maneira mais ágil e prática de planejar o que vestir, economizando tempo e tornando a escolha de roupas mais eficiente.

### 5. Principais Necessidades dos Usuários

Para empresas e profissionais, a necessidade é divulgar sua disponibilidade de atendimentos para viabilizar, de forma mais eficiente, o atendimento dos seus clientes.

Para os clientes, as necessidades são encontrar profissionais e empresas prestadoras de serviço e agendar atendimentos com estes de acordo as disponibilidades de tempo dos envolvidos.

### 6.	Alternativas Concorrentes

As alternativas concorrentes geralmente se concentram em organização de looks manuais ou recomendação de peças individuais. A proposta desta aplicação é oferecer uma solução simples e acessível para a escolha de combinações de roupas, considerando tanto o guarda-roupa do usuário quanto a temperatura da cidade selecionada.

### 7.	Visão Geral do Produto

Em resumo, o Sistema de assistência para vestuário, o Cloud Wear, tem por objetivo ajudar os usuários com uma rotina muito agitada, ou quem tem muitas peças de roupa no guarda roupas a montar combinações de roupas que combinem entre si e que sejam eficientes na questão climática, pois o sistema escolherá uma combinação usando as peças cadastradas do usuário e também com bvase no clima da cidade selecionada pelo usuário.

### 8. Requisitos Funcionais

| Código | Nome | Descrição |
|:---  |:--- |:--- |
| RF01 | Entrar no sistema | Usuários devem logar no sistema para acessar as funcionalidades relacionadas ao agendamento |
| RF02 | Cadastro de Funcionários | Administrador do sistema mantém o cadastro dos funcionários responsáveis pelo gerenciamento das agendas |
| RF03 | Gerenciamento de Serviços |  Funcionário mantém a relação de serviços prestados pela empresa ou profissional |
| RF04 | Gerenciamento da Agenda | Funcionário registra os horários disponíveis de atendimento, confirma e cancela o agendamento de clientes |
| RF05 | Cadastro de Clientes | Cliente deve realizar o auto cadastramento |
| RF06 | Consulta de Agendas | Cliente consulta agendas de atendimento dos serviços disponíveis, podendo agendar um serviço  |
| RF07 | Consulta de Agendamento | Cliente consulta atendimentos agendados, podendo cancelar um agendamento |


### 9. Requisitos Não-funcionais

 Código | Nome | Descrição | Categoria | Classificação
|:---  |:--- |:--- |:--- |:--- |
| RNF01 | Design responsivo | O sistema deve adaptar-se a qualquer tamanho de tela de dispositivo, seja, computador, tablets ou smart phones. | Usabilidade| Obrigatório |
| RNF02 | Criptografia de dados| Senhas de usuários devem ser gravadas de forma criptografada no banco de dados. | Segurança | Obrigatório |
| RNF03 | Controle de acesso | Só usuários autenticados podem ter acesso ao sistema, com exceção ao auto cadastramento do usuário. | Segurança | Obrigatório |
| RNF04 | Tempo de resposta |A comunicação entre o servidor e o cliente deve ocorrer em tempo hábil | Performance | Desejável |
| RNF05 | Sistema Web | A aplicação deve ser um site. | Arquitetura | Obrigatório |
| RNF06 | Dados pessoais | Os clientes não devem visualizar dados de outros clientes (na agenda, por exemplo). | Privacidade | Obrigatório |