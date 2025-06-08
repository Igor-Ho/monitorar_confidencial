# Monitoramento de Documento Crítico

Este projeto tem como objetivo monitorar alterações em um arquivo crítico do sistema e registrar qualquer modificação detectada em um log. Essa funcionalidade pode ser útil em contextos de segurança da informação, onde é importante auditar acessos e edições de arquivos sensíveis.

## Funcionalidades

- Verifica se o arquivo crítico existe
- Monitora continuamente alterações (modificação de timestamp)
- Registra eventos com data e hora em um arquivo de log (`security_log.txt`)

## Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/devops.git
   cd monitoramento-documento
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
[2025-06-08 14:13:45] Arquivo 'documento_critico.txt' foi modificado.
[2025-06-08 14:20:00] Monitoramento interrompido pelo usuário.
```

## Requisitos
- Python 3.x

## Melhorias Futuras
- Monitoramento de múltiplos arquivos ou diretórios
- Envio de alertas por e-mail ou mensageria
- Uso de bibliotecas como `watchdog` para eficiência

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
