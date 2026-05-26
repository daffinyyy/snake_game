# Snake Game

Jogo da cobrinha feito em Python com Pygame, com multiplayer local para 2 jogadores, pontuação separada, dificuldade selecionável e tela em grade.

## Requisitos

- Python 3.10 ou superior
- `pip`
- Sistema operacional: Linux ou Windows

## Instalação no Linux

1. Abra o terminal na pasta do projeto.
2. Crie o ambiente virtual:

	```bash
	python3 -m venv .venv
	```

3. Ative o ambiente virtual:

	```bash
	source .venv/bin/activate
	```

4. Instale as dependências:

	```bash
	pip install -r requirements.txt
	```

5. Execute o jogo:

	```bash
	cd src
	python main.py
	```

## Instalação no Windows

1. Abra o PowerShell ou Prompt de Comando na pasta do projeto.
2. Crie o ambiente virtual:

	```powershell
	py -m venv .venv
	```

3. Ative o ambiente virtual:

	```powershell
	.venv\Scripts\activate
	```

4. Instale as dependências:

	```powershell
	pip install -r requirements.txt
	```

5. Execute o jogo:

	```powershell
	cd src
	python main.py
	```

## Como jogar

- Jogador 1: setas do teclado
- Jogador 2: teclas WASD
- `Enter`: inicia a partida no menu
- `1`, `2`, `3`: selecionam dificuldade no menu
- `R`: reinicia após game over
- `ESC`: sai da tela de fim de jogo

## Dificuldades

- Fácil: menos comidas na tela
- Normal: quantidade padrão de comidas
- Difícil: mais comidas na tela

## Observações

- O jogo deve ser executado a partir da pasta `src`, porque os imports são relativos aos arquivos dessa pasta.
- A dependência externa principal está em `requirements.txt`.

## Estrutura do projeto

```text
snake_game/
├── README.md
├── requirements.txt
└── src/
	 ├── config.py
	 ├── game.py
	 ├── main.py
	 ├── sprites.py
	 ├── systems.py
	 └── utils.py
```