from pydantic import BaseModel, field_validator


class Post(BaseModel):
    id: int
    title: str

    @field_validator("id")
    def check_that_id_is_less_than_two(cls, v):
        if v > 4:
            raise ValueError('ID is not less than two')
        else:
            return v

    @field_validator("title")
    def check_that_title_include_post_string(cls, b):
        if b != "Post 1" and b != "Post 2" and b != "Post 3":
            raise ValueError('Titles does not include Post 1 and Post 2 and Post 3')
        else:
            return b

