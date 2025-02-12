# CQTraining: Variational Quantum Algorithms Workshop  

This repository contains materials for the **Variational Quantum Algorithms (VQA) Workshop** as part of the **CQTraining** program. The workshop is designed to be **interactive and hands-on**, focusing on the **Variational Quantum Eigensolver (VQE)** and its applications in quantum computing using **Qiskit**.  

---

## 📂 Repository Structure  

- `notebooks/` → Contains Jupyter notebooks for each chapter of the workshop.  
- `utils/` → Utility functions for the workshop.  
- `correctors/` → Correction materials for exercises.  
- `Start.ipynb` → **Entry point** to the workshop. Open this first!  
- `vqa_env.yml` → Conda environment file for installation.  

---

## 🛠 Installation  

The workshop requires **Python** and **Qiskit**. It is recommended to use **Conda** for environment management.  

### **1️⃣ Install Conda (if not already installed)**  

#### 🔹 **Windows**  
Download and install **[Miniconda](https://docs.conda.io/en/latest/miniconda.html)** or **[Anaconda](https://www.anaconda.com/download/)**.  

#### 🔹 **macOS & Linux**  
Use the following command in the terminal:  

```bash
# Install Miniconda (lightweight version of Anaconda)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
Follow the instructions, then restart your terminal.  

---

### **2️⃣ Create and Activate the Environment**  

Clone the repository and navigate into it:  

```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

Then, create the environment using the provided `vqa_env.yml` file:  

```bash
conda env create -f vqa_env.yml
```

Activate the environment:  

- **Windows**:  
  ```bash
  conda activate vqa_env
  ```
- **macOS/Linux**:  
  ```bash
  source activate vqa_env
  ```

---

### **3️⃣ Launch the Workshop**  

Start Jupyter Notebook:  

```bash
jupyter notebook
```

Then, open **`Start.ipynb`**, which will guide you through the workshop.  

---

## 🚀 Getting Started  

1. Open `Start.ipynb` in Jupyter Notebook.  
2. Follow the instructions in each section.  
3. The workshop is structured in linked notebooks—simply follow the prompts.  
4. If you run into issues, ensure you have activated the Conda environment.  

---

## 🛠 Troubleshooting  

If you encounter issues, try the following:  

- **Environment not found?** Run `conda env list` to check installed environments.  
- **Missing packages?** Run `conda install -n vqa_env qiskit jupyter` to manually install them.  
- **Kernel not showing in Jupyter?** Run `python -m ipykernel install --user --name=vqa_env`.  

For further assistance, refer to the [Qiskit documentation](https://qiskit.org/documentation/).  

---

## 📜 License  

This workshop is provided under the **MIT License**. Feel free to use and modify it for educational purposes.  
