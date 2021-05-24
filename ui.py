from tkinter import *
from recommender import netflix

window = Tk()
window.title('Netflix Movie Recommender')
window.geometry('800x600')

label = StringVar(window)
label.set("")

hereare = StringVar(window)
hereare.set("") 

language = StringVar(window)
language.set('select language')

genre = StringVar(window)
genre.set('select genre')

age = StringVar(window)
age.set('select age')


def recommend():
    answer = netflix(language.get(), genre.get(), age.get())
    label.set(answer)
    hereare.set('Here are some top movies recommended for you: ')
    print(str(language))


Label(window, text='Welcome to Netflix!!!').pack(pady=10)
OptionMenu(window, language, 'English', 'Hindi').pack(pady=10)
OptionMenu(window, genre, 'action', 'comedy', 'crime and mystery', 'documentary',
           'fantasy', 'horror', 'romance', 'sci-fi', 'family fun').pack(pady=10)
OptionMenu(window, age, 'kids', 'teenagers', 'adult', 'family').pack(pady=10)
Label(window, textvariable=hereare).pack(pady=10)
Label(window, textvariable=label).pack(pady=10)
Button(window, text="Recommend", command=recommend).place(relx=0.45,rely=0.9)
window.update()


window.mainloop()
