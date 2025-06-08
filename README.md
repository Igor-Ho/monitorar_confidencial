# Monitoramento de Documento Confidencial

Este projeto tem como objetivo monitorar alterações em um arquivo confidencial do sistema e registrar qualquer modificação detectada em um log usando script python.

## Funcionalidades

- Verifica se o arquivo crítico existe
- Monitora continuamente alterações (modificação de timestamp)
- Registra eventos com data e hora em um arquivo de log (`security_log.txt`)

## Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/monitorar_confidencial.git
   cd monitorar_confidencial
   ```

2. **Crie o arquivo crítico (caso ainda não exista):**
   ```bash
   echo "Conteúdo inicial" > confidencial.txt
   ```

3. **Execute o monitoramento:**
   ```bash
   python monitor.py
   ```

4. **Interrompa com `CTRL+C` quando desejar.**

## Exemplo de Log
```txt
[2025-06-08 14:12:01] Monitoramento iniciado.
[2025-06-08 14:13:45] Arquivo 'confidencial.txt' foi modificado.
[2025-06-08 14:20:00] Monitoramento interrompido pelo usuário.
```

## Requisitos
- Python 3.x

## Melhorias Futuras
- Monitoramento de múltiplos arquivos ou diretórios
- Envio de alertas por e-mail ou mensageria
- Uso de bibliotecas como `watchdog` para eficiência
