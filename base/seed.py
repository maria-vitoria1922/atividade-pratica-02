from database import nova_sessao, engine, Base
from models import Autor, Livro

def popular_banco():
    Base.metadata.create_all(bind=engine)

    session = nova_sessao()

    try:
        autor1 = Autor(nome="Laricia", pais="Brasil")
        autor2 = Autor(nome="Aislanny", pais="Brasil")
        autor3 = Autor(nome="Jeseane", pais="Brasil")

        session.add(autor1)

        livro1 = Livro(titulo="As setes chaves", ano=2021, autor=autor1, disponivel=False)
        livro2 = Livro(titulo="Ala D", ano=2022, autor=autor2, disponivel=True)
        livro3 = Livro(titulo="A intrusa", ano=2020, autor=autor1, disponivel=True)
        livro4 = Livro(titulo="Nunca Minta", ano=2023, autor=autor3, disponivel=False)
        livro5 = Livro(titulo="Nós já moramos aqui", ano=2019, autor=autor2, disponivel=True)
        livro6 = Livro(titulo="1984", ano=1949, autor=autor1, disponivel=True)

        session.add_all([autor2, autor3])
        session.add_all([livro1, livro2, livro3, livro4, livro5, livro6])

        session.commit()
        print("Banco de dados ok!")

    except Exception as e:
        session.rollback()
        print(f"Erro no banco de dados")

    finally:
        session.close()
