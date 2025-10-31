from kivymd.app import MDApp
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class TodoApp(MDApp):
    """Main Todo Application Class"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

    def build(self):
        """Build the application"""
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.title = "Todo App"
        return

    def add_task(self):
        """Add a new task to the list"""
        task_input = self.root.ids.task_input
        task_text = task_input.text.strip()
        
        if task_text:
            task_list = self.root.ids.task_list
            
            # Create list item
            item = TwoLineAvatarIconListItem(
                text=task_text,
                secondary_text="Pending",
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1)
            )
            
            # Checkbox icon
            checkbox = IconLeftWidget(
                icon="checkbox-blank-circle-outline",
                on_release=lambda x, item=item: self.toggle_task(item)
            )
            
            # Delete icon
            delete_btn = IconRightWidget(
                icon="delete",
                on_release=lambda x, item=item: self.delete_task(item)
            )
            
            item.add_widget(checkbox)
            item.add_widget(delete_btn)
            
            task_list.add_widget(item)
            task_input.text = ""

    def toggle_task(self, item):
        """Toggle task completion status"""
        checkbox = item.children[-1]  # Get the checkbox widget
        
        if checkbox.icon == "checkbox-blank-circle-outline":
            # Mark as complete
            checkbox.icon = "check-circle"
            checkbox.theme_icon_color = "Custom"
            checkbox.icon_color = (0, 0.7, 0, 1)
            item.secondary_text = "Completed"
            item.theme_text_color = "Custom"
            item.text_color = (0.5, 0.5, 0.5, 1)
        else:
            # Mark as incomplete
            checkbox.icon = "checkbox-blank-circle-outline"
            checkbox.theme_icon_color = "Primary"
            item.secondary_text = "Pending"
            item.theme_text_color = "Custom"
            item.text_color = (0, 0, 0, 1)

    def delete_task(self, item):
        """Delete a specific task"""
        task_list = self.root.ids.task_list
        task_list.remove_widget(item)

    def clear_all_tasks(self):
        """Show confirmation dialog before clearing all tasks"""
        if not self.dialog:
            self.dialog = MDDialog(
                title="Clear All Tasks?",
                text="Are you sure you want to delete all tasks?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                    MDFlatButton(
                        text="DELETE ALL",
                        theme_text_color="Custom",
                        text_color=(1, 0, 0, 1),
                        on_release=lambda x: self.confirm_clear_all()
                    ),
                ],
            )
        self.dialog.open()

    def confirm_clear_all(self):
        """Clear all tasks after confirmation"""
        task_list = self.root.ids.task_list
        task_list.clear_widgets()
        self.dialog.dismiss()

    def on_stop(self):
        """Clean up when app closes"""
        if self.dialog:
            self.dialog.dismiss()


if __name__ == '__main__':
    TodoApp().run()