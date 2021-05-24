from data import movies

def netflix(language, genre, age):
    answer = movies[language.lower()][genre.lower()][age.lower()]
    print('Here are some top movies recommended for you:')
    print(answer)
    return answer
