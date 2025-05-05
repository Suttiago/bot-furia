# Bot FURIA

Um bot do Telegram focado no time de CS:GO da FURIA. Ele fornece notícias, lineup atual, próximos jogos, e um minigame para fãs interagirem.

## Funcionalidades

- `/start`: Mensagem de boas-vindas.
- `/help`: Lista os comandos disponíveis.
- `/lineup`: Mostra o lineup atual.
- Notícias sobre a FURIA.
- Minigame interativo para fãs.
- Análise de sentimentos (em desenvolvimento).

## Tecnologias

- Python 3.x  
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)  
- requests  
- beautifulsoup4  
- python-dotenv

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Suttiago/bot-furia.git
   cd bot-furia
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Adicione seu token ao arquivo `.env` ou `config.py` (dependendo de como está implementado).

## Execução

```bash
python bot.py
```

## Estrutura do Projeto

```
/commands        # Comandos do bot (ex: /start.py, /help.py)
bot.py           # Inicialização principal do bot
config.py        # Configurações e token do bot
```

## Contribuindo

Contribuições são bem-vindas! Para colaborar:

1. Faça um fork do repositório.
2. Crie uma branch com sua funcionalidade:
   ```bash
   git checkout -b minha-funcionalidade
   ```
3. Faça um commit com suas mudanças.
4. Envie um pull request.

---

💬 Dúvidas, sugestões ou bugs? Sinta-se à vontade para abrir uma issue!