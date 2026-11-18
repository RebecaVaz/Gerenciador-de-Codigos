# 📄 Analisador e Gerenciador de Catálogos PDF
### PDF Catalog Analyzer & Management System

<p align="center">
  **🇧🇷 Português | 🇺🇸 English**
</p>

---

# 🇧🇷 Português

## 📌 Sobre o projeto

Aplicação desenvolvida em Python para automatizar a análise de catálogos de produtos em PDF, com foco na identificação de códigos duplicados, controle de numeração e identificação de códigos disponíveis para reutilização.

O projeto surgiu de uma necessidade real no ambiente profissional, naqual os catálogos passam por atualizações frequentes, envolvendo a inclusão e remoção de produtos. Como a numeração não segue uma sequência contínua e alguns códigos podem ser reutilizados, o controle manual aumentava o risco de inconsistências e duplicidades.

Para solucionar esse problema, desenvolvi uma aplicação capaz de automatizar a extração, organização e análise dessas informações, tornando o processo mais eficiente e confiável.

## 🎯 Objetivos

- Automatizar a identificação e análise dos códigos presentes nos catálogos.
- Detectar duplicidades e inconsistências na numeração.
- Identificar códigos disponíveis para reutilização.
- Comparar os códigos do catálogo atual com os registros anteriormente armazenados.
- Preservar as informações por meio de armazenamento estruturado e backups locais.

## ⚙️ Funcionalidades

- **Extração automatizada:** leitura de arquivos PDF e identificação de códigos por meio de expressões regulares (Regex).
- **Detecção de duplicidades:** identificação de códigos repetidos e contabilização de suas ocorrências.
- **Controle de numeração:** gerenciamento de códigos de 001 a 999, com retorno automático ao início da sequência.
- **Identificação de códigos disponíveis:** geração automática de uma lista de códigos que não estão sendo utilizados no catálogo atual.
- **Comparação de versões:** identificação de códigos que deixaram de constar no catálogo em relação à versão anteriormente armazenada, permitindo identificar novas possibilidades de reutilização.
- **Armazenamento estruturado:** utilização do SQLite para persistência das informações processadas.
- **Backup local automático:** preservação de uma cópia da versão anterior do banco de dados antes da atualização.
- **Interface gráfica:** interação simplificada com suporte a arrastar e soltar arquivos PDF.

## 🖥️ Demonstração da aplicação

### Tela inicial

Interface gráfica desenvolvida com Tkinter, projetada para facilitar a utilização e o processamento dos catálogos.

![Tela inicial do programa](imagens/tela-inicial.png)

### Implementação e código-fonte

Desenvolvimento da lógica de extração, processamento, identificação de duplicidades e gerenciamento das informações utilizando Python.

![Código-fonte do projeto](imagens/codigo-fonte.png)

### Gerenciamento e backup

Funcionalidade responsável por salvar os dados processados e preservar uma cópia da versão anterior do banco de dados SQLite.

![Funcionalidade de backup](imagens/backup.png)

### Identidade visual

Logo utilizada na interface da aplicação.

![Logo do projeto](imagens/logo.png)

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal e lógica da aplicação |
| Tkinter | Desenvolvimento da interface gráfica |
| TkinterDnD2 | Implementação do recurso de arrastar e soltar |
| PDFPlumber | Extração de texto de arquivos PDF |
| Regex (re) | Identificação de padrões e códigos numéricos |
| SQLite | Armazenamento e gerenciamento dos dados |
| Counter | Contabilização de ocorrências duplicadas |
| OS e Shutil | Manipulação de arquivos e realização de backups |

## 🚀 Instalação e execução

**1. Clone o repositório:**

```bash
git clone URL_DO_REPOSITORIO
```

**2. Acesse o diretório do projeto:**

