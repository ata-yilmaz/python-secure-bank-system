import tkinter as tk
from tkinter import messagebox


class BankApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Secure Bank Automation System")
    self.root.geometry("420x520")
    self.root.resizable(False, False)

    # Hesap Bilgileri Değişkenleri
    self.holder_name = ""
    self.balance = 0.0
    self.password = ""
    self.recovery_question = ""
    self.recovery_answer = ""
    self.login_attempts = 3

    # Uygulama açıldığında önce Hesap Kurulum Ekranını çalıştır
    self.setup_account_screen()

  def clear_screen(self):
    """Penceredeki mevcut widget'ları temizler"""
    for widget in self.root.winfo_children():
      widget.destroy()

  def setup_account_screen(self):
    self.clear_screen()

    tk.Label(
        self.root,
        text="Welcome to Bank System",
        font=("Arial", 16, "bold"),
        fg="#0D47A1",
    ).pack(pady=20)
    tk.Label(
        self.root, text="Please setup your account first", font=("Arial", 11)
    ).pack(pady=5)

    # İsim Alanı
    tk.Label(self.root, text="Full Name:", font=("Arial", 10)).pack(pady=2)
    self.entry_name = tk.Entry(self.root, font=("Arial", 11), width=25)
    self.entry_name.pack(pady=2)

    # Şifre Alanı (4 Hane Kuralı)
    tk.Label(self.root, text="Set Password:", font=("Arial", 10)).pack(pady=2)
    self.entry_pass = tk.Entry(
        self.root, show="*", font=("Arial", 11), width=25
    )
    self.entry_pass.pack(pady=2)

    # Silik/Gri Bilgilendirme Notu
    tk.Label(
        self.root,
        text="* Password must be exactly 4 digits",
        font=("Arial", 8, "italic"),
        fg="#777777",
    ).pack(pady=1)

    # Kurtarma Sorusu
    tk.Label(
        self.root, text="Security Question (e.g., Pet's name?):", font=("Arial", 10)
    ).pack(pady=2)
    self.entry_q = tk.Entry(self.root, font=("Arial", 11), width=25)
    self.entry_q.pack(pady=2)

    # Kurtarma Cevabı
    tk.Label(self.root, text="Security Answer:", font=("Arial", 10)).pack(pady=2)
    self.entry_a = tk.Entry(self.root, font=("Arial", 11), width=25)
    self.entry_a.pack(pady=2)

    tk.Button(
        self.root,
        text="Create Account",
        command=self.save_account,
        bg="#1976D2",
        fg="white",
        font=("Arial", 11, "bold"),
        width=20,
    ).pack(pady=15)

  def save_account(self):
    name = self.entry_name.get().strip()
    pwd = self.entry_pass.get().strip()
    q = self.entry_q.get().strip()
    a = self.entry_a.get().strip().lower()

    if not name or not pwd or not q or not a:
      messagebox.showerror(
          "Error", "Please fill in all fields to create an account!"
      )
      return

    # 4 haneli şifre kontrolü
    if not pwd.isdigit() or len(pwd) != 4:
      messagebox.showerror(
          "Error", "Password must be numeric and exactly 4 digits!"
      )
      return

    self.holder_name = name
    self.password = pwd
    self.recovery_question = q
    self.recovery_answer = a
    self.balance = 0.0

    messagebox.showinfo("Success", "Account created successfully!")
    self.login_screen()

  def login_screen(self):
    self.clear_screen()
    self.login_attempts = 3

    tk.Label(
        self.root, text="Secure Bank Login", font=("Arial", 16, "bold"), fg="#0D47A1"
    ).pack(pady=30)
    tk.Label(
        self.root, text=f"Account Holder: {self.holder_name}", font=("Arial", 11)
    ).pack(pady=5)
    tk.Label(self.root, text="Enter Your Password (4 digits):", font=("Arial", 10)).pack(
        pady=5
    )

    self.login_pass_entry = tk.Entry(self.root, show="*", font=("Arial", 12))
    self.login_pass_entry.pack(pady=5)

    tk.Button(
        self.root,
        text="Log In",
        command=self.check_login,
        bg="#1976D2",
        fg="white",
        font=("Arial", 11),
        width=15,
    ).pack(pady=10)

    tk.Button(
        self.root,
        text="Forgot Password?",
        command=self.forgot_password,
        font=("Arial", 9),
        fg="#1565C0",
        relief="flat",
    ).pack(pady=5)

  def check_login(self):
    if self.login_pass_entry.get() == self.password:
      self.main_menu()
    else:
      self.login_attempts -= 1
      if self.login_attempts > 0:
        messagebox.showerror(
            "Access Denied",
            f"Incorrect password! Remaining attempts: {self.login_attempts}",
        )
      else:
        messagebox.showwarning(
            "Locked",
            "3 failed attempts. Redirecting to password recovery.",
        )
        self.forgot_password()

  def forgot_password(self):
    self.clear_screen()

    tk.Label(
        self.root, text="Password Recovery", font=("Arial", 16, "bold"), fg="#0D47A1"
    ).pack(pady=20)
    tk.Label(
        self.root,
        text=f"Security Question:\n{self.recovery_question}",
        font=("Arial", 11),
        fg="#333",
    ).pack(pady=10)

    tk.Label(self.root, text="Your Answer:", font=("Arial", 10)).pack(pady=2)
    self.recovery_answer_entry = tk.Entry(self.root, font=("Arial", 11), width=25)
    self.recovery_answer_entry.pack(pady=5)

    tk.Label(self.root, text="New Password:", font=("Arial", 10)).pack(pady=2)
    self.new_pass_entry = tk.Entry(
        self.root, show="*", font=("Arial", 11), width=25
    )
    self.new_pass_entry.pack(pady=5)
    tk.Label(
        self.root,
        text="* Must be 4 digits",
        font=("Arial", 8, "italic"),
        fg="#777777",
    ).pack(pady=1)

    tk.Button(
        self.root,
        text="Reset Password",
        command=self.verify_and_reset,
        bg="#FFA000",
        fg="white",
        font=("Arial", 11, "bold"),
        width=20,
    ).pack(pady=15)

    tk.Button(
        self.root,
        text="Back to Login",
        command=self.login_screen,
        font=("Arial", 9),
        fg="gray",
        relief="flat",
    ).pack(pady=5)

  def verify_and_reset(self):
    ans = self.recovery_answer_entry.get().strip().lower()
    new_pwd = self.new_pass_entry.get().strip()

    if ans != self.recovery_answer:
      messagebox.showerror("Error", "Incorrect security answer!")
      return

    if not new_pwd.isdigit() or len(new_pwd) != 4:
      messagebox.showerror(
          "Error", "New password must be numeric and exactly 4 digits!"
      )
      return

    self.password = new_pwd
    messagebox.showinfo("Success", "Your password has been reset successfully!")
    self.login_screen()

  def main_menu(self):
    self.clear_screen()

    tk.Label(
        self.root, text=f"Welcome, {self.holder_name}", font=("Arial", 14, "bold"), fg="#0D47A1"
    ).pack(pady=20)

    # Ana Menü Seçenekleri (Çok Katmanlı Yönlendirme)
    tk.Button(
        self.root,
        text="Check Balance",
        command=self.screen_check_balance,
        width=25,
        font=("Arial", 11),
        bg="#E3F2FD",
        fg="#0D47A1",
    ).pack(pady=10)

    tk.Button(
        self.root,
        text="Deposit Money",
        command=lambda: self.screen_transaction("deposit"),
        width=25,
        font=("Arial", 11),
        bg="#E3F2FD",
        fg="#0D47A1",
    ).pack(pady=10)

    tk.Button(
        self.root,
        text="Withdraw Money",
        command=lambda: self.screen_transaction("withdraw"),
        width=25,
        font=("Arial", 11),
        bg="#E3F2FD",
        fg="#0D47A1",
    ).pack(pady=10)

    tk.Button(
        self.root,
        text="Log Out",
        command=self.login_screen,
        width=25,
        font=("Arial", 11),
        bg="#D32F2F",
        fg="white",
    ).pack(pady=30)

  def screen_check_balance(self):
    self.clear_screen()

    tk.Label(
        self.root, text="Account Balance", font=("Arial", 16, "bold"), fg="#0D47A1"
    ).pack(pady=30)

    tk.Label(
        self.root,
        text=f"Your Current Balance:\n${self.balance:.2f}",
        font=("Arial", 14, "bold"),
        fg="#2e7d32",
    ).pack(pady=30)

    tk.Button(
        self.root,
        text="Back to Menu",
        command=self.main_menu,
        width=20,
        font=("Arial", 11),
        bg="#757575",
        fg="white",
    ).pack(pady=20)

  def screen_transaction(self, trans_type):
    self.clear_screen()

    title_text = (
        "Deposit Money" if trans_type == "deposit" else "Withdraw Money"
    )
    btn_color = "#1976D2" if trans_type == "deposit" else "#E65100"

    tk.Label(self.root, text=title_text, font=("Arial", 16, "bold"), fg="#0D47A1").pack(
        pady=25
    )

    # Anlık güncellenen bakiye etiketi
    self.trans_balance_label = tk.Label(
        self.root,
        text=f"Current Balance: ${self.balance:.2f}",
        font=("Arial", 11, "bold"),
        fg="#2e7d32",
    )
    self.trans_balance_label.pack(pady=10)

    tk.Label(self.root, text="Enter Amount ($):", font=("Arial", 11)).pack(
        pady=5
    )
    self.trans_amount_entry = tk.Entry(
        self.root, font=("Arial", 12), width=15, justify="center"
    )
    self.trans_amount_entry.pack(pady=5)

    self.trans_status_label = tk.Label(
        self.root, text="", font=("Arial", 10), fg="#333"
    )
    self.trans_status_label.pack(pady=10)

    tk.Button(
        self.root,
        text="Confirm",
        command=lambda: self.execute_transaction(trans_type),
        width=20,
        font=("Arial", 11, "bold"),
        bg=btn_color,
        fg="white",
    ).pack(pady=10)

    tk.Button(
        self.root,
        text="Back to Menu",
        command=self.main_menu,
        width=20,
        font=("Arial", 10),
        bg="#757575",
        fg="white",
    ).pack(pady=5)

  def execute_transaction(self, trans_type):
    amount_str = self.trans_amount_entry.get().strip()
    try:
      amount = float(amount_str)
      if amount <= 0:
        self.trans_status_label.config(
            text="Error: Amount must be greater than 0!", fg="red"
        )
        return

      if trans_type == "deposit":
        self.balance += amount
        self.trans_status_label.config(
            text=f"Successfully deposited ${amount:.2f}!", fg="green"
        )
      elif trans_type == "withdraw":
        if amount <= self.balance:
          self.balance -= amount
          self.trans_status_label.config(
              text=f"Successfully withdrew ${amount:.2f}!", fg="green"
          )
        else:
          self.trans_status_label.config(
              text="Error: Insufficient balance!", fg="red"
          )

      # Ekrandaki bakiyeyi anlık olarak güncelle ve giriş kutusunu temizle
      self.trans_balance_label.config(text=f"Current Balance: ${self.balance:.2f}")
      self.trans_amount_entry.delete(0, tk.END)

    except ValueError:
      self.trans_status_label.config(
          text="Error: Please enter a valid number!", fg="red"
      )


if __name__ == "__main__":
  root = tk.Tk()
  app = BankApp(root)
  root.mainloop()
