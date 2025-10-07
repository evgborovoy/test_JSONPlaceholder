from pydantic import BaseModel, Field, ConfigDict


class CommentModel(BaseModel):
    """
    Model for response validation, GET /posts/{id}/comments.
    """

    post_id: int = Field(..., alias="postId", description="Post ID")
    id: int = Field(..., description="Comment ID")
    name: str
    email: str
    body: str

    model_config = ConfigDict(
        from_attributes=True,
        extra='ignore',
        populate_by_name=True,
    )
