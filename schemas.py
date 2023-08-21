from pydantic import BaseModel
from models import session, Post
import strawberry
from strawberry.types import Info

# class PostSchema(BaseModel):
#     title: str
#     content: str

# Create PostType
@strawberry.type
class PostType:
    title: str
    author: str
    content: str


@strawberry.type
class Query:
    @strawberry.field
    def get_posts(self, info: Info) -> list[PostType]:
        return [
            PostType(title=post.title, author=post.author, content=post.content)
            for post in session.query(Post).all()
        ]

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
        return PostType(
            title=new_post.title, author=new_post.author, content=new_post.content
        )


schema = strawberry.Schema(query=Query, mutation=Mutation)
