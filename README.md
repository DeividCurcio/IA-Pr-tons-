# IA-Prótons - Robocop Policial

Sistema de Inteligência Artificial para Segurança e Proteção

## 🤖 Sobre o Projeto

O **Robocop Policial** é um sistema de IA desenvolvido para monitoramento de segurança, detecção de ameaças e patrulhamento automático. O sistema utiliza algoritmos de análise para identificar diferentes níveis de ameaça e tomar ações apropriadas.

## 🚀 Funcionalidades

- **Patrulhamento Automático**: Sistema de patrulha inteligente em áreas designadas
- **Detecção de Ameaças**: Análise contínua do ambiente com 4 níveis de ameaça
- **Registro de Incidentes**: Documentação automática de situações suspeitas
- **Relatórios**: Geração de relatórios detalhados sobre atividades e incidentes
- **Sistema de Alertas**: Notificações baseadas no nível de ameaça detectado

## 📋 Níveis de Ameaça

1. **BAIXO** - Área segura, patrulha normal
2. **MÉDIO** - Atividade suspeita, aumentar vigilância
3. **ALTO** - Possível ameaça, solicitar reforços
4. **CRÍTICO** - Ameaça iminente, intervenção imediata

## 🛠️ Instalação

```bash
# Clone o repositório
git clone https://github.com/DeividCurcio/IA-Pr-tons-.git
cd IA-Pr-tons-

# Instalar dependências (se necessário)
pip install -r requirements.txt
```

## 💻 Uso

### Execução Básica

```bash
python robocop_policial.py
```

### Uso Programático

```python
from robocop_policial import RobocopPolicial

# Criar instância do Robocop
robocop = RobocopPolicial(nome="ROBOCOP-001", area_patrulha="Centro")

# Ativar sistema
robocop.ativar()

# Executar patrulha
robocop.executar_patrulha()

# Gerar relatório
robocop.relatorio_incidentes()

# Desativar sistema
robocop.desativar()
```

## 📁 Estrutura do Projeto

```
IA-Pr-tons-/
├── robocop_policial.py  # Sistema principal
├── config.py            # Configurações
├── requirements.txt     # Dependências
└── README.md           # Documentação
```

## ⚙️ Configuração

Edite o arquivo `config.py` para personalizar:
- ID e versão do sistema
- Área de patrulha padrão
- Sensibilidade de detecção
- Parâmetros de alerta
- Ações automáticas

## 🔒 Segurança

Este é um sistema de demonstração. Para uso em produção, considere:
- Integração com câmeras e sensores reais
- Sistema de autenticação robusto
- Criptografia de dados
- Backup e redundância
- Conformidade com regulamentações locais

## 📝 Licença

Este projeto é parte do Tabernáculo da Luz.

## 👨‍💻 Autor

Desenvolvido por DeividCurcio
