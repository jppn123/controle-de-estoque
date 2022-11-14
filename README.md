# gerenciamento-de-estoque
Você deve criar o algoritmo de uma plaicação para gerenciamento do estoque de uma loja de jogos

Cada jogo possui um título (string), um ano de lançamento (inteiro), uma plataforma (Nintendo Switch, Playstation 5, XBOX Series X e S, PC) (string), um gênero (string), um preço (float) e a quantidade de unidades do jogo no estoque (inteiro).

O estoque deve ser armazenado em um arquivo e pode ser manipulado como uma lista. Cada jogo deve ser representado obrigratoriamento por uma estrutura de Dicionário (Registro).

A aplicação deve ter um menu similar ao abaixo com as mesma opções:

Digite o número correspondente a opção desejada:
- 1 - Ver lista de jogos
- 2 - Buscar um jogo
- 3 - Salvar um novo jogo
- 4 - Retirar um jogo
- 0 - Fechar o sistema

Esse menu deve aparecer ao iniciar o programa e após alguma das opções 1 a 4 do menu serem executadas. O programa só deve finalizar se for escolhida a opção 0 do menu.

- Ao ser escolhida a opção 1, a lista de jogos no arquivo com o estoque de jogos deve ser lida e mostrada na tela os títulos dos jogos no estoque
- Ao ser escolhida a opção 2, deve ser solicitado o título do jogo que o usuário quer buscar, então deve ser feita a busca do jogo no estoque (vocês podem ler a lista de jogos do estoque, guardar em uma estrutura de lista e depois buscar o jogo nessa lista) e deve ser mostrada todas as informações desse jogo.
- Ao ser escolhida a opção 3, deve ser pedido para o usuário indicar as informações do jogo que quer salvar no estoque (título, ano de lançamento, plataforma, gênero, preço e quantidade de unidades do jogo) e então o jogo deve ser salvo no estoque, ou seja, deve ser adicionado no arquivo que contém o estoque
- Ao ser escolhida a opção 4, deve ser solicitado o título do jogo que o usuário quer remover e então uma unidade do jogo deve ser removida do estoque, ou seja, deve ser decrementada a quantidade de unidades do jogo no estoque e caso a quantidade chegue a zero, o jogo deve ser removido do estoque, lembre-se de depois guardar o estoque atualizado no arquivo

O estoque inicial deve conter ao menos 10 jogos diferentes (vocês devem inciar o programa então com o arquivo de estoque já com esses 10 jogos escritos nele)
