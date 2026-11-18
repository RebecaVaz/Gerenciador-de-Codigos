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

O sistema funciona a partir da comparação entre versões de um catálogo. O usuário seleciona o arquivo PDF e o arrasta para a aplicação, que realiza automaticamente a leitura e a extração dos códigos, em seguida os dados identificados são comparados com as informações da versão anteriormente armazenada no banco de dados SQLite, permitindo acompanhar as alterações entre os catálogos.

Para que essa comparação seja possível, é necessário armazenar os dados de cada atualização criando uma cópia de segurança do banco de dados anterior, preservando as informações da versão precedente, utilizando o botão de **Backup** logo abaixo na interface do programa!!

Com esse processo, a aplicação oferece as seguintes funcionalidades:

- **Extração automatizada:** leitura de arquivos PDF e identificação de códigos por meio de expressões regulares (Regex).
- **Detecção de duplicidades:** identificação de códigos repetidos no catálogo e contabilização de suas ocorrências.
- **Controle de numeração:** gerenciamento de códigos no intervalo de 001 a 999, com identificação do maior código utilizado e sugestão automática de uma numeração disponível.
- **Identificação de códigos disponíveis:** geração de uma lista de códigos que não estão sendo utilizados no catálogo atual, indicando possibilidades de reutilização.
- **Comparação entre versões:** análise dos códigos da atualização atual em relação aos dados anteriormente armazenados, identificando quais códigos deixaram de constar no catálogo.
- **Armazenamento estruturado:** utilização do SQLite para persistência dos dados e consulta às informações de atualizações anteriores.
- **Backup local:** criação de uma cópia de segurança do banco de dados anterior antes da atualização dos registros.
- **Interface gráfica interativa:** utilização simplificada por meio de uma interface desenvolvida com Tkinter, com suporte a arrastar e soltar arquivos PDF.

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

## ⚙️ Features

The system operates by comparing different versions of a catalog. The user selects a PDF file and drags it into the application, which automatically processes the document and extracts the product codes. The extracted data is then compared against the information from the previous version stored in the SQLite database, making it possible to track changes between catalog versions.

To make this comparison possible, the data from each update must be stored by creating a backup of the previous database, thereby preserving the information from the preceding version. This can be done using the **Backup** button located directly below in the application interface!!

Through this process, the application provides the following features:

- **Automated Data Extraction:** reads PDF files and identifies codes using Regular Expressions (Regex).
- **Duplicate Detection:** identifies repeated codes within the catalog and counts their occurrences.
- **Code Sequence Management:** manages codes within the range of 001 to 999, identifies the highest code currently in use, and automatically suggests an available code.
- **Available Code Identification:** generates a list of codes that are not currently being used in the catalog, highlighting potential opportunities for reuse.
- **Version Comparison:** compares codes from the current update against previously stored data, identifying which codes are no longer present in the catalog.
- **Structured Data Storage:** uses SQLite for data persistence and retrieval of information from previous updates.
- **Local Backup:** creates a backup copy of the previous database before updating its records.
- **Interactive Graphical Interface:** provides a simplified user experience through an interface developed with Tkinter, featuring drag-and-drop support for PDF files.

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
