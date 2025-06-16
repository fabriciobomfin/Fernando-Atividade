# 🚚 TransportGuard - Sistema de Gerenciamento de Transportadora

**Equipe:** Fabrício Bomfim, Marcus Vinnicius, Claudio Henrique, Bruno Santos  
**Turma:** Desenvolvimento de Sistemas - Senai Dendezeiras  
**Semestre:** 2025.1  

---

## 📋 Descrição do Projeto

**TransGuard** é um sistema completo de gerenciamento para uma transportadora, desenvolvido como projeto final da disciplina de **Internet das Coisas (IoT)**.  
O sistema realiza o controle das principais operações da empresa, como:

- Manutenção da frota
- Cadastro de clientes e fornecedores
- Registros de movimentação de caminhões
- Monitoramento de sensores em galpões
- Atuação remota em dispositivos via **Arduino**

---

## ⚙️ Funcionalidades Principais

### 📦 CRUDs

- **Peças**
- **Fornecedores**
- **Caminhões**
- **Funcionários**
- **Clientes**

### 📝 Registro de Saída de Caminhões

Campos registrados:
- Cliente
- Tipo de carga
- Destino
- Horário de entrada e saída
- Quilometragem inicial e final

### 🧠 Simulação de Sensores

- Sensor de **presença** (ultrassônico, se necessário)
- Sensor de **temperatura**
- Sensor de **luminosidade**

### 🚨 Ações Automáticas com Base nos Sensores

- Ativação de **alarme** em caso de presença suspeita
- Ativação de **sirene** por alta temperatura
- **Apagar luzes** automaticamente se o ambiente estiver claro

### 💡 Controle Manual de Iluminação (via interface)

Setores controlados:
- Oficina  
- Galpão (3 blocos)  
- Escritório  
- Corredor  
- Área de serviço  
- Área externa  

---

## 🧰 Tecnologias Utilizadas

- **Python 3**
- **Tkinter** (interface gráfica)
- **Arduino Uno/Mega** (simulado no Tinkercad)
- **Sensores:** presença (ou distância), temperatura, luminosidade, gás
- **Armazenamento:** arquivos `.txt` (simulando tabelas)
- **Comunicação Serial** (Python ↔ Arduino)

---

## 📡 Comunicação Serial Python ↔ Arduino

### 🔍 Sensores

- O Arduino simula sensores e envia os dados via Monitor Serial.
- O Python **lê os dados simulados** e exibe na interface gráfica.

### 💡 Controle de Luzes

- O Python **envia caracteres via serial** para acender ou apagar luzes.
- Exemplo de mapeamento:


---

## 📐 Modelagem e Diagramação

- **Casos de Uso:**  
  [Diagrama no Lucidchart](https://lucid.app/lucidchart/1914538b-1123-4e9b-bc26-f11e20b9c855/edit?viewport_loc=176%2C-236%2C3328%2C1780%2CsDms4zyG4P~t&invitationId=inv_fd4e685c-5b98-42db-9785-3633dbccd74f)

- **Diagrama de Classes:**  
  Representando os módulos principais (ilustrativo, simplificado)

---

## 🧪 Simulações no Tinkercad

### 🔧 Sensores

**Nome do Projeto:** `AVALIAÇÃO FINAL IOT (PROJETO SENSORES)`  
[Simulação - Sensor de Distância (Ultrassônico)](https://www.tinkercad.com/things/95vdITbEQFX-fernando-moreira-sensor-distancia?sharecode=yMGtEjZ1vxqIZ-p3Rmo0qI7lg7hlCRnBpwafPM4R-7Q)

### 💡 Controle de Luzes

**Nome do Projeto:** `AVALIAÇÃO FINAL IOT (PROJETO LÂMPADAS)`  
[Simulação - Controle Serial com Python](https://www.tinkercad.com/things/diOGfZNg5bt-comunicacao-serial-fernando?sharecode=m74cmOU-bVf3Ky7-_ZetpQrNyFXnoYgcTmHhoIITHoM)

---

## 📘 Documentação de Falhas (caso necessário)

Caso algum requisito não seja implementado, será entregue um arquivo `.txt` contendo:

- Requisito não cumprido  
- Tentativas realizadas  
- Dificuldades enfrentadas  
- Possível solução (e por que não foi implementada)

---

## ✅ Conclusão

O projeto **TransGuard** visa entregar uma solução robusta, intuitiva e funcional para a gestão de uma transportadora, aliando:

- Controle operacional e logístico
- Monitoramento inteligente de ambientes
- Atuação em tempo real com **Arduino**
- Interface gráfica organizada em **Tkinter**
- Armazenamento seguro com arquivos `.txt` bem estruturados

Com isso, demonstramos domínio das competências em **programação, automação e integração IoT**, conforme proposto pela disciplina.

---


