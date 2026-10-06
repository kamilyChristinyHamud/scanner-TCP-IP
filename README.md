# Port Scanner Simples em Python

Script em Python que desenvolvi para estudar redes e entender como funciona a varredura básica de portas TCP utilizando a biblioteca padrão `socket`.

## Aviso!
Ferramentas de varredura de portas devem ser utilizadas exclusivamente em ambientes controlados e com autorização explícita (como em laboratórios locais no IP `127.0.0.1`). Escanear redes, servidores ou sistemas de terceiros sem permissão viola políticas de segurança e pode ser interpretado como atividade maliciosa.

## Como Funciona
O script resolve o endereço IP do alvo e percorre uma lista de portas TCP comuns. Utilizando a função `connect_ex`, ele verifica quais portas respondem a conexões, identificando serviços ativos na máquina alvo de forma rápida.

## Como Usar

1. Ter o Python instalado no teu sistema.
2. Salvar o script como `scanner.py`.
3. Abrir o terminal na pasta do projeto e executar:
   ```bash
   python3 scanner.py
   
