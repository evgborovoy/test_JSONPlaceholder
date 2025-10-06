from pydantic import BaseModel, Field, ConfigDict


class CreatePostRequest(BaseModel):
    """
    Model for POST /posts request (create new post).
    """
    title: str = Field(..., description="Post title")
    body: str = Field(..., description="Post body")
    user_id: int = Field(1, alias="userId", description="ID user, default 1")

    model_config = ConfigDict(
        populate_by_name=True,
    )

    def to_dict(self):
        return self.model_dump()


class PostModel(BaseModel):
    """
    Model for response validation (GET, POST, PUT).
    """
    id: int = Field(..., description="Post ID")
    title: str = Field(..., description="Post title")
    body: str = Field(..., description="Post body")
    user_id: int = Field(..., alias="userId", description="User ID (who created post)")

    model_config = ConfigDict(
        from_attributes=True,
        extra='ignore',
        populate_by_name=True,
    )
