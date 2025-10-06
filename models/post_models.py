from pydantic import BaseModel, Field, ConfigDict


class CreatePostRequest(BaseModel):
    """
    Model for POST /posts request (create new post).
    """
    title: str = Field(..., description="Post title")
    body: str = Field(..., description="Post body")
    userId: int = Field(1, description="ID user, default 1")

    def to_dict(self):
        return self.model_dump()


class PostModel(BaseModel):
    """
    Model for response validation (GET, POST, PUT).
    """
    id: int = Field(..., description="Post ID")
    title: str = Field(..., description="Post title")
    body: str = Field(..., description="Post body")
    userId: int = Field(..., description="User ID (who created post)")

    model_config = ConfigDict(
        from_attributes=True,
        extra='ignore'
    )
