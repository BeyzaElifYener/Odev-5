import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

root = tk.Tk()
root.title("Kullanıcı Girişi")

username_label = tk.Label(root, text="Kullanıcı Adı:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Şifre:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()

    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    if c.fetchone():
        messagebox.showinfo("Başarılı", "Giriş Başarılı!")
        # Başarılı giriş durumunda menüyü göster
        show_menu()
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

def register():
    username = username_entry.get()
    password = password_entry.get()

    c.execute('SELECT * FROM users WHERE username=?', (username,))
    if c.fetchone():
        messagebox.showerror("Hata", "Bu kullanıcı zaten var!")
    else:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Başarılı", "Kullanıcı başarıyla kaydedildi!")

login_button = tk.Button(root, text="Giriş Yap", command=login)
login_button.pack()

register_button = tk.Button(root, text="Kayıt Ol", command=register)
register_button.pack()

def show_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menü")

    compare_button = tk.Button(menu_window, text="Karşılaştır", command=compare_menu)
    compare_button.pack()

    operations_button = tk.Button(menu_window, text="İşlemler", command=operations_menu)
    operations_button.pack()

    exit_button = tk.Button(menu_window, text="Çıkış", command=root.destroy)
    exit_button.pack()

def compare_menu():
    compare_window = tk.Toplevel(root)
    compare_window.title("Karşılaştır")

    text_x_button = tk.Button(compare_window, text="Metin x algoritması ile Karşılaştır", command=compare_x_menu)
    text_x_button.pack()

    text_y_button = tk.Button(compare_window, text="Metin y algoritması ile Karşılaştır", command=compare_y_menu)
    text_y_button.pack()

def calculate_similarity_x(text1, text2):
  
    words_text1 = set(text1.lower().split())
    words_text2 = set(text2.lower().split())

    common_words_count = len(words_text1.intersection(words_text2))
    average_word_count = (len(words_text1) + len(words_text2)) / 2

    similarity_score = common_words_count / average_word_count

    return similarity_score

def compare_x_menu():
    compare_window_x = tk.Toplevel(root)
    compare_window_x.title("Metin Karşılaştırma")

    text1_x_label = tk.Label(compare_window_x, text="Metin X:")
    text1_x_label.pack()
    text1_x_entry = tk.Entry(compare_window_x)
    text1_x_entry.pack()

    text2_y_label = tk.Label(compare_window_x, text="Metin Y:")
    text2_y_label.pack()
    text2_y_entry = tk.Entry(compare_window_x)
    text2_y_entry.pack()

    def select_file(entry):
        filename = filedialog.askopenfilename(initialdir="/", title="Dosya Seç", filetypes=(("Text Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")))
        entry.delete(0, tk.END)
        entry.insert(0, filename)

    file_x_button = tk.Button(compare_window_x, text="Dosya Seç (Metin X)", command=lambda: select_file(text1_x_entry))
    file_x_button.pack()

    file_y_button = tk.Button(compare_window_x, text="Dosya Seç (Metin Y)", command=lambda: select_file(text2_y_entry))
    file_y_button.pack()

    def compare_texts():
    
        text1 = text1_x_entry.get()
        text2 = text2_y_entry.get()

        similarity_score_x = calculate_similarity_x(text1, text2)
        result_x = f"Metin X Algoritması İle Benzerlik Skoru: {similarity_score_x}"

        result_label_x = tk.Label(compare_window_x, text=result_x)
        result_label_x.pack()

    compare_x_button = tk.Button(compare_window_x, text="Karşılaştır", command=compare_texts)
    compare_x_button.pack()

def calculate_similarity_y(text1, text2):

    words_text1 = set(text1.lower().split())
    words_text2 = set(text2.lower().split())

    common_words_count = len(words_text1.intersection(words_text2))
    average_word_count = (len(words_text1) * len(words_text2)) / 2

    similarity_score = common_words_count / average_word_count

    return similarity_score

def compare_y_menu():
    compare_window_y = tk.Toplevel(root)
    compare_window_y.title("Metin Karşılaştırma")

    text1_x_label = tk.Label(compare_window_y, text="Metin X:")
    text1_x_label.pack()
    text1_x_entry = tk.Entry(compare_window_y)
    text1_x_entry.pack()

    text2_y_label = tk.Label(compare_window_y, text="Metin Y:")
    text2_y_label.pack()
    text2_y_entry = tk.Entry(compare_window_y)
    text2_y_entry.pack()

    def select_file(entry):
        filename = filedialog.askopenfilename(initialdir="/", title="Dosya Seç", filetypes=(("Text Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")))
        entry.delete(0, tk.END)
        entry.insert(0, filename)

    file_x_button = tk.Button(compare_window_y, text="Dosya Seç (Metin X)", command=lambda: select_file(text1_x_entry))
    file_x_button.pack()

    file_y_button = tk.Button(compare_window_y, text="Dosya Seç (Metin Y)", command=lambda: select_file(text2_y_entry))
    file_y_button.pack()

    def compare_texts():
        
        text1 = text1_x_entry.get()
        text2 = text2_y_entry.get()

        similarity_score_y = calculate_similarity_y(text1, text2)
        result_x = f"Metin y Algoritması İle Benzerlik Skoru: {similarity_score_y}"

        result_label_x = tk.Label(compare_window_y, text=result_x)
        result_label_x.pack()

    compare_y_button = tk.Button(compare_window_y, text="Karşılaştır", command=compare_texts)
    compare_y_button.pack()

def operations_menu():
    operations_window = tk.Toplevel(root)
    operations_window.title("İşlemler")

    password_button = tk.Button(operations_window, text="Şifre İşlemleri", command=password_menu)
    password_button.pack()

def password_menu():
    password_window = tk.Toplevel(root)
    password_window.title("Şifre İşlemleri")

    change_password_button = tk.Button(password_window, text="Şifre Değiştir", command=change_password_menu)
    change_password_button.pack()

def change_password_menu():
    change_password_window = tk.Toplevel(root)
    change_password_window.title("Şifre Değiştir")

    old_password_label = tk.Label(change_password_window, text="Eski Şifre:")
    old_password_label.pack()
    old_password_entry = tk.Entry(change_password_window, show="*")
    old_password_entry.pack()

    new_password_label = tk.Label(change_password_window, text="Yeni Şifre:")
    new_password_label.pack()
    new_password_entry = tk.Entry(change_password_window, show="*")
    new_password_entry.pack()

    confirm_new_password_label = tk.Label(change_password_window, text="Yeni Şifre Onay:")
    confirm_new_password_label.pack()
    confirm_new_password_entry = tk.Entry(change_password_window, show="*")
    confirm_new_password_entry.pack()

    def change_password():
        old_password = old_password_entry.get()
        new_password = new_password_entry.get()
        confirm_new_password = confirm_new_password_entry.get()

        if new_password == confirm_new_password:
            c.execute('SELECT * FROM users WHERE username=? AND password=?', (username_entry.get(), old_password))
            if c.fetchone():
                c.execute('UPDATE users SET password=? WHERE username=?', (new_password, username_entry.get()))
                conn.commit()
                messagebox.showinfo("Başarılı", "Şifre başarıyla güncellendi!")
                change_password_window.destroy()
            else:
                messagebox.showerror("Hata", "Eski şifre yanlış!")
        else:
            messagebox.showerror("Hata", "Yeni şifreler uyuşmuyor!")

    change_button = tk.Button(change_password_window, text="Değiştir", command=change_password)
    change_button.pack()

root.mainloop()





