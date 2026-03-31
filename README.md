# Inferencia Difusa | Fuzzy Inference

Proyecto académico orientado a la implementación y análisis de un sistema de inferencia difusa aplicado a un problema de decisión.

Academic project focused on implementing and analyzing a fuzzy inference system applied to a decision-making problem.

## Índice | Table of Contents

- [Español](#español)
  - [1. Resumen](#1-resumen)
  - [2. Objetivo](#2-objetivo)
  - [3. Alcance](#3-alcance)
  - [4. Estructura del proyecto](#4-estructura-del-proyecto)
  - [5. Requisitos](#5-requisitos)
  - [6. Ejecución](#6-ejecución)
  - [7. Metodología general](#7-metodología-general)
  - [8. Resultados esperados](#8-resultados-esperados)
  - [9. Próximos pasos](#9-próximos-pasos)
  - [10. Autoría](#10-autoría)
- [English](#english)
  - [1. Overview](#1-overview)
  - [2. Objective](#2-objective)
  - [3. Scope](#3-scope)
  - [4. Project structure](#4-project-structure)
  - [5. Requirements](#5-requirements)
  - [6. Running the project](#6-running-the-project)
  - [7. General methodology](#7-general-methodology)
  - [8. Expected outcomes](#8-expected-outcomes)
  - [9. Next steps](#9-next-steps)
  - [10. Authorship](#10-authorship)

---

## Español

### 1. Resumen

Este repositorio contiene una implementación en Python de un enfoque de inferencia difusa, desarrollada en el contexto de la asignatura de Redes Neuronales. El proyecto busca modelar reglas lingüísticas y transformar entradas numéricas en decisiones interpretables.

### 2. Objetivo

Diseñar y ejecutar un sistema de inferencia difusa que permita:

- Definir variables lingüísticas de entrada y salida.
- Establecer funciones de membresía.
- Formular reglas difusas basadas en conocimiento experto.
- Obtener una salida final mediante un proceso de defuzzificación.

### 3. Alcance

El proyecto está orientado a fines académicos y demostrativos. Incluye:

- Construcción del modelo difuso.
- Ejecución de casos de prueba representativos.
- Análisis cualitativo de resultados.

No incluye, por defecto, despliegue en producción ni integración con interfaces web.

### 4. Estructura del proyecto

- `InferenciaDifusaJuanParedes.py`: Script principal con la lógica del sistema difuso.
- `Actividad Inferencia Difusa Juan Paredes.pdf`: Documento de soporte académico.
- `Inferencia Difusa.rar`: Archivo comprimido con materiales del proyecto.

### 5. Requisitos

- Python 3.9 o superior.
- Dependencias de Python necesarias para ejecutar el script (según imports del archivo principal).

### 6. Ejecución

1. Crear y activar un entorno virtual (opcional, recomendado).
2. Instalar dependencias necesarias.
3. Ejecutar el script principal:

```bash
python InferenciaDifusaJuanParedes.py
```

### 7. Metodología general

El flujo de trabajo del sistema sigue, de forma general, estas etapas:

1. Definición de variables de entrada y salida.
2. Fuzzificación de entradas.
3. Evaluación de reglas difusas.
4. Agregación de resultados.
5. Defuzzificación para obtener una salida crisp.

### 8. Resultados esperados

- Salidas interpretables alineadas con las reglas establecidas.
- Comportamiento coherente ante cambios en entradas.
- Evidencia del valor explicativo de la lógica difusa.

### 9. Próximos pasos

- Documentar ejemplos de entrada/salida con casos concretos.
- Incluir pruebas automáticas para validar reglas.
- Agregar visualizaciones de funciones de membresía y superficies de decisión.

### 10. Autoría

Proyecto desarrollado por Juan Paredes en el marco de actividades académicas.

---

## English

### 1. Overview

This repository contains a Python implementation of a fuzzy inference approach, developed in the context of a Neural Networks course. The project models linguistic rules and transforms numeric inputs into interpretable decisions.

### 2. Objective

Design and run a fuzzy inference system that can:

- Define input and output linguistic variables.
- Establish membership functions.
- Formulate fuzzy rules based on expert knowledge.
- Produce a final output through defuzzification.

### 3. Scope

This project is intended for academic and demonstration purposes. It includes:

- Fuzzy model construction.
- Execution of representative test cases.
- Qualitative analysis of outcomes.

It does not include production deployment or web interface integration by default.

### 4. Project structure

- `InferenciaDifusaJuanParedes.py`: Main script containing the fuzzy system logic.
- `Actividad Inferencia Difusa Juan Paredes.pdf`: Supporting academic document.
- `Inferencia Difusa.rar`: Compressed file with project materials.

### 5. Requirements

- Python 3.9 or higher.
- Required Python dependencies to run the main script (according to its imports).

### 6. Running the project

1. Create and activate a virtual environment (optional, recommended).
2. Install required dependencies.
3. Run the main script:

```bash
python InferenciaDifusaJuanParedes.py
```

### 7. General methodology

At a high level, the system workflow follows these stages:

1. Define input and output variables.
2. Fuzzify inputs.
3. Evaluate fuzzy rules.
4. Aggregate rule outputs.
5. Defuzzify to obtain a crisp value.

### 8. Expected outcomes

- Interpretable outputs aligned with the defined rule base.
- Coherent behavior under input changes.
- Evidence of the explanatory value of fuzzy logic.

### 9. Next steps

- Document concrete input/output examples.
- Add automated tests to validate rules.
- Include visualizations for membership functions and decision surfaces.

### 10. Authorship

Project developed by Juan Paredes as part of academic coursework.
