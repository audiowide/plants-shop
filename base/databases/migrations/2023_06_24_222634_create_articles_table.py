"""CreateArticlesTable Migration."""

from masoniteorm.migrations import Migration


class CreateArticlesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("ontroller") as table:
            table.increments("id")
            table.string("title")
            table.string("slug").unique()
            
            table.integer("user_id").unsigned()
            table.foreign_id("user_id").references("id").on("users")
            
            table.integer("tag_id").unsigned()
            table.foreign_id("tag_id").references("id").on("tags")
            
            table.text("body")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("ontroller")
