
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class TextSummary(models.Model):

    url = fields.CharField(max_length=200)
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    class Meta:
        table = "text_summary"


SummarySchema = pydantic_model_creator(TextSummary, name="TextSummary")