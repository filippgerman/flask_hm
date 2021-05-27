from blog.app import create_app
from blog.models.database import db


app = create_app()


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("готово!")


@app.cli.command("create-users")
def create_users():
    from blog.models import User
    username = input('Введите имя пользователя: ')
    password = input('Введите пароль: ')
    email = input('Введите email: ')
    
    user = User(username=username, password=password, email=email)
    
    db.session.add(user)
    db.session.commit()
    
    print(f"готово! создали юзера: {username}")
    

@app.cli.command("create-article")
def create_article():
    from blog.models import Articles
    title = input('Введите название статьи: ')
    text = input('Введите текст статьи: ')
    author_id = int(input('Введите айди автора: '))

    article = Articles(title=title, text=text, author_id=author_id)
    db.session.add(article)
    db.session.commit()

    print(f'статья создана: {article}')

app.run(
    host="0.0.0.0",
    debug=True,
)
