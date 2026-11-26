# HealthBridge

## Sobre o projeto

O HealthBridge é um protótipo acadêmico de compartilhamento de dados essenciais de saúde entre instituições e profissionais, mediante consentimento do paciente. Ele reúne os dados essenciais em um perfil único e registra o consentimento de compartilhamento, os alertas e a auditoria das ações.

> Todos os dados são fictícios. O projeto não deve ser usado com dados reais nem em atendimento clínico.

## Funcionalidades

- **Perfil único do paciente:** dados essenciais (idade, tipo sanguíneo, sexo, alergias, condições e medicamentos) e histórico de registros.
- **Cadastro e registros clínicos:** cadastro de pacientes e de registros (consulta, exame, internação), com validação das entradas.
- **Consentimento de compartilhamento:** concessão e revogação por paciente, com data registrada.
- **Alertas:** consentimento revogado e acompanhamento recomendado.
- **Auditoria:** registro de cadastros, novos registros e mudanças de consentimento.
- **Dashboard e busca:** indicadores, pacientes recentes e busca por nome ou identificador.

## Arquitetura

| Arquivo | Camada | Responsabilidade |
|---|---|---|
| `frontend.html` | Interface | Telas, navegação, formulários e consumo da API (HTML, CSS e JavaScript) |
| `backend.py` | API REST | Endpoints, validação de entradas e regras de alertas e auditoria (FastAPI e Pydantic) |
| `database.py` | Banco de dados | Conexão SQLite, modelos ORM (SQLAlchemy) e dados fictícios de demonstração |
| `README.md` | Documentação | Descrição e instruções |

**Modelo de dados:** `patients` (dados essenciais e consentimento), `records` (histórico clínico, ligado ao paciente) e `audit` (eventos). Os dados de demonstração são criados na primeira execução.

## Tecnologias

- HTML5, CSS3 e JavaScript puro (Fetch API)
- Python 3.10+
- FastAPI, Uvicorn e Pydantic
- SQLAlchemy e SQLite


## Limitações

Protótipo acadêmico, não pronto para produção:

- autenticação simulada e sem permissões clínicas;
- consentimento registrado e auditado, mas ainda sem bloquear o acesso aos dados na API;
- sem criptografia ponta a ponta e sem integração institucional (como o PEC e-SUS);
- indicadores do dashboard demonstrativos.


## Contexto acadêmico

Projeto desenvolvido em grupo no Projeto Integrador II (ADS, 2026/2), a partir do case de otimização do acesso a dados de pacientes por instituições e profissionais de saúde.
