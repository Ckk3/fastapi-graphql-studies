from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schemas import schema


app = FastAPI()
graphql_app = GraphQLRouter(schema=schema, graphiql=True)


# This is like a add_route but the include router get all routes from a custom fastapi.APIRouter created by strawberry
app.include_router(graphql_app, prefix="/graphql")