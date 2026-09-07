# Customtkinter-powers-store
<h1 align="center">🛒 Tienda de Poderes - CustomTkinter</h1>

<p align="center">
  Aplicación de escritorio moderna desarrollada en Python utilizando <b>CustomTkinter</b> y <b>Pillow</b>, que simula una tienda interactiva con gestión de saldo en tiempo real, reloj dinámico y ventanas de confirmación independientes.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/CustomTkinter-00599C?style=for-the-badge&logo=python&logoColor=white" alt="CustomTkinter"/>
  <img src="https://img.shields.io/badge/Pillow-328F33?style=for-the-badge&logo=python&logoColor=white" alt="Pillow"/>
</p>

---

## ✨ Características Principales

- 🕒 **Reloj en Tiempo Real:** Incorpora un temporizador dinámico en formato de 12 horas (AM/PM) en la barra superior con la libreria time.
- 💰 **Gestión de Saldo Reactiva:** Control de dinero disponible con alertas visuales temporales en caso de fondos insuficientes.
- 🪟 **Ventanas Secundarias Seguras (`CTkToplevel`):** Sistema de confirmación de compra modal que evita múltiples instancias abiertas simultáneamente y gestiona el foco de la aplicación.
- 🎨 **Interfaz Moderna:** Diseño responsivo estructurado con marcos personalizados, tipografías institucionales y soporte nativo para imágenes mediante la libreria de `Pillow`.

---

## 🛠️ Requisitos e Instalación

1. **Asegúrate de tener Python instalado y descarga las dependencias necesarias:**
   ```bash
   pip install customtkinter pillow
