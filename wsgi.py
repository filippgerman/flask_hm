from blog.app import create_app
from blog.models.database import db

from blog.models import Articles
    
app = create_app()


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("готово!")


@app.cli.command("create-users")
def create_users():
    from blog.models import User
    username = 'huston'
    password = 'huston'
    email = 'huston@mail.com'
    
    user = User(username=username, password=password, email=email)
    
    db.session.add(user)
    db.session.commit()
    
    print(f"готово! создали юзера: {username}")

@app.cli.command("create-link")
def create_link():
    from blog.models import ArticleTags
    art = int(input('Введите id article: '))
    tag = int(input('Введите id tag: '))
    
    link = ArticleTags(article_id=art, tag_id=tag)
    
    db.session.add(link)
    db.session.commit()
    
    print(f"готово!")

    
@app.cli.command("create-tag")  
def create_tag():
    from blog.models import Tag
    name = input('Введите tag: ')
    tag = Tag(name=name)
    
    db.session.add(tag)
    db.session.commit()
    
    print(f"готово! создали tag: {tag}")


@app.cli.command("create-article")
def create_article():

    title = 'prog'
    text = 'text text'
    author_id = 1

    article = Articles(title=title, text=text, author_id=author_id)
    db.session.add(article)
    db.session.commit()

    print(f'статья создана: {article}')

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )
