# Detektor spamu w wiadomościach e-mail z wykorzystaniem modeli językowych

Projekt poświęcony wykrywaniu spamu w wiadomościach e-mail z wykorzystaniem klasycznych metod uczenia maszynowego oraz modelu transformera BERT. Głównym celem było porównanie skuteczności podejść opartych na cechach tekstowych z podejściem opartym na semantycznym rozumieniu treści.

## Opis projektu

W repozytorium znajdują się:

- analiza porównawcza modeli klasycznych i transformerowych,
- przygotowanie i wstępna obróbka danych tekstowych,
- eksperymenty z fine-tuningiem modelu BERT,
- zapisane wyniki eksperymentów oraz metryki jakości,
- prosty interfejs graficzny do sprawdzania, czy wiadomość jest spamem.

Główne elementy projektu:

- `projekt_spam_magistra_v3_fixed.ipynb` — notebook z analizą danych, trenowaniem modeli i eksperymentami,
- `spam_checker_gui.py` — aplikacja GUI do testowania modelu na dowolnym tekście,
- `spam_Emails_data.csv` — zbiór danych używany do treningu i ewaluacji,
- `requirements.txt` — lista zależności,
- `results/` — zapisane modele i wyniki eksperymentów,

## Cel i zakres

Projekt obejmuje:

- analizę danych e-mailowych,
- porównanie metod takich jak Naive Bayes, Logistic Regression, SVM, Random Forest, XGBoost,
- ocenę modelu BERT po fine-tuningu,
- analizę metryk klasyfikacji: accuracy, precision, recall, F1, ROC-AUC, PR-AUC,
- przygotowanie gotowego prototypu do wykrywania spamu w praktyce.

## Struktura katalogów

```text
projekt/
├── README.md
├── requirements.txt
├── spam_Emails_data.csv
├── spam_checker_gui.py
├── projekt_spam_magistra_v3_fixed.ipynb
├── results/
│   ├── bert_finetuned/
│   ├── bert_finetuned_0p5x/
│   ├── bert_finetuned_2p0x/
│   ├── bert_finetuned_4p0x/
│   ├── bert_finetuned_8p0x/
│   └── checkpoint-*/
├── *.png
└── *.json / *.pkl
```

## Wymagania

- Python 3.10+
- pip
- system operacyjny: Windows, Linux lub macOS
- karta graficzna nie jest wymagana do uruchamiania modelu, choć może przyspieszyć obliczenia

## Konfiguracja środowiska

1. Utwórz środowisko wirtualne:

```bash
python -m venv .venv
```

2. Aktywuj środowisko:

- Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

- Linux/macOS:

```bash
source .venv/bin/activate
```

3. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

## Uruchamianie notebooka

Notatnik z eksperymentami można otworzyć w VS Code, Jupyter Notebook lub JupyterLab:

```bash
jupyter notebook projekt_spam_magistra_v3_fixed.ipynb
```

Po uruchomieniu notebooka można wykonać kolejne komórki w odpowiedniej kolejności, aby:

- wczytać dane,
- przeprowadzić eksplorację danych,
- trenować modele klasyczne,
- uruchomić fine-tuning BERT,
- porównać wyniki eksperymentów.

## Uruchamianie aplikacji GUI

Aplikacja do sprawdzania spamu w tekście:

```bash
python spam_checker_gui.py
```

Po uruchomieniu otworzy się okno, w którym można wkleić treść wiadomości i sprawdzić, czy została zaklasyfikowana jako spam lub nie-spam.

> Ważna uwaga: skrypt `spam_checker_gui.py` ładuje model z katalogu `bert_finetuned` w bieżącym katalogu roboczym. W repozytorium najczęściej model jest zapisany w katalogu `results/bert_finetuned`. Jeśli uruchomienie kończy się błędem z powodu brakującego katalogu modelu, należy dostosować ścieżkę w kodzie lub skopiować odpowiedni folder modelu do lokalizacji oczekiwanej przez aplikację.

## Zbiór danych

Zbiór danych znajduje się w pliku:

- `spam_Emails_data.csv`

Dane zawierają teksty wiadomości oraz etykiety klasy:

- `Spam`
- `Ham` / `Not Spam`

## Wyniki i artefakty

W katalogu `results/` oraz w katalogu głównym projektu znajdują się artefakty eksperymentów, m.in.:

- wyniki klasyfikacji,
- macierze pomyłek,
- wykresy krzywych ROC/PR,
- porównania modeli,
- pliki modelu BERT w formacie Hugging Face,
- pliki z wynikami i metadanymi eksperymentów.

## Zależności

Lista zależności jest zdefiniowana w pliku `requirements.txt` i obejmuje m.in.:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `torch`
- `transformers`
- `huggingface-hub`
- `accelerate`
- `xgboost`
- `wordcloud`
- `datasets`
- `ipywidgets`
- `ipykernel`