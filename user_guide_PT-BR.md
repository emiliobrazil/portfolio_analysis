<h1>GUIA DO USUARIO</h1>
<h2>Requisitos e sistema operacional</h2>
Para que o aplicativo funcione adequadamente o mesmo deve operar em:

1) um ambiente com python 3.4 (ou superior)

2) processador com no minimo 2 nucleos e 2GHz
   
3) no minimo 4GB de RAM

Embora não seja um requisito o aplicativo foi testado e aprovado
nos seguintes sistemas operacionais:

1) Windows 11

2) Windows 10

3) Linux UBbuntu 23.04

Em outros sistemas operacionais não há garantia de 
estabilidade, abertura ou funcionamento do programa

<h2>Utilizando o app</h2>
Guia de uso do aplicativo
<h3> Tela inicial</h3>

Ao iniciar o aplicativo a seguinte tela será apresentada

![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/35ca9125-f8d3-44fc-a9c5-9b7aa83b48ba)

Caso essa tela tenha sido apresentada o programa
provavelmente está sendo executado corretamente

<h3> Criando um portifolio</h3>

Ao abrir o aplicativo não será exibida nenhuma ação
sendo necessario a criação de uma coleção de ações(portfólio)
clique no botão "Criar Portfólio" e será exibido a seguinte tela

![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/d4ac8550-170d-4774-bb29-7ecb8bd14674)


Em "Nome do portfolio" é o nome a se nomear o portfolio
esse será o nome do arquivo que será salvo e exibido em diversos gráficos

Em "Codigo da empresa" é o campo destinado a os codigos da empresa
esse codigo é o codigo que cada empresa de capital aberto possui para sua ação
após adicionar o codigo clique em "Adicionar" e a empresa será adicionada

ATENÇÃO:Adicione todas as empresas antes de inserir os valores.

Insira nos valores a quantidade de ações que possui
e marque as checkbox das ações que deseja incluir

Obsereve o exemplo:

![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/85e5c78f-65de-4690-90b4-8b72bab3168c)

Após isso clique em "Salvar alterações", o portfólio será salvo em arquivos
além disso todas suas ações escolhidas serão carregadas
observe:

![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/fd23195f-4c47-42a6-bd6f-fbeca6e08fb8)

<h3>carregando um novo portfólio</h3>
  
Para carregar um novo portfólio há duas maneiras
1) Clique em "Carregar Portfólio"
2)Clique em "Arquivo">"Abrir"

Em ambos caso será aberta uma tela de seleção de portfolio
efetue a seleção e clique no botão "Abrir"
observe a imagem abaixo

![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/0b2b3a77-16dd-4d66-9e3f-b2a246e05f6a)

Caso voce tenha carregado um portoflio com simulação será possivel ver a ultima simulação

<h3>Observando cada empresa</h3>

Após carregar ou criar seu portfolio é possivel visualizar um periodo de um ano

Todavia esse periodo encerra 5 dias antes do atual

(Esses 5 dias não sao propagados na simulação, a simulação ocorre com o ultimo dado disponivel)

O codigo escolhido receberá uma coloração azul, e o restante cinza

![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/cc134cd2-5e42-4c2c-9aee-8da174578890)

<h3>Efetuando uma simulação</h3>

Uma vez que o portfolio foi criado ou carregado corretamente

É possivel simular os riscos, para isso clique em "calcular risco"


Será aberta uma nova janela, selecione o periodo desejado



Dia analisa com espaçamento diario

Mes analisacom espaçamentos em meses

Ano analisa com espaçamento anual

Há 30 periodos por padrão e não configuravel

Observe:

![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/e267d2f4-0094-444a-97dd-340ee557fa7c)

Após isso clique em "Iniciar simulação"

O processo iniciará em um segundo thread/nucleo

E após finalizado exbirá o grafico com as informações na parte frontal


observe o exemplo:

![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/96decb51-3363-4920-ac10-de707948be60)


Observe que o nome do portfólio é exibido com titulo do grafico

<h3>Carregando a ultima simulação sem simular</h3>

Caso a simulação tenha sido concluida e você deseje observar novamente

Ou o portfolio carregado possua uma simulação armazenada 

Será possivel observa-la clicando em "Ultima simulação"

![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/5a050f4c-d92a-42d2-b5fa-79ea7563fb24)


<h3>Visualizando os creditos</h3>

Ao clicar em "Ajuda">"Creditos" será possivel observar os criadores do projeto


![image](https://github.com/emiliobrazil/portfolio_analysis/assets/128740531/002b1875-030d-4c9f-931c-62bc720b14f1)


<h2>Vantagens desse programa</h2>

1) Simulações rapidas e precisas: o aplicativo juntamente com o metodo de montecarlo permite simulações que duram poucos minutos e apresentam boa precisão

2) Avaliação de Riscos: Ajuda a entender os riscos. Imagine um superpoder que permite simular diferentes situações para ver quais são os riscos em cada uma delas.

3) Dados atualizados: coleta os dados atualizados em tempo real, garantindo maior fidelidade na simulação.

4) Facil e simples de usar: o programa possui uma interface rustica, sem complicações e modernismos, alem de prover toda sua usabilidade em poucos cliques, permitindo que qualquer usuario possa usa-lo sem complicações.

5) Leve e funciona em quase todos os computadores:Com requisistos minimos praticamente universais, o proograma pode ser executado sem problemas em quase todos os computadores atualmente.

