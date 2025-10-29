# 🧩 Desafio de Refatoração de Código — Engenharia de Software II

## 📘 Contexto Acadêmico

Este repositório foi desenvolvido como parte da disciplina **DEC7130 – Engenharia de Software II**, do curso de **Tecnologias da Informação e Comunicação (TIC)** da **Universidade Federal de Santa Catarina – Campus Araranguá**.  

O trabalho teve como objetivo **identificar, analisar e corrigir diferentes tipos de *code smells*** (maus odores de código), aplicando técnicas de **refatoração** para melhorar a clareza, modularidade e manutenção do código, conforme os princípios da **programação orientada a objetos** e das boas práticas de **engenharia de software**.

Todos os exemplos foram implementados em **Python**, dentro do contexto temático do **futebol**, com foco em situações que envolvem o **Criciúma Esporte Clube**, buscando tornar os exemplos didáticos.

---

## ⚙️ Objetivos

- Identificar *code smells* em exemplos de código simples e funcionais.  
- Aplicar as técnicas de refatoração adequadas para cada categoria.  
- Demonstrar, na prática, como a refatoração melhora a qualidade do código.  
- Produzir documentação e exemplos que possam servir como material de estudo.  

---

## 🧠 Categorias de Code Smells

A seguir estão descritas as cinco categorias abordadas neste trabalho, conforme a classificação proposta por **Refactoring Guru (2025)**.

### 🧱 1. Bloaters

Os *Bloaters* surgem quando o código cresce em tamanho e complexidade, tornando-se difícil de compreender e manter.  
No exemplo, foi identificado o *Long Method*, onde uma única função acumulava diversas responsabilidades (entrada, processamento e exibição de dados).  
A refatoração aplicada foi **Extract Method**, que dividiu o método em partes menores e mais legíveis.  


---

### 🧩 2. Object-Orientation Abusers

Essa categoria representa o mau uso dos princípios da orientação a objetos.  
O exemplo escolhido foi o *Switch Statements*, em que uma estrutura condicional controlava o comportamento de jogadores de diferentes posições.  
Foi aplicada a refatoração **Replace Conditional with Polymorphism**, criando subclasses específicas para cada tipo de jogador.


---

### 🔄 3. Change Preventers

Os *Change Preventers* indicam estruturas que dificultam a modificação e evolução do sistema.  
No caso estudado, observou-se o *Divergent Change*, em que uma mesma classe possuía múltiplas responsabilidades (gols, cartões e público).  
A refatoração **Extract Class** foi utilizada para separar as responsabilidades em classes distintas.


---

### 🗑️ 4. Dispensables

Os *Dispensables* englobam elementos desnecessários no código, como duplicações, classes ociosas ou código morto (*Dead Code*).  
O exemplo utilizou um sistema de gerenciamento de treinos do Criciúma, no qual métodos não utilizados foram mantidos sem propósito.  
Aplicou-se a refatoração **Remove Dead Code**, eliminando funções redundantes e simplificando a classe.


---

### 🤝 5. Couplers

Os *Couplers* surgem quando há acoplamento excessivo entre classes, resultando em dependências fortes e baixa modularidade.  
O exemplo de *Feature Envy* mostrou uma classe `Transferencia` que manipulava diretamente os atributos de `Jogador`.  
A refatoração **Move Method** transferiu a responsabilidade para a classe correta, reduzindo o acoplamento e aumentando a coesão.


---

## 🧰 Técnicas de Refatoração Utilizadas

- **Extract Method** → divisão de métodos longos em partes menores.  
- **Replace Conditional with Polymorphism** → substituição de condicionais por hierarquia de classes.  
- **Extract Class** → extração de responsabilidades para novas classes.  
- **Remove Dead Code** → eliminação de trechos não utilizados.  
- **Move Method** → realocação de métodos para a classe mais apropriada.  

