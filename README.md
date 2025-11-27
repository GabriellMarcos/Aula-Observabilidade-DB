📘 Observabilidade com Banco de Dados, Exporters e Carga Real

Este projeto implementa um ambiente completo de observabilidade, incluindo banco de dados relacional, coleta de métricas, dashboards e camada de segurança, tudo orquestrado via Docker Compose.

A arquitetura final integra:

👉 Coleta → Exposição → Armazenamento → Visualização → Análise → Apresentação

🧩 Arquitetura do Projeto

O ambiente é composto pelos seguintes serviços:

Serviço	Função
PostgreSQL	Banco de dados relacional principal
Postgres Exporter	Exporta métricas do PostgreSQL para Prometheus
Node Exporter	Exporta métricas do sistema host
Prometheus	Armazena e consulta métricas dos exporters
Grafana	Dashboards e visualização
Load Generator	Gera carga real no banco
Nginx (HTTPS + Basic Auth)	Reverse proxy seguro para o Grafana

Toda a comunicação interna ocorre em uma única rede Docker, garantindo isolamento e segurança.

🎯 1. Banco de Dados Relacional (PostgreSQL)

O grupo escolheu o PostgreSQL devido à estabilidade, documentação extensa e grande compatibilidade com exporters.

Configurações principais:

Persistência via volume pgdata

Banco padrão: observabilidade

Usuário e senha: admin / admin123

Script de inicialização suportado via ./db

🎯 2. Database Exporter (Postgres Exporter)

Para expor métricas do banco no padrão Prometheus, utilizamos o postgres-exporter, que coleta informações como:

Conexões ativas

Locks e deadlocks

Tamanho de tabelas

Queries por segundo

Buffers, cache e I/O

O serviço expõe métricas na porta 9187, acessível internamente.

🎯 3. Load Generator (Gerador de Carga)

Foi criado um container separado responsável por:

Inserir, ler, atualizar e deletar registros no banco

Executar operações contínuas e aleatórias

Gerar atividade real para que os dashboards mostrem informações dinâmicas

Isso garante que o Prometheus e o Grafana sempre tenham dados relevantes sendo atualizados.

🎯 4. Prometheus — Coleta e Armazenamento

O Prometheus foi configurado para coletar:

node-exporter (métricas do host)

postgres-exporter (métricas do banco)

Próprias métricas internas (self-metrics)

Configurações essenciais foram feitas no arquivo:

./prometheus/prometheus.yml

🎯 5. Grafana — Visualização e Dashboards

O Grafana roda na porta interna 3000, porém somente exposto ao usuário final via porta 443 no Nginx.

Dashboards criados:

Métricas gerais do PostgreSQL

Conexões ativas (em tempo real)

Throughput de queries

Locks e conflitos

Tamanho de tabelas e índices

Utilização de CPU / RAM via Node Exporter

Latência de operações do banco

Datasource foi provisionado automaticamente apontando para o Prometheus.

🔐 6. Camada Extra de Segurança (Nginx + HTTPS + Basic Auth)

O ambiente exige que somente duas portas fiquem acessíveis externamente:

Porta	Função
22	SSH da EC2
443	Grafana via Nginx com autenticação

Recursos configurados:

✔ HTTPS usando certificado .pem
✔ Reverse Proxy
✔ Proteção com htpasswd

Fluxo final:

Usuário → HTTPS :443 → Nginx → Grafana (3000)


O Grafana não fica exposto diretamente, aumentando a segurança.

🧰 7. Docker Compose Completo

A stack é toda provisionada via:

docker-compose up -d


Incluindo:

Banco

Exporters

Prometheus

Grafana

Load Generator

Nginx

A arquitetura final segue exatamente o checklist solicitado pelo professor.

🧪 8. Testes Realizados

✔ Acesso ao Grafana via HTTPS
✔ Login com usuário e senha configurados
✔ Carga sendo gerada continuamente
✔ Métricas chegando no Prometheus
✔ Dashboards atualizando em tempo real
✔ Banco recebendo operações de I/O corretamente
✔ Exporters funcionando sem erros

📊 9. Dashboards Criados

Os dashboards mostram:

🟦 Métricas do Banco

Queries por segundo (QPS)

Slow queries

Locks / deadlocks

Tamanho das tabelas

Conexões ativas por aplicação

Cache Hit Ratio

Buffers / I/O

🟩 Métricas do Host

CPU total

Load average

Memória usada / disponível

Disco

I/O do container

🧱 10. Diagrama da Arquitetura
             ┌───────────────────────┐
             │       Usuário         │
             └───────────┬───────────┘
                         │ https:443
                         ▼
                 ┌──────────────┐
                 │    Nginx     │
                 └──────┬───────┘
                        │ proxy
                        ▼
                ┌───────────────┐
                │    Grafana    │
                └───────────────┘
                        │
                        ▼
             ┌────────────────────────┐
             │      Prometheus        │
             └───────────┬────────────┘
                         │ scrapes
       ┌─────────────────┼──────────────────┐
       ▼                 ▼                  ▼
Node Exporter   Postgres Exporter   Load Generator
                       │
                       ▼
                  PostgreSQL

✔ Checklist Final Entregue
Requisito	Status
Docker Compose funcionando	✔
Banco configurado	✔
Exporter configurado	✔
Load generator	✔
Prometheus coletando métricas	✔
Dashboards no Grafana	✔
Segurança com Nginx + HTTPS + Auth	✔
Apenas portas 22 e 443 abertas	✔
📄 11. Como Rodar
1. Clone o repositório
git clone <seu repo>
cd Aula-Observabilidade-DB

2. Inicie a stack
docker-compose up -d

3. Acesse o Grafana:
https://<IP-DA-EC2>


Login:

user: admin

pass: admin

senha básica configurada no Nginx

📚 Conclusão

Este projeto demonstra de forma completa:

Monitoramento

Coleta de métricas

Observabilidade real

Segurança de acesso

Carga simulada

Análise gráfica

É um ambiente pronto e escalável, que reflete uma arquitetura moderna usada em empresas reais.
