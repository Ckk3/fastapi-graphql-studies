from pydantic import BaseModel
from models import session, Post
import strawberry
from strawberry.types import Info
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper


strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()


@strawberry_sqlalchemy_mapper.type(Post)
class PostType:
    pass


@strawberry.type
class Query:
    @strawberry.field
    def get_posts(self, info: Info) -> list[PostType]:
        return session.query(Post).all()

    @strawberry.field
    def hello_world(self, info: Info) -> str:
        return "Hello World"


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_post(self, info: Info, title: str, author: str, content: str) -> PostType:
        new_post = Post(title=title, author=author, content=content)
        print("Create new Post")
        session.add(new_post)
        session.commit()
        print(f"Added new post {new_post.title}")
        return new_post


strawberry_sqlalchemy_mapper.finalize()
schema = strawberry.Schema(query=Query, mutation=Mutation)
