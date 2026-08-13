import tkinter as tk
from tkinter import scrolledtext, messagebox
import torch
import numpy as np
from transformers import BertTokenizer, BertForSequenceClassification
from pathlib import Path


class SpamCheckerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Detektor Spamu - BERT")
        self.root.geometry("500x415")
        
        # Ładowanie modelu
        self.model = None
        self.tokenizer = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.load_model()
        
        # Tytuł
        title_label = tk.Label(
            root, 
            text=" Detektor Spamu BERT", 
            font=("Arial", 18, "bold"),
            pady=10
        )
        title_label.pack()
        
        # Instrukcja
        instruction_label = tk.Label(
            root, 
            text="Wpisz treść wiadomości email:",
            font=("Arial", 11)
        )
        instruction_label.pack(pady=(15, 5))
        
        # Pole tekstowe
        self.text_input = scrolledtext.ScrolledText(
            root,
            width=65,
            height=8,
            font=("Arial", 10),
            wrap=tk.WORD
        )
        self.text_input.pack(padx=20, pady=5)
        
        # Przycisk sprawdzania
        self.check_button = tk.Button(
            root,
            text="Sprawdź wiadomość",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            command=self.check_spam,
            cursor="hand2",
            padx=20,
            pady=10
        )
        self.check_button.pack(pady=15)
        
        # Wynik
        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 14, "bold"),
            pady=10
        )
        self.result_label.pack()
        
        # Przycisk czyszczenia
        clear_button = tk.Button(
            root,
            text="Wyczyść",
            font=("Arial", 10),
            command=self.clear_text,
            cursor="hand2"
        )
        clear_button.pack()
    
    def load_model(self):
        """Wczytuje zapisany model BERT"""
        model_dir = Path("bert_finetuned")
        
        if not model_dir.exists():
            messagebox.showerror(
                "Błąd", 
                "Brak wytrenowanego modelu!\n\n"
            )
            self.root.destroy()
            return
        
        try:
            self.tokenizer = BertTokenizer.from_pretrained(model_dir)
            self.model = BertForSequenceClassification.from_pretrained(model_dir)
            self.model.to(self.device)
            self.model.eval()
            print(f" Model załadowany z {model_dir}")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się załadować modelu:\n{e}")
            self.root.destroy()
    
    def check_spam(self):
        """Sprawdza czy tekst to spam"""
        text = self.text_input.get("1.0", tk.END).strip()
        
        if not text:
            messagebox.showwarning("Uwaga", "Wpisz treść wiadomości!")
            return
        
        try:
            # Tokenizacja
            inputs = self.tokenizer(
                text,
                return_tensors='pt',
                truncation=True,
                padding=True,
                max_length=128
            )
            
            # Przeniesienie na odpowiednie urządzenie
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            # Predykcja
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits
                prediction = np.argmax(logits.detach().cpu().numpy(), axis=1)[0]
                probabilities = torch.softmax(logits, dim=1).cpu().numpy()[0]
            
            # Wyświetlenie wyniku
            if prediction == 1:
                self.result_label.config(
                    text=f" SPAM ({probabilities[1]*100:.1f}%)",
                    fg="red"
                )
            else:
                self.result_label.config(
                    text=f"NIE-SPAM ({probabilities[0]*100:.1f}%)",
                    fg="green"
                )
                
        except Exception as e:
            messagebox.showerror("Błąd", f"Błąd podczas analizy:\n{e}")
    
    def clear_text(self):
        """Czyszczenie pola tekstowego i wyniku"""
        self.text_input.delete("1.0", tk.END)
        self.result_label.config(text="")


def main():
    root = tk.Tk()
    app = SpamCheckerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
