from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# AVANCE 2 - CLASIFICACIÓN DE FLORES
# Exploración inicial del dataset de imágenes
# ============================================

DATASET_DIR = Path("dataset")
RESULTADOS_DIR = Path("resultados")

RESULTADOS_DIR.mkdir(exist_ok=True)

splits = ["train", "valid", "test"]
extensiones = ["*.jpg", "*.jpeg", "*.png", "*.webp"]

registros = []

print("=== AVANCE 2: EXPLORACIÓN DEL DATASET DE IMÁGENES ===\n")

# Revisar si existe la carpeta dataset
if not DATASET_DIR.exists():
    print("ERROR: No se encontró la carpeta 'dataset'.")
    print("La estructura esperada es:")
    print("dataset/train")
    print("dataset/valid")
    print("dataset/test")
    exit()

# Recorrer train, valid y test
for split in splits:
    split_path = DATASET_DIR / split

    if not split_path.exists():
        print(f"Advertencia: no existe la carpeta {split_path}")
        continue

    # Recorrer clases dentro de cada split
    for clase_path in sorted(split_path.iterdir()):
        if clase_path.is_dir():
            cantidad = 0

            for extension in extensiones:
                cantidad += len(list(clase_path.glob(extension)))

            registros.append({
                "division": split,
                "clase": clase_path.name,
                "cantidad": cantidad
            })

df = pd.DataFrame(registros)

# Validar que haya imágenes
if df.empty:
    print("No se encontraron imágenes.")
    print("Revisa que tengas carpetas como:")
    print("dataset/train/girasol")
    print("dataset/train/rosa")
    print("dataset/train/tulipan")
    exit()

print("Resumen por división y clase:")
print(df)

print("\nCantidad total de imágenes:")
print(df["cantidad"].sum())

print("\nCantidad total por clase:")
print(df.groupby("clase")["cantidad"].sum())

print("\nCantidad total por división:")
print(df.groupby("division")["cantidad"].sum())

# Guardar resumen en CSV
df.to_csv(RESULTADOS_DIR / "resumen_dataset.csv", index=False)

# Crear gráfico de distribución
plt.figure(figsize=(9, 5))

labels = df["clase"] + " - " + df["division"]

plt.bar(labels, df["cantidad"])
plt.title("Distribución de imágenes por clase y división")
plt.xlabel("Clase y división")
plt.ylabel("Cantidad de imágenes")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(RESULTADOS_DIR / "distribucion_dataset.png")
plt.close()

print("\nArchivos generados:")
print("- resultados/resumen_dataset.csv")
print("- resultados/distribucion_dataset.png")

print("\nConclusión del avance:")
print("El dataset inicial de imágenes está organizado en train, valid y test.")
print("Las clases encontradas serán utilizadas posteriormente para entrenar un modelo de clasificación de flores.")

print("\nPróximo paso:")
print("Entrenar un modelo de clasificación de imágenes usando Transfer Learning con ResNet50.")