import dearpygui.dearpygui as dpg


def save_callback():
    input_text = dpg.get_value("string")
    print(f"Save Clicked {input_text}")


def save_callback_two():
    input_text = dpg.get_value("string2")
    print(f"Save Clicked {input_text}")


class MainWindow:
    def __init__(self, width, height):
        self.__width: int = width
        self.__height: int = height
        self.__title: str = "Spotube"
        self.setup()

    def setup(self):
        dpg.create_context()

        with dpg.window(tag="Primary Window"):
            dpg.add_text(default_value="Spotify Client", label="Spotify Client")
            dpg.add_input_text(label="Path", hint="Quick brown fox", tag="string")
            dpg.add_button(label="Save", callback=save_callback)

            dpg.add_text(default_value="Youtube Client", label="Youtube Client")
            dpg.add_input_text(label="Path", hint="Quick brown fox")
            dpg.add_button(label="Save", callback=save_callback_two)

            dpg.add_text(default_value="Output", label="Output")
            dpg.add_input_text(label="Path", hint="Quick brown fox")

        with dpg.window(label="Tutorial"):
            with dpg.table(header_row=False):

                # use add_table_column to add columns to the table,
                # table columns use child slot 0
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                # add_table_next_column will jump to the next row
                # once it reaches the end of the columns
                # table next column use slot 1
                for i in range(0, 4):
                    with dpg.table_row():
                        for j in range(0, 3):
                            dpg.add_text(f"Row{i} Column{j}")
 

        dpg.create_viewport(title=self.__title, width=self.__width, height=self.__height)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Primary Window", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
