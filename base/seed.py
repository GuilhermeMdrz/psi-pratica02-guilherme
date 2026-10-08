from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    autor01 = Autor(nome='Machado de Assis', pais='Brasil')
    autor02 = Autor(nome='Lima Barreto', pais='Brasil')
    autor03 = Autor(nome ='Jorge Amado', pais='Brasil')

    livro01 = Livro(titulo='Memórias Póstumas de Brás Cubas', ano='1881', disponivel=False, autor='Machado de Assis')
    livro02 = Livro(titulo='O Cortiço', ano='1890', disponivel=True, autor='Aluísio Azevedo')
    livro03 = Livro(titulo='Dom Casmurro', ano='1899', disponivel=True, autor='Machado de Assis')
    livro04 = Livro(titulo='Os Sertões', ano='1902', disponivel=True, autor='Euclides da Cunha')
    livro05 = Livro(titulo='Triste Fim de Policarpo Quaresma', ano='1915 ', disponivel=True, autor='Lima Barreto')
    livro06 = Livro(titulo='Capitães da Areia', ano='1937', disponivel=False, autor='Jorge Amado')
    # TODO: inclua livros disponíveis e indisponíveis.
    # TODO: use session.add ou session.add_all e finalize com session.commit().
    pass
