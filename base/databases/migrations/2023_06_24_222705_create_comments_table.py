"""CreateCommentsTable Migration."""

from masoniteorm.migrations import Migration


class CreateCommentsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("comments") as table:
            table.increments("id")
            
            table.integer("article_id").unsigned()
            table.foreign_id("article_id").references("id").on("articles")
            
            table.integer("user_id").unsigned()
            table.foreign_id("user_id").references("id").on("users")
            
            table.text('body')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("comments")
