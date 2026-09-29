# Lab Data Manager 🧪

Aplicación web moderna para gestionar datos de investigación científica universitaria con análisis estadístico integrado.

Una plataforma intuitiva, moderna y científica para estudiantes de ingeniería biológica que desean registrar, analizar y visualizar datos experimentales sin necesidad de conocimientos avanzados en programación o estadística.

## 🎯 Características

- ✅ **Ingreso de datos intuitivo** con validación automática
- ✅ **Gráficas interactivas** (crecimiento, boxplots, correlaciones, comparaciones)
- ✅ **Estadística descriptiva** completa
- ✅ **Análisis ANOVA** con verificación de supuestos
- ✅ **Pruebas post-hoc** (Tukey HSD)
- ✅ **Análisis de medidas repetidas** para variables longitudinales
- ✅ **Correlaciones** (Pearson y Spearman)
- ✅ **Análisis multivariable** (MANOVA, matriz de correlación, PCA)
- ✅ **Control de calidad** de datos
- ✅ **Importación** CSV y Excel
- ✅ **Exportación** CSV, Excel y PDF
- ✅ **Generación de informes** automáticos
- ✅ **Base de datos flexible** que permite agregar variables nuevas
- ✅ **Datos simulados** de demostración claramente marcados

## 🚀 Inicio Rápido

### Requisitos Previos
- Node.js 18+
- Python 3.10+
- npm o yarn

### Instalación

```bash
# Clonar repositorio
git clone https://github.com/isabelaospina24/lab-data-manager.git
cd lab-data-manager

# Backend
cd backend
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed_data.py
uvicorn app.main:app --reload --port 8000

# Frontend (en otra terminal)
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173  
Backend: http://localhost:8000  
Documentación API: http://localhost:8000/docs

## 📊 Estructura del Proyecto

```
lab-data-manager/
├── frontend/              # React + TypeScript + Tailwind
│   ├── src/
│   │   ├── components/   # Componentes reutilizables
│   │   ├── pages/        # Páginas principales
│   │   ├── hooks/        # Custom React hooks
│   │   ├── lib/          # Utilidades
│   │   ├── types/        # Tipos TypeScript
│   │   └── App.tsx
│   └── package.json
│
├── backend/               # FastAPI + Python
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── services/
│   │   └── routers/
│   ├── requirements.txt
│   └── seed_data.py
│
└── README.md
```

## 📝 Variables Experimentales

### Medidas Una Sola Vez
- Día de germinación (días)
- Materia seca (g)
- Masa total (g)
- Tamaño de raíz (cm)

### Medidas Inicial-Final
- pH del suelo
- Fósforo total del suelo
- Nitrógeno total del suelo

### Medidas Diariamente
- Tamaño del tallo (cm)
- Número de hojas
- Grosor del tallo (mm)
- Temperatura (°C)

## 📈 Análisis Disponibles

✅ Estadística descriptiva (n, media, mediana, DE, varianza, mínimo, máximo, CV, SEM)  
✅ ANOVA con verificación de supuestos  
✅ Kruskal-Wallis y Welch ANOVA como alternativas  
✅ Pruebas post-hoc (Tukey HSD)  
✅ ANOVA de medidas repetidas  
✅ Correlaciones (Pearson y Spearman)  
✅ MANOVA y análisis multivariable  
✅ PCA como análisis exploratorio  

## 🎓 Pensado para Estudiantes

- Interfaz intuitiva sin necesidad de conocimientos avanzados
- Explicaciones estadísticas en lenguaje sencillo
- Validaciones automáticas para evitar errores
- Advertencias cuando los supuestos no se cumplen
- Nunca elimina datos automáticamente
- Datos simulados claramente marcados

## 🔍 Control de Calidad

- Detección de valores atípicos (sin eliminación automática)
- Distinción entre 0, NA y ND
- Detección de duplicados
- Advertencias para datos incompletos
- Dashboard de control de calidad

## 📋 Para Más Información

Vea la [documentación completa](./DOCUMENTATION.md)

---

**Versión:** 1.0.0 | **Estado:** En desarrollo