```bash
cd Sistema-Analise-Catalogos-PDF
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Execute a aplicação:**

```bash
python Sistema.py
```

**Pré-requisitos:** Python instalado e ambiente com suporte ao Tkinter.

## 📊 Resultados alcançados

A implementação da ferramenta possibilitou identificar diversas duplicidades que anteriormente passavam despercebidas durante o processo manual de conferência.

Com a automatização, o catálogo passou a contar com maior consistência na numeração, reduzindo erros operacionais, evitando confusões durante as vendas e agilizando a identificação dos produtos.

## 💡 Aprendizados e desenvolvimento

Este projeto proporcionou experiência prática no desenvolvimento de aplicações Python, manipulação de arquivos PDF, processamento de dados, expressões regulares, persistência em bancos de dados relacionais e automação de processos.

Também reforçou a importância de compreender problemas reais e transformar necessidades operacionais em soluções tecnológicas eficientes.

---

# 🇺🇸 English

## 📌 Project Overview

A Python-based desktop application designed to automate the analysis and management of product catalogs in PDF format, focusing on duplicate code detection, numbering control, and the identification of codes available for reuse.

The project originated from a real-world operational challenge: product catalogs undergo frequent updates involving the addition and removal of items. Since identifiers are non-sequential and may be reused, manual tracking increased the risk of inconsistencies and duplicate assignments.

To address this challenge, I developed an application capable of automating data extraction, organization, and analysis, improving operational efficiency and data consistency.

## 🎯 Project Objectives

- Automate the identification and analysis of catalog identifiers.
- Detect duplicate entries and numbering inconsistencies.
- Identify codes available for reuse.
- Compare the current catalog against previously stored records.
- Preserve processed information through structured data storage and local backups.

## ⚙️ Key Features

- **Automated data extraction:** PDF text processing and code identification using regular expressions (Regex).
- **Duplicate detection:** identification of repeated codes and frequency counting.
- **Numbering control:** management of identifiers ranging from 001 to 999, with automatic sequence rollover.
- **Available code identification:** automatic generation of a list of identifiers not currently in use within the catalog.
- **Version comparison:** detection of identifiers that are no longer present compared with the previously stored catalog, making newly available codes identifiable for potential reuse.
- **Structured data persistence:** SQLite integration for storing processed information.
- **Automatic local backup:** preservation of the previous database version before updating stored records.
- **Graphical user interface:** streamlined interaction with drag-and-drop PDF support.

## 🖥️ Application Showcase

### Main Interface

A graphical interface developed with Tkinter, designed to simplify catalog processing and user interaction.

![Application main interface](imagens/tela-inicial.png)

### Source Code and Implementation

Python implementation covering data extraction, processing, duplicate detection, and identifier management.

![Project source code](imagens/codigo-fonte.png)

### Data Management and Backup

A backup mechanism designed to preserve the previous SQLite database version before updating stored information.

![Backup functionality](imagens/backup.png)

### Application Branding

Logo incorporated into the application's graphical interface.

![Application logo](imagens/logo.png)

## 🛠️ Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Core programming language and application logic |
| Tkinter | Graphical user interface development |
| TkinterDnD2 | Drag-and-drop functionality |
| PDFPlumber | PDF text extraction |
| Regular Expressions | Pattern recognition and code identification |
| SQLite | Structured data storage and management |
| Counter | Duplicate occurrence analysis |
| OS and Shutil | File system operations and backup management |

## 🚀 Installation and Execution

**1. Clone the repository:**

```bash
git clone REPOSITORY_URL
```

**2. Navigate to the project directory:**

```bash
cd Sistema-Analise-Catalogos-PDF
```

**3. Install the required dependencies:**

```bash
pip install -r requirements.txt
```

**4. Run the application:**

```bash
python Sistema.py
```

**Prerequisites:** Python installation and an environment with Tkinter support.

## 📊 Project Outcomes

The implementation enabled the identification of multiple duplicated codes that had previously gone unnoticed during manual verification.

By automating the process, the application improved catalog numbering consistency, reduced operational errors, minimized potential sales-related confusion, and streamlined product identification.

## 💡 Technical Experience and Learning Outcomes

This project provided hands-on experience in Python application development, PDF processing, data manipulation, regular expressions, relational database management, and process automation.

It also reinforced the importance of translating real-world business requirements into practical, reliable, and efficient software solutions.

---

## 📄 License

This project is distributed under the MIT License.
